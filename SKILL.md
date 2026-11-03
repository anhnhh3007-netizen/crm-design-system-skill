---
name: crm-design-system
description: Dựng màn hình hoặc luồng màn hình CRM (CRM-HR-WEB, MB Bank) trong Figma bằng layout chung, component và token có sẵn của thư viện "Component". Dùng khi người dùng muốn tạo màn hình/luồng CRM mới trong Figma ("tạo màn hình quản lý…", "vẽ luồng thêm mới/sửa/chi tiết…", "build a CRM screen in Figma"), khi cần chuyển giá trị raw (hex, px) sang variable đã bind, hoặc khi cần một màn hình phải dùng component thư viện thay vì vẽ tay.
user-invocable: true
---

# CRM design system — dựng màn hình/luồng trong Figma

## Nguồn

| Nguồn | File key | Ghi chú |
|---|---|---|
| Design system (thư viện **Component**) | `m1uk68gT43hnMwKYOmv6vE` | Đã add vào CRM-HR-WEB. Library key: `lk-132a16a9596327435c24eed300bd2d1ee92d1d6748578e0e43ce7dbea6c3397a1312200e5dd23e188fa2a3a3dc0205394091659833b210fc4493d994546aa205` |
| Thư viện **Icon** | — | Library key: `lk-77899ab003d5a7c80257d8056c2119d5765dce7113c8d757ed95fc197e625653eb711111fd330bf237c0f8fd55f8b3c2090ccb113578bb0e4c959894df713d34`. Icon tên `ic_*` |
| Thiết kế có sẵn **CRM-HR-WEB** | `GztI8Yyl0PJ1GE0pptPi48` | Màn hình tham chiếu + component cục bộ (trang `🔶 Local components`, id `962:148876`) |

Link: https://www.figma.com/design/m1uk68gT43hnMwKYOmv6vE/Component · https://www.figma.com/design/GztI8Yyl0PJ1GE0pptPi48/CRM-HR-WEB

Khi tìm component bằng `search_design_system`, **luôn truyền `includeLibraryKeys`** với key của Component và Icon. Không giới hạn thì kết quả lẫn các thư viện khác (Component (Copy), M-Office, IAS…) và rất dễ import nhầm.

## Bắt buộc trước khi gọi tool

1. Load skill `figma-use` (bắt buộc trước mọi `use_figma`), và `figma-generate-design` khi dựng cả màn hình.
2. `create_session` với file key đích (thường là CRM-HR-WEB), dùng lại `sessionId` cho mọi call.
3. Đọc [references/layout.md](references/layout.md) (layout chung + các pattern màn hình) và [references/tokens.md](references/tokens.md) (token để bind).

## Quy trình

### 1. Hiểu yêu cầu
- Xác định **loại màn hình** theo pattern ở `references/layout.md`: Danh sách (List), Danh sách + cây (Tree + List), Thêm mới/Sửa (Drawer form), Chi tiết (Drawer/Page detail), Dashboard/Home.
- Xác định **module** trên Menu (Workbench, Customer, Business, Marketing, Product, Basic, Public) và breadcrumb (`<Module> / <Nhóm chức năng>`).
- Với **luồng**: liệt kê các bước (ví dụ: List → Drawer thêm mới → Toast thành công → List cập nhật). Mỗi bước là một frame 1440×822 riêng.
- Nếu chưa rõ module, loại màn hình, hoặc các trường dữ liệu → hỏi người dùng trước khi dựng.

### 2. Tìm trước khi tạo
Theo thứ tự ưu tiên:
1. **Màn hình tương tự trong CRM-HR-WEB** — tìm trang trong cùng module (danh sách trang: `get_metadata` không truyền nodeId). Nếu có màn hình cùng pattern, đọc cấu trúc của nó và tái dùng cách sắp xếp.
2. **Component cục bộ CRM-HR-WEB** (Top bar, Tab navigation, Page header, Menu, tree navigation, Filter, Bottom action, Activity Tag, _badge, _chipItem, _illus cho empty state…).
3. **Thư viện Component** qua `search_design_system` (chỉ lọc 2 library key ở trên).
4. Chỉ khi cả 3 không có mới tạo phần tử mới — và phải dựng từ các component/token sẵn có, đặt tên theo quy ước (mục 5).

Cách lấy component của layout chung nhanh và chắc nhất: trong `use_figma`, đọc instance trên màn hình tham chiếu (`getNodeByIdAsync` → `getMainComponentAsync()`) rồi `createInstance()` từ main component đó. Không detach.

### 3. Dựng layout chung (shell) trước
Dựng đúng khung trong `references/layout.md` → mục "Layout chung" (có bảng instance tham chiếu và danh sách lỗi đã gặp — đọc kỹ trước khi viết script), từng phần một và kiểm tra sau mỗi phần (screenshot). Màn mới đặt trong một Section trên trang người dùng chỉ định, cách xa nội dung có sẵn:
`Menu (80)` + `body (1360)` → `Top bar (48)` → `tab navigation (42)` → vùng nội dung (padding ngang 24, nền `surface/neutral/lighter-1`) → `Page header` → `main content`.

### 4. Lắp nội dung theo pattern
- Dùng instance + variant + component property; chỉnh text qua property hoặc text node bên trong instance, không vẽ lại.
- Bảng: ghép cột `col` = `table-header` + `data` (các `table-cell`), cột hành động cuối dùng `Icon Button / Ghost` (sửa, xem). Phía dưới là `Pagination`.
- Form: `Drawer` 459px bên phải + `overlay`; trường dùng `🚧 Input normal`, `Select / Single Choice`, `❖selectDate`/`Date range`; hành động cuối drawer là `Standard Button / Secondary` (Huỷ) + `Standard Button / Primary` (Lưu/Cập nhật).
- Trạng thái rỗng dùng `_illus` (type=empty/search/404/no task…).

### 5. Token và quy ước đặt tên
- **Mọi** fill, stroke, radius, gap, padding, typography, effect phải bind vào variable/style (xem `references/tokens.md`). Không để hex/px raw. Nếu gặp giá trị raw trên layer cũ → tìm token khớp giá trị và bind lại.
- Ưu tiên token **comp/** (đúng component) → **semantic** (`text/…`, `surface/…`, `border/…`, `icon/…`) → mới đến **primitive** (`primary/550`, `neutral/20`). Không dùng primitive khi đã có semantic tương đương.
- Đặt tên layer theo file mẫu: khung màn hình đặt theo trạng thái (`Management`, `Create`, `Edit`, `Detail`); khung con dùng tên thường mô tả vai trò (`body`, `main content`, `header`, `title`, `form`, `action`, `table`, `col`, `data`, `overlay`). Không để tên mặc định `Frame 1321…` cho layer mới.
- Section chứa luồng đặt tên theo chức năng (vd. `Organization Management`), các frame xếp trái → phải theo thứ tự bước, cách nhau ~89px.

### 6. Kiểm tra trước khi bàn giao
- Screenshot từng frame, so với màn hình tham chiếu cùng pattern: kích thước shell, khoảng cách, màu.
- Rà toàn bộ node mới bằng script: duyệt mọi node **không nằm trong instance**, báo fill/stroke SOLID chưa bind, padding/gap/radius > 0 chưa bind, TEXT không có `textStyleId`, tên `Frame \d+`. Phần clone từ màn mẫu cũng phải rà (màn mẫu còn giá trị raw). Giá trị lệch lưới (15, 10) đổi về token gần nhất.
- Không có instance bị detach.
- Báo lại cho người dùng: link frame/section, các component đã dùng, phần nào phải tạo mới (và vì sao không có trong thư viện).

## Ví dụ

**Input:** "Tạo màn hình quản lý cửa hàng gồm danh sách, nút thêm mới và form thêm mới."

**Output:** Section `Store Management` với 2 frame 1440×822:
- `Management`: shell chung (Menu module Product active, Top bar, tab navigation có tab "Store management" active, Page header breadcrumb `Product management / Store management` + nút `Standard Button / Primary` "Add new"), `Filter` + bảng ghép từ `Table / header`/`Table / Cell` + `Pagination`.
- `Create`: cùng shell, phủ `overlay` (`color/global/black-alpha/8`) và `Drawer` 459px, form 2 cột dùng `🚧 Input normal` / `Select / Single Choice`, chân drawer `Cancel` (Secondary) + `Save` (Primary).
Mọi màu bind token `comp/*` hoặc semantic, chữ dùng text style `body/size-m/regular`, `title/size-s/semibold`…, layer đặt tên theo quy ước.
