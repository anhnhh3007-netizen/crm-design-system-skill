// Audit override trên instance — chạy trong use_figma (bước 6 của SKILL.md).
// Thay ROOT_ID bằng id Section/frame vừa dựng. Kết quả `violations` phải rỗng
// (trừ ngoại lệ đã duyệt trong references/component-gaps.md).

const ROOT_ID = 'REPLACE_ME';

// Trục được phép FILL theo tên component set (giữ đồng bộ với SKILL.md + reset-overrides.js).
const STRETCH = {
  'Top bar': 'H', 'Top Bar': 'H', 'tab navigation': 'H', 'Page header': 'H',
  'Filter': 'H', 'Pagination': 'H',
  'table-header': 'H', 'Table / header': 'H', 'table-cell': 'H', 'Table / Cell': 'H',
  'Input / Text': 'H', 'Input': 'H', 'Select / Single Choice': 'H',
  '❖selectDate': 'H', 'Date range': 'H', '_inputLookup': 'H', 'Input (S)': 'H', 'Search': 'H',
  'tree navigation': 'H', 'data entry': 'H', 'Table-Cell': 'H',
  'Menu': 'V',
};

// Ngoại lệ đã duyệt: bỏ qua override bên trong (vẫn kiểm tra kích thước).
const isException = (setName, inst) =>
  (setName === 'table-cell' || setName === 'Table / Cell') &&
  inst.componentProperties?.Type?.value === 'Slot';

// Field override được phép trên chính instance gốc (vị trí trong auto layout cha).
const ROOT_OK = new Set([
  'componentProperties', 'name', 'x', 'y', 'constraints', 'layoutPositioning',
  'layoutGrow', 'layoutAlign', 'layoutSizingHorizontal', 'layoutSizingVertical',
  'primaryAxisSizingMode', 'counterAxisSizingMode',
  'width', 'height', // kích thước gốc được kiểm tra riêng ở dưới
]);

// Field Figma tự sinh khi chỉ sửa nội dung chữ (đã đo trên màn mẫu 962:134238: 102/102 text
// node có các field này nhưng không có style trộn). Chỉ là vi phạm nếu text bị trộn style.
const TEXT_EDIT_NOISE = new Set([
  'characterStyleOverrides', 'styleOverrideTable', 'styledTextSegments', 'lineIndentations', 'lineTypes',
]);
const hasMixedStyle = (t) =>
  t?.type === 'TEXT' && t.characters.length > 0 &&
  t.getStyledTextSegments(['textStyleId', 'fills', 'fontSize', 'fontName']).length > 1;

const setNameOf = (main) =>
  main.parent?.type === 'COMPONENT_SET' ? main.parent.name : main.name;

const root = await figma.getNodeByIdAsync(ROOT_ID);
if (!root) return { error: `Không tìm thấy ${ROOT_ID}` };

// Chỉ instance cấp ngoài cùng; override của instance lồng được báo qua instance cha.
const topInstances = root.findAll((n) => {
  if (n.type !== 'INSTANCE') return false;
  for (let p = n.parent; p && p !== root; p = p.parent) if (p.type === 'INSTANCE') return false;
  return true;
});

const violations = [];
const round = (v) => Math.round(v * 10) / 10;

for (const inst of topInstances) {
  const main = await inst.getMainComponentAsync();
  if (!main) { violations.push({ id: inst.id, name: inst.name, issue: 'mất main component' }); continue; }
  const setName = setNameOf(main);
  const axis = STRETCH[setName] || '';

  // 0) Mọi component 🚧 bị cấm ở cấp ngoài (🚧 lồng bên trong component hợp lệ, vd. data entry, thì không xét).
  if (setName.includes('🚧') || main.name.includes('🚧')) {
    violations.push({ id: inst.id, name: inst.name, set: setName, issue: 'component 🚧 bị cấm → xem thay thế trong SKILL.md (input: migrate-input-normal.js)' });
  }

  // 1) Kích thước: trục không được FILL phải bằng main component; trục được FILL thì chỉ FILL hoặc bằng gốc.
  //    HUG được bỏ qua: kích thước đổi do BOOLEAN prop ẩn/hiện phần con (vd. Filter Tab=false) là hợp lệ;
  //    override padding/gap làm HUG phình ra vẫn bị bắt ở bước 2.
  for (const [dim, ax, sizing] of [['width', 'H', 'layoutSizingHorizontal'], ['height', 'V', 'layoutSizingVertical']]) {
    if (round(inst[dim]) === round(main[dim])) continue;
    if (inst[sizing] === 'HUG') continue;
    if (axis.includes(ax) && inst[sizing] === 'FILL') continue;
    violations.push({ id: inst.id, name: inst.name, set: setName, issue: `${dim} ${round(inst[dim])} ≠ gốc ${round(main[dim])}` });
  }

  if (isException(setName, inst)) continue;

  // 2) Override bên trong.
  for (const o of inst.overrides) {
    const node = o.id === inst.id ? inst : await figma.getNodeByIdAsync(o.id);
    const refs = node?.componentPropertyReferences || {};
    const bad = o.overriddenFields.filter((f) => {
      if (o.id === inst.id) return !ROOT_OK.has(f);
      if (f === 'componentProperties') return false;           // variant/boolean của instance lồng
      if (f === 'characters') return false;                     // nội dung chữ
      if (TEXT_EDIT_NOISE.has(f)) return hasMixedStyle(node);  // nhiễu khi sửa chữ
      if (f === 'visible' && refs.visible) return false;        // qua BOOLEAN prop
      if (f === 'mainComponent' && refs.mainComponent) return false; // qua INSTANCE_SWAP prop
      // Text auto-resize đổi kích thước theo nội dung — không phải override style.
      if ((f === 'width' || f === 'height') && node?.type === 'TEXT' && node.textAutoResize !== 'NONE') return false;
      return true;
    });
    if (bad.length) violations.push({ id: inst.id, name: inst.name, set: setName, layer: node?.name ?? o.id, fields: bad });
  }
}

return { checked: topInstances.length, violations };
