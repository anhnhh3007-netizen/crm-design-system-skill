#!/usr/bin/env python3
"""Dựng danh mục component hợp lệ từ 2 file: thư viện Component + CRM-HR-WEB.

    FIGMA_TOKEN=figd_... python3 build-catalog.py

Ghi ra (cạnh skill):
  references/catalog.md    — bảng tra cho người/Claude
  references/catalog.json  — dữ liệu cho script audit (whitelist key)

Nguồn:
  A. Thư viện Component (m1uk…): mọi component set / component publish, kèm prop + kích thước.
  B. CRM-HR-WEB (GztI…): component cục bộ (định nghĩa trong file) và component từ thư viện ngoài
     chưa publish nhưng đang dùng trên các màn (chỉ dùng được bên trong CRM-HR-WEB, lấy qua instance mẫu).
Mỗi component có số lần dùng trên các màn CRM và một instance mẫu (node id + trang) để getMainComponentAsync().
"""
import collections, json, os, sys, time, urllib.error, urllib.request

LIB = 'm1uk68gT43hnMwKYOmv6vE'
CRM = 'GztI8Yyl0PJ1GE0pptPi48'
LOCAL_PAGE = '962:148876'
# Trang không phải màn sản phẩm — bỏ qua khi đếm mức dùng.
SKIP_PAGES = ('Thumbnail', 'Site map', 'Chart', '---', 'Functional Screenshots', 'Demo UI', 'HopeRun UI',
              'Test Design System', 'Presentation', 'Research', 'Draft')
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, '..', 'references')


def get(path, tries=5):
    req = urllib.request.Request('https://api.figma.com/v1/' + path, headers={'X-Figma-Token': os.environ['FIGMA_TOKEN']})
    for i in range(tries):
        try:
            return json.load(urllib.request.urlopen(req, timeout=600))
        except urllib.error.HTTPError as e:
            if e.code == 429 or e.code >= 500:
                time.sleep(int(e.headers.get('Retry-After') or 20 * (i + 1))); continue
            raise
        except (TimeoutError, urllib.error.URLError):
            time.sleep(10 * (i + 1))
    raise RuntimeError('quá số lần thử: ' + path)


def log(*a):
    print(*a, file=sys.stderr, flush=True)


def prop_summary(defs):
    out = []
    for k, v in (defs or {}).items():
        name = k.split('#')[0]
        if v['type'] == 'VARIANT':
            out.append(f"{name}=" + '|'.join(v.get('variantOptions', [])))
        else:
            out.append(f"{name}:{v['type'].lower()}")
    return out


def status_of(name, page):
    s = (page or '') + ' ' + name
    if '🚧' in s: return 'cấm'
    if 'Parts' in s or name.startswith(('.', '_')): return 'part'
    if page in ('Demo', 'Chart'): return 'demo'
    return 'ok'


def main():
    # ---------- A. Thư viện Component ----------
    log('A. thư viện Component')
    sets = get(f'files/{LIB}/component_sets')['meta']['component_sets']
    comps = get(f'files/{LIB}/components')['meta']['components']
    lib_comp_keys = {c['key'] for c in comps}
    standalone = [c for c in comps if not (c.get('containing_frame') or {}).get('containingComponentSet')]
    entries = {}
    for s in sets:
        entries[s['key']] = {'source': 'Component', 'kind': 'set', 'name': s['name'], 'key': s['key'], 'node': s['node_id'],
                             'page': (s.get('containing_frame') or {}).get('pageName', '').strip(), 'desc': s.get('description', '')}
    for c in standalone:
        entries[c['key']] = {'source': 'Component', 'kind': 'component', 'name': c['name'], 'key': c['key'], 'node': c['node_id'],
                             'page': (c.get('containing_frame') or {}).get('pageName', '').strip(), 'desc': c.get('description', '')}
    lib_nodes = [e['node'] for e in entries.values()]
    for i in range(0, len(lib_nodes), 25):
        r = get(f'files/{LIB}/nodes?depth=1&ids=' + ','.join(lib_nodes[i:i + 25]))['nodes']
        for e in entries.values():
            n = (r.get(e['node']) or {}).get('document')
            if not n: continue
            e['props'] = prop_summary(n.get('componentPropertyDefinitions'))
            first = (n.get('children') or [n])[0] if n['type'] == 'COMPONENT_SET' else n
            b = first.get('absoluteBoundingBox') or {}
            e['size'] = [round(b.get('width', 0)), round(b.get('height', 0))]
            e['variants'] = len(n.get('children', [])) if n['type'] == 'COMPONENT_SET' else 1
    for e in entries.values():
        e['status'] = status_of(e['name'], e['page'])

    # ---------- B. CRM-HR-WEB ----------
    log('B. CRM-HR-WEB: trang Local components')
    local = get(f'files/{CRM}/nodes?ids={LOCAL_PAGE}')['nodes'][LOCAL_PAGE]['document']
    def collect_defs(n):
        # Không đi vào bên trong set/component: variant con thuộc về set.
        if n['type'] in ('COMPONENT_SET', 'COMPONENT'):
            yield n; return
        for c in n.get('children', []):
            yield from collect_defs(c)
    local_ids = {}
    for n in collect_defs(local):
        b = ((n.get('children') or [n])[0] if n['type'] == 'COMPONENT_SET' else n).get('absoluteBoundingBox') or {}
        local_ids[n['id']] = {'source': 'CRM-local', 'kind': 'set' if n['type'] == 'COMPONENT_SET' else 'component',
                              'name': n['name'], 'key': None, 'node': n['id'], 'page': '🔶 Local components',
                              'props': prop_summary(n.get('componentPropertyDefinitions')),
                              'size': [round(b.get('width', 0)), round(b.get('height', 0))],
                              'variants': len(n.get('children', [])) if n['type'] == 'COMPONENT_SET' else 1,
                              'status': status_of(n['name'], ''), 'desc': n.get('description', '')}

    pages = get(f'files/{CRM}?depth=1')['document']['children']
    pages = [p for p in pages if not any(s in p['name'] for s in SKIP_PAGES)]
    usage = collections.Counter()
    sample = {}
    observed = collections.defaultdict(lambda: collections.defaultdict(set))
    ext = {}
    for idx, p in enumerate(pages, 1):
        log(f'  [{idx}/{len(pages)}] {p["name"].strip()}')
        try:
            d = get(f'files/{CRM}/nodes?ids={p["id"]}')['nodes'][p['id']]
        except Exception as ex:
            log('    lỗi', ex); continue
        cmap, smap = d['components'], d['componentSets']
        def walk(n, in_inst=False):
            if n['type'] == 'INSTANCE' and not in_inst:
                c = cmap.get(n['componentId'], {})
                s = smap.get(c.get('componentSetId'), {})
                key = s.get('key') or c.get('key')
                # Cục bộ: map về node id định nghĩa (set hoặc component).
                if not c.get('remote'):
                    ident = c.get('componentSetId') or n['componentId']
                    if ident not in local_ids:  # định nghĩa nằm ngoài trang Local components
                        local_ids[ident] = {'source': 'CRM-local', 'kind': 'set' if s else 'component',
                                            'name': s.get('name') or c.get('name'), 'key': None, 'node': ident,
                                            'page': '(trang khác)', 'props': [], 'size': None, 'variants': None,
                                            'status': status_of(s.get('name') or c.get('name', ''), ''), 'desc': ''}
                else:
                    ident = key
                    if key not in entries and key not in ext:
                        is_icon = (s.get('name') or c.get('name', '')).startswith('ic_')
                        ext[key] = {'source': 'Icon' if is_icon else 'CRM-ext', 'kind': 'set' if s else 'component',
                                    'name': s.get('name') or c.get('name'), 'key': key, 'node': None, 'page': '',
                                    'props': [], 'size': None, 'variants': None, 'status': 'ok', 'desc': ''}
                usage[ident] += 1
                if ident not in sample:
                    b = n.get('absoluteBoundingBox') or {}
                    sample[ident] = {'instance': n['id'], 'page': p['name'].strip(), 'size': [round(b.get('width', 0)), round(b.get('height', 0))]}
                for k, v in (n.get('componentProperties') or {}).items():
                    observed[ident][f"{k.split('#')[0]}:{v['type']}"].add(str(v['value']) if v['type'] in ('VARIANT', 'BOOLEAN') else '')
            for ch in n.get('children', []):
                walk(ch, in_inst or n['type'] == 'INSTANCE')
        walk(d['document'])
        del d

    for ident, e in list(ext.items()) + [(i, e) for i, e in local_ids.items() if not e['props']]:
        e['props'] = sorted(f"{k.split(':')[0]}=" + '|'.join(sorted(v - {''})) if k.endswith('VARIANT') else f"{k.split(':')[0]}:{k.split(':')[1].lower()}"
                            for k, v in observed[ident].items())
        e['size'] = e.get('size') or sample.get(ident, {}).get('size')

    catalog = []
    for ident, e in list(entries.items()) + list(local_ids.items()) + list(ext.items()):
        e = dict(e)
        e['usage'] = usage.get(ident, 0)
        e['sample'] = sample.get(ident)
        catalog.append(e)
    json.dump({'generated': time.strftime('%Y-%m-%d'), 'components': catalog},
              open(os.path.join(OUT, 'catalog.json'), 'w'), ensure_ascii=False, indent=1)
    write_md(catalog)
    log('xong:', len(catalog), 'mục')


def write_md(catalog):
    by = collections.defaultdict(list)
    for e in catalog:
        by[e['source']].append(e)
    L = [f"# Danh mục component hợp lệ (sinh tự động {time.strftime('%d/%m/%Y')} bởi `scripts/build-catalog.py` — không sửa tay)", '',
         'Cột **Dùng** = số instance cấp ngoài trên các màn CRM-HR-WEB. **Trạng thái**: ok · cấm (có 🚧 — không dùng) · part (thành phần con, không dùng trực tiếp) · demo.',
         'Cách tạo instance theo nguồn: xem SKILL.md → "Nguồn component hợp lệ".', '']
    def size(e): return '×'.join(map(str, e['size'])) if e.get('size') else ''
    def sample(e): return f"`{e['sample']['instance']}` ({e['sample']['page']})" if e.get('sample') else ''
    def props(e): return ' · '.join(e.get('props') or [])[:220].replace('|', '\\|')
    L += ['## A. Thư viện Component (`m1uk68gT43hnMwKYOmv6vE`) — import theo key', '',
          '| Tên | Loại | Key | Trang | Prop / variant | Cỡ | Dùng | Trạng thái |', '|---|---|---|---|---|---|---|---|']
    for e in sorted(by['Component'], key=lambda e: (e['status'] != 'ok', e['page'], e['name'])):
        L.append(f"| {e['name']} | {e['kind']} | `{e['key']}` | {e['page']} | {props(e)} | {size(e)} | {e['usage']} | {e['status']} |")
    L += ['', '## B1. CRM-HR-WEB — component cục bộ (trang `🔶 Local components`) — dùng trong CRM-HR-WEB qua node id', '',
          '| Tên | Loại | Node id | Prop / variant | Cỡ | Dùng | Instance mẫu |', '|---|---|---|---|---|---|---|']
    for e in sorted(by['CRM-local'], key=lambda e: -e['usage']):
        L.append(f"| {e['name']} | {e['kind']} | `{e['node']}` | {props(e)} | {size(e)} | {e['usage']} | {sample(e)} |")
    L += ['', '## B2. CRM-HR-WEB — thư viện ngoài chưa publish — chỉ dùng trong CRM-HR-WEB qua instance mẫu', '',
          'Không import được theo key (REST 404/403). Lấy bằng `getMainComponentAsync()` từ instance mẫu rồi `createInstance()`. Prop = giá trị quan sát được trên các màn.', '',
          '| Tên | Key | Prop quan sát | Cỡ mẫu | Dùng | Instance mẫu |', '|---|---|---|---|---|---|']
    for e in sorted(by['CRM-ext'], key=lambda e: -e['usage']):
        L.append(f"| {e['name']} | `{e['key']}` | {props(e)} | {size(e)} | {e['usage']} | {sample(e)} |")
    if by['Icon']:
        L += ['', f"## Icon (thư viện Icon) — {len(by['Icon'])} icon đang dùng, tìm bằng `search_design_system` (lọc library key Icon)"]
    open(os.path.join(OUT, 'catalog.md'), 'w').write('\n'.join(L) + '\n')


if __name__ == '__main__':
    main()
