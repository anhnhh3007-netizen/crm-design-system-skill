// Xoá override không hợp lệ — chạy trong use_figma sau khi audit-overrides.js báo vi phạm.
// Giữ: component property (của instance và instance lồng), nội dung chữ, cách FILL được phép.
// Xoá: mọi thứ khác (màu, kích thước, padding, style chữ, visible thủ công…).
// Thay IDS bằng danh sách id instance trong kết quả audit.

const IDS = ['REPLACE_ME'];

// Giữ đồng bộ với audit-overrides.js.
const STRETCH = {
  'Top bar': 'H', 'Top Bar': 'H', 'tab navigation': 'H', 'Page header': 'H',
  'Filter': 'H', 'Pagination': 'H',
  'table-header': 'H', 'Table / header': 'H', 'table-cell': 'H', 'Table / Cell': 'H',
  'Input / Text': 'H', 'Input': 'H', 'Select / Single Choice': 'H',
  '❖selectDate': 'H', 'Date range': 'H', '_inputLookup': 'H', 'Input (S)': 'H', 'Search': 'H',
  'tree navigation': 'H', 'data entry': 'H', 'Table-Cell': 'H',
  'Menu': 'V',
};

const setNameOf = (main) =>
  main.parent?.type === 'COMPONENT_SET' ? main.parent.name : main.name;

// Chỉ lấy prop ghi lại được; prop của instance lồng không có INSTANCE_SWAP để tránh lỗi setProperties.
const pickProps = (node, allowSwap) => {
  const out = {};
  for (const [k, p] of Object.entries(node.componentProperties || {})) {
    if (p.type === 'VARIANT' || p.type === 'BOOLEAN' || p.type === 'TEXT' || (allowSwap && p.type === 'INSTANCE_SWAP')) out[k] = p.value;
  }
  return out;
};

const done = [], skipped = [];

for (const id of IDS) {
  const inst = await figma.getNodeByIdAsync(id);
  if (inst?.type !== 'INSTANCE') { skipped.push({ id, reason: 'không phải instance' }); continue; }
  const main = await inst.getMainComponentAsync();
  const setName = setNameOf(main);
  if ((setName === 'table-cell' || setName === 'Table / Cell') && inst.componentProperties?.Type?.value === 'Slot') {
    skipped.push({ id, reason: 'ngoại lệ đã duyệt (cell Slot)' }); continue;
  }

  // Lưu trạng thái hợp lệ. Id node con trong instance (I<inst>;…) giữ nguyên sau reset.
  const rootProps = pickProps(inst, true);
  const nested = inst.findAll((n) => n.type === 'INSTANCE').map((n) => ({ id: n.id, props: pickProps(n, false) }));
  const texts = inst.findAll((n) => n.type === 'TEXT').map((n) => ({ id: n.id, chars: n.characters }));
  const sizing = { h: inst.layoutSizingHorizontal, v: inst.layoutSizingVertical };

  inst.resetOverrides();

  inst.setProperties(rootProps);
  for (const { id: nid, props } of nested) {
    const n = await figma.getNodeByIdAsync(nid);
    if (n?.type === 'INSTANCE' && Object.keys(props).length) {
      try { n.setProperties(props); } catch (e) { skipped.push({ id: nid, reason: `prop lồng: ${e.message}` }); }
    }
  }
  for (const { id: tid, chars } of texts) {
    const t = await figma.getNodeByIdAsync(tid);
    if (t?.type !== 'TEXT' || t.characters === chars) continue;
    for (const f of t.getRangeAllFontNames(0, t.characters.length)) await figma.loadFontAsync(f);
    t.characters = chars;
  }

  // Chỉ khôi phục FILL ở trục được phép; trục còn lại để theo main component.
  const axis = STRETCH[setName] || '';
  if (inst.parent?.layoutMode && inst.parent.layoutMode !== 'NONE') {
    if (axis.includes('H') && sizing.h === 'FILL') inst.layoutSizingHorizontal = 'FILL';
    if (axis.includes('V') && sizing.v === 'FILL') inst.layoutSizingVertical = 'FILL';
  }
  done.push({ id, name: inst.name, set: setName });
}

return { done, skipped };
