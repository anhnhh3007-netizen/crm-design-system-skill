#!/usr/bin/env python3
"""Audit override chỉ đọc qua Figma REST API — dùng khi không có tool use_figma.

Cùng quy tắc với audit-overrides.js, nhưng không reset được và không xét được style trộn
trong text ở mức Plugin API (dùng styleOverrideTable thay thế).

    FIGMA_TOKEN=figd_... python3 audit-overrides-rest.py <file_key> <node_id> [--json]

Token lấy từ biến môi trường, không ghi vào file.
"""
import collections, json, os, sys, urllib.request

LIB_FILE = 'm1uk68gT43hnMwKYOmv6vE'  # thư viện Component

# Giữ đồng bộ với audit-overrides.js.
STRETCH = {
    'Top bar': 'H', 'Top Bar': 'H', 'tab navigation': 'H', 'Page header': 'H', 'Filter': 'H', 'Pagination': 'H',
    'table-header': 'H', 'Table / header': 'H', 'table-cell': 'H', 'Table / Cell': 'H',
    'Input / Text': 'H', 'Input': 'H', 'Select / Single Choice': 'H', '❖selectDate': 'H', 'Date range': 'H',
    '_inputLookup': 'H', 'Input (S)': 'H', 'Search': 'H', 'tree navigation': 'H', 'data entry': 'H', 'Table-Cell': 'H', 'Menu': 'V',
}
ROOT_OK = {'componentProperties', 'name', 'x', 'y', 'constraints', 'layoutPositioning', 'layoutGrow', 'layoutAlign',
           'layoutSizingHorizontal', 'layoutSizingVertical', 'primaryAxisSizingMode', 'counterAxisSizingMode',
           'width', 'height'}
TEXT_EDIT_NOISE = {'characterStyleOverrides', 'styleOverrideTable', 'styledTextSegments', 'lineIndentations', 'lineTypes'}


def get(path):
    req = urllib.request.Request('https://api.figma.com/v1/' + path, headers={'X-Figma-Token': os.environ['FIGMA_TOKEN']})
    return json.load(urllib.request.urlopen(req, timeout=180))


def main():
    file_key, node_id = sys.argv[1], sys.argv[2]
    data = get(f'files/{file_key}/nodes?ids={node_id}')['nodes'][node_id]
    comps, sets = data['components'], data['componentSets']

    byid, tops = {}, []
    def walk(n, in_inst=False):
        byid[n['id']] = n
        if n['type'] == 'INSTANCE' and not in_inst:
            tops.append(n)
        for c in n.get('children', []):
            walk(c, in_inst or n['type'] == 'INSTANCE')
    walk(data['document'])

    def set_of(cid):
        c = comps[cid]
        s = sets.get(c.get('componentSetId'), {})
        return s.get('name') or c['name'], s.get('key')

    # Nguồn của từng component: cục bộ / thư viện Component / thư viện khác (không publish hoặc không truy cập được).
    lib_sets = {s['key'] for s in get(f'files/{LIB_FILE}/component_sets')['meta']['component_sets']}
    lib_comps = {c['key']: c['node_id'] for c in get(f'files/{LIB_FILE}/components')['meta']['components']}
    # Whitelist từ catalog.json (build-catalog.py): key của nguồn A/B2/Icon.
    cat_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'references', 'catalog.json')
    allowed = {e['key']: e['source'] for e in json.load(open(cat_path))['components'] if e.get('key')} if os.path.exists(cat_path) else {}
    def source(cid):
        c = comps[cid]
        if not c.get('remote'):
            return 'local'
        if set_of(cid)[1] in lib_sets or c['key'] in lib_comps:
            return 'Component'
        k = set_of(cid)[1] or c['key']
        return allowed.get(k, 'NGOÀI CATALOG')

    # Kích thước main component (cục bộ + thư viện Component).
    used = {i['componentId'] for i in tops}
    sizes = {}
    local = [c for c in used if source(c) == 'local']
    if local:
        for k, v in get(f'files/{file_key}/nodes?depth=1&ids=' + ','.join(local))['nodes'].items():
            if v:
                b = v['document']['absoluteBoundingBox']; sizes[k] = (b['width'], b['height'])
    lib = {c: lib_comps[comps[c]['key']] for c in used if comps[c]['key'] in lib_comps}
    if lib:
        r = get(f'files/{LIB_FILE}/nodes?depth=1&ids=' + ','.join(set(lib.values())))['nodes']
        for c, nid in lib.items():
            if r.get(nid):
                b = r[nid]['document']['absoluteBoundingBox']; sizes[c] = (b['width'], b['height'])

    violations = []
    for inst in tops:
        name, _ = set_of(inst['componentId'])
        axis = STRETCH.get(name, '')
        ms = sizes.get(inst['componentId'])
        if ms:
            b = inst['absoluteBoundingBox']
            for dim, ax, key, i in (('width', 'H', 'layoutSizingHorizontal', 0), ('height', 'V', 'layoutSizingVertical', 1)):
                if round(b[dim], 1) == round(ms[i], 1) or inst.get(key) == 'HUG':
                    continue
                if ax in axis and inst.get(key) == 'FILL':
                    continue
                violations.append({'set': name, 'id': inst['id'], 'layer': inst['name'],
                                   'fields': [f'{dim} {round(b[dim], 1)} ≠ gốc {round(ms[i], 1)}']})
        if name in ('table-cell', 'Table / Cell') and inst.get('componentProperties', {}).get('Type', {}).get('value') == 'Slot':
            continue  # ngoại lệ đã duyệt
        for o in inst.get('overrides', []):
            node = byid.get(o['id'], {})
            refs = node.get('componentPropertyReferences') or {}
            bad = []
            for f in o['overriddenFields']:
                if o['id'] == inst['id']:
                    if f not in ROOT_OK: bad.append(f)
                elif f in ('componentProperties', 'characters'):
                    pass
                elif f in TEXT_EDIT_NOISE:
                    if node.get('styleOverrideTable'): bad.append(f)
                elif f == 'visible' and 'visible' in refs:
                    pass
                elif f == 'mainComponent' and 'mainComponent' in refs:
                    pass
                elif f in ('width', 'height') and node.get('type') == 'TEXT' and node.get('style', {}).get('textAutoResize', 'NONE') != 'NONE':
                    pass
                else:
                    bad.append(f)
            if bad:
                violations.append({'set': name, 'id': inst['id'], 'layer': node.get('name') or o['id'], 'fields': bad})

    for i in tops:
        n = set_of(i['componentId'])[0]
        if '🚧' in n or '🚧' in comps[i['componentId']]['name']:
            violations.append({'set': n, 'id': i['id'], 'layer': i['name'], 'fields': ['component 🚧 bị cấm']})
        if source(i['componentId']) == 'NGOÀI CATALOG':
            violations.append({'set': set_of(i['componentId'])[0], 'id': i['id'], 'layer': i['name'], 'fields': ['component ngoài catalog']})
    src = collections.Counter((set_of(i['componentId'])[0], source(i['componentId'])) for i in tops)
    out = {'instances': len(tops), 'sources': [{'set': s, 'source': k, 'count': n} for (s, k), n in src.items()],
           'no_size_check': sorted({set_of(c)[0] for c in used if c not in sizes}), 'violations': violations}
    if '--json' in sys.argv:
        print(json.dumps(out, ensure_ascii=False, indent=1)); return
    print(f"Instance cấp ngoài: {out['instances']}")
    print('Nguồn component:')
    for r in out['sources']:
        print(f"  {r['count']:3}× {r['set']:<26} {r['source']}")
    if out['no_size_check']:
        print('Không kiểm tra được kích thước (không đọc được main):', ', '.join(out['no_size_check']))
    grouped = collections.Counter((v['set'], v['layer'], tuple(v['fields'])) for v in violations)
    print(f'Vi phạm: {len(violations)}')
    for (s, layer, fields), n in grouped.most_common():
        print(f"  {n:3}× {s} › {layer}: {', '.join(fields)}")


if __name__ == '__main__':
    main()
