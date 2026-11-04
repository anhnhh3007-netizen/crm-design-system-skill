// Chuyển instance `🚧 Input normal` (cấp ngoài) sang `data entry` — chạy trong use_figma, trong file CRM-HR-WEB.
// Mặc định DRY_RUN=true: chỉ báo cáo. Kiểm tra báo cáo rồi chạy lại với DRY_RUN=false.
// Ánh xạ: xem SKILL.md → "Chuyển 🚧 Input normal có sẵn sang data entry".

const ROOT_ID = 'REPLACE_ME';          // Section/frame cần chuyển
const DRY_RUN = true;
const REQUIRED = false;                // data entry mặc định Required=true — true/false cho mọi trường, hoặc mảng tiêu đề trường bắt buộc
const SUB_TYPE = {};                   // tiêu đề → `-> sub type` (mặc định 'default'), vd. { 'Store manager': 'look-up' }
const DATA_ENTRY_SET = '1068:91679';   // set `data entry` (CRM-HR-WEB, nguồn B1)

const STATE = { Default: 'default', Filled: 'filled', Focused: 'focus', Disabled: 'disable', Error: 'error', 'Read-only': 'read-only' };
const CONTROL_H = 36;                  // chiều cao control bên trong data entry

const propKey = (node, name) => Object.keys(node.componentProperties || {}).find((k) => k.split('#')[0] === name);
const propVal = (node, name) => { const k = propKey(node, name); return k ? node.componentProperties[k].value : undefined; };
const findInst = (root, name) => root.findOne((n) => n.type === 'INSTANCE' && n.name === name);
const setText = async (t, chars) => {
  if (!t || chars == null || t.characters === chars) return;
  for (const f of t.getRangeAllFontNames(0, t.characters.length)) await figma.loadFontAsync(f);
  t.characters = chars;
};

const root = await figma.getNodeByIdAsync(ROOT_ID);
const set = await figma.getNodeByIdAsync(DATA_ENTRY_SET);
if (!root || set?.type !== 'COMPONENT_SET') return { error: 'Không tìm thấy ROOT_ID hoặc set data entry (phải chạy trong CRM-HR-WEB)' };

const targets = [];
for (const n of root.findAll((n) => n.type === 'INSTANCE')) {
  let nested = false;
  for (let p = n.parent; p && p !== root; p = p.parent) if (p.type === 'INSTANCE') { nested = true; break; }
  if (nested) continue;
  const main = await n.getMainComponentAsync();
  const setName = main?.parent?.type === 'COMPONENT_SET' ? main.parent.name : main?.name;
  if (setName === '🚧 Input normal') targets.push(n);
}

const report = [];
for (const old of targets) {
  const state = STATE[propVal(old, 'state')] || 'default';
  const showTitle = String(propVal(old, 'iShowTitle')) !== 'False';
  const titleBox = findInst(old, '❖title');
  const titleText = titleBox?.findOne((t) => t.type === 'TEXT' && t.visible && !t.parent?.name?.includes('Sub'))?.characters;
  const labelText = old.findOne((t) => t.type === 'TEXT' && t.name === 'Label')?.characters;
  const captionOn = String(propVal(old, 'isShowCaption')) === 'True';
  const captionText = old.findOne((t) => t.type === 'TEXT' && t.name === 'supporting-text')?.characters;
  const leadingOn = String(propVal(old, 'isShowLeadingIcon')) === 'True';

  const notes = [];
  if (!showTitle) notes.push('iShowTitle=False: data entry luôn có tiêu đề — cần quyết định');
  // data entry dùng `🚧 Input normal size=S` (control cao 36) cho mọi variant.
  if (propVal(old, 'size') && propVal(old, 'size') !== 'S') notes.push(`size=${propVal(old, 'size')} → data entry chỉ có size S (control ${CONTROL_H})`);

  const subType = SUB_TYPE[titleText] || 'default';
  const required = Array.isArray(REQUIRED) ? REQUIRED.includes(titleText) : REQUIRED;
  const item = { id: old.id, parent: old.parent?.name, title: titleText, label: labelText, state, subType, required, notes };
  report.push(item);
  if (DRY_RUN) continue;

  const variant = set.children.find((c) => c.name === `Type=Input, -> sub type=${subType}, State=${state}`);
  if (!variant) { item.notes.push(`không có variant sub type=${subType}, State=${state}`); continue; }
  const inst = variant.createInstance();
  const parent = old.parent;
  parent.insertChild(parent.children.indexOf(old), inst);
  if (parent.layoutMode && parent.layoutMode !== 'NONE') {
    if (old.layoutSizingHorizontal === 'FILL') inst.layoutSizingHorizontal = 'FILL';
    if (old.layoutPositioning === 'ABSOLUTE') { inst.layoutPositioning = 'ABSOLUTE'; inst.x = old.x; inst.y = old.y; }
  } else { inst.x = old.x; inst.y = old.y; }

  inst.setProperties({ [propKey(inst, 'Required')]: required, [propKey(inst, 'infor')]: false });
  const disp = findInst(inst, '[Display] Title');
  if (disp && titleText != null && propKey(disp, 'Title')) disp.setProperties({ [propKey(disp, 'Title')]: titleText });
  const sel = findInst(inst, '❖inputSelection');
  if (sel) {
    const p = {};
    if (labelText != null && propKey(sel, 'Label')) p[propKey(sel, 'Label')] = labelText;
    if (propKey(sel, 'isShowCaption')) p[propKey(sel, 'isShowCaption')] = captionOn;
    if (propKey(sel, 'isShowLeadingIcon')) p[propKey(sel, 'isShowLeadingIcon')] = leadingOn;
    if (Object.keys(p).length) sel.setProperties(p);
    if (captionOn) await setText(sel.findOne((t) => t.type === 'TEXT' && t.name === 'supporting-text'), captionText);
  }
  inst.name = old.name === '🚧 Input normal' ? 'data entry' : old.name;
  old.remove();
  item.newId = inst.id;
}

return { dryRun: DRY_RUN, found: targets.length, report };
