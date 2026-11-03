# crm-design-system (Claude Code skill)

Skill cho Claude Code để dựng màn hình hoặc luồng màn hình CRM (CRM-HR-WEB) trong Figma bằng layout chung, component và token có sẵn của thư viện **Component**.

## Nội dung

| File | Mô tả |
|---|---|
| `SKILL.md` | Khi nào dùng skill và quy trình 6 bước: hiểu yêu cầu → tìm trước khi tạo → dựng layout chung → lắp nội dung → bind token, đặt tên → kiểm tra |
| `references/layout.md` | Layout chung (Menu, Top bar, tab navigation, Page header, main content), các pattern màn hình (List, Tree + List, Drawer form, Detail, luồng), instance tham chiếu và các lỗi đã gặp |
| `references/tokens.md` | Token màu, spacing, radius, typography, effect và key để import |

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
