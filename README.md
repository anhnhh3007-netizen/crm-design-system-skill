# crm-design-system (Claude Code skill)

Skill cho Claude Code để dựng màn hình hoặc luồng màn hình CRM (CRM-HR-WEB) trong Figma bằng layout chung, component và token có sẵn của thư viện **Component**.

## Nội dung

| File | Mô tả |
|---|---|
| `SKILL.md` | Khi nào dùng skill và quy trình 6 bước: hiểu yêu cầu → tìm trước khi tạo → dựng layout chung → lắp nội dung → bind token, đặt tên → kiểm tra |
| `references/layout.md` | Layout chung (Menu, Top bar, tab navigation, Page header, main content), các pattern màn hình (List, Tree + List, Drawer form, Detail, luồng), instance tham chiếu và các lỗi đã gặp |
| `references/tokens.md` | Token màu, spacing, radius, typography, effect và key để import |
| `references/catalog.md` · `catalog.json` | Danh mục component hợp lệ (thư viện Component + CRM-HR-WEB): nguồn, key, prop, mức dùng, trạng thái (ok / cấm 🚧 / part / demo). Sinh tự động, không sửa tay |
| `references/component-gaps.md` | Ngoại lệ đã duyệt và component còn thiếu/lỗi, kèm cách đang xử lý tạm và đề xuất cho team design system |
| `scripts/audit-overrides.js` | Chạy trong `use_figma`: báo override vi phạm trên instance, component 🚧, kích thước lệch |
| `scripts/reset-overrides.js` | Chạy trong `use_figma`: xoá override không hợp lệ, giữ prop và nội dung chữ |
| `scripts/migrate-input-normal.js` | Chạy trong `use_figma`: chuyển `🚧 Input normal` sang `data entry` |
| `scripts/audit-overrides-rest.py` | Audit chỉ đọc qua REST API (cần `FIGMA_TOKEN`) |
| `scripts/build-catalog.py` | Dựng lại `catalog.md` / `catalog.json` từ 2 file Figma (cần `FIGMA_TOKEN`) |

## Cài đặt

Chép thư mục này vào `~/.claude/skills/crm-design-system/`:

```bash
git clone https://github.com/anhnhh3007-netizen/crm-design-system-skill ~/.claude/skills/crm-design-system
```

## Yêu cầu

- Figma MCP server (đã kết nối tài khoản có quyền vào file CRM-HR-WEB và thư viện Component).
- Skill `figma-use` và `figma-generate-design` của Figma.

## Cách dùng

Trong Claude Code, gọi `/crm-design-system` hoặc mô tả yêu cầu, ví dụ: "Tạo màn hình quản lý cửa hàng gồm danh sách và form thêm mới ở trang <link Figma>".
