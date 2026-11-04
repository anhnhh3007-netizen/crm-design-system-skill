---
name: crm-design-system
description: Dựng màn hình hoặc luồng màn hình CRM (CRM-HR-WEB, MB Bank) trong Figma bằng layout chung, component và token có sẵn của thư viện "Component" và của file CRM-HR-WEB (danh mục hợp lệ trong references/catalog.md). Dùng khi người dùng muốn tạo màn hình/luồng CRM mới trong Figma ("tạo màn hình quản lý…", "vẽ luồng thêm mới/sửa/chi tiết…", "build a CRM screen in Figma"), khi cần chuyển giá trị raw (hex, px) sang variable đã bind, hoặc khi cần một màn hình phải dùng component thư viện thay vì vẽ tay.
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

## Nguồn component hợp lệ

Chỉ dùng component có trong [references/catalog.md](references/catalog.md) (sinh tự động từ 2 file bởi `scripts/build-catalog.py`). Tra catalog **trước** `search_design_system`. Component ngoài catalog = không hợp lệ.

| Nguồn trong catalog | Là gì | Cách tạo instance | Dùng được ở |
|---|---|---|---|
| **A. Component** | Component publish của thư viện Component | `importComponentSetByKeyAsync(key)` / `importComponentByKeyAsync(key)` → chọn variant → `createInstance()` | Mọi file đã add thư viện |
| **B1. CRM-local** | Component định nghĩa trong CRM-HR-WEB | `getNodeByIdAsync(node)` → (set: chọn variant con) → `createInstance()` | Chỉ CRM-HR-WEB |
| **B2. CRM-ext** | Component từ thư viện ngoài chưa publish, đang dùng trên màn CRM (vd. `table-cell`, `table-header`, `tab navigation`) | `getNodeByIdAsync(<instance mẫu>)` → `getMainComponentAsync()` → `createInstance()` → `setProperties` | Chỉ CRM-HR-WEB |

**Chọn giữa các nguồn khi có nhiều ứng viên:**
1. Theo pattern màn CRM đang dùng: component có cột **Dùng** cao trên các màn CRM cùng loại → ưu tiên (giữ nhất quán với màn hiện có).
2. Nhu cầu không có ở component CRM → lấy từ thư viện Component (vd. ô bảng kiểu tiền, tag, account, switch).
3. **Cấm** dùng bất kỳ component nào có ký hiệu 🚧 (trong tên hoặc trang chứa nó; trạng thái `cấm` trong catalog) — gồm `🚧 Input normal`, `🚧 Input password`, `🚧 Input dropdown`, `🚧 Timeline`, `🚧 Step`, `🚧 Milestone`, `🚧 Badge highligt`. Thay thế: trường nhập liệu → `data entry`; bước/timeline → `step` / `item_step` (CRM-local) hoặc `step` (thư viện); badge → `Badge`. Không có thay thế → hỏi người dùng, ghi `component-gaps.md`. Không dùng `part` / `demo` trực tiếp. (🚧 nằm **bên trong** một component hợp lệ, như `🚧 Input normal` trong `data entry`, là cấu tạo của component đó — không tính là dùng.)
4. Không tìm thấy trong catalog → hỏi người dùng, ghi vào `component-gaps.md`; không lấy từ thư viện khác.

**Trường nhập liệu trong form** — dùng `data entry` (B1, set `1068:91679`, 2117 lần dùng trên màn CRM; mỗi instance = nhãn + control, 58px). Chọn bằng variant, không dùng component input rời:

| Nhu cầu | `Type` | `-> sub type` |
|---|---|---|
| Text 1 dòng | `Input` | `default` |
| Số tiền | `Input` | `currency` |
| Tra cứu đối tượng (nhân viên, KH, đơn vị) | `Input` | `look-up` |
| Chọn 1 / nhiều | `Select` | `single` / `multi` |
| Ngày · khoảng ngày | `Single date` · `Date` | `default` · `date range` |
| Giờ · khoảng giờ | `Time` · `Time range` | `default` · `time range` |
| Ô tìm kiếm trong form | `Search` | `default` |
| Text nhiều dòng | `Text Area` | `default` |

`State`: Create → `default`, Edit → `filled`, chỉ đọc → `read-only`, màn Detail → `view`, lỗi validate → `error`.
Prop mặc định của set đang **bật** `Required` và `infor` → luôn đặt rõ: `Required` theo trường (bắt buộc mới `true`), `infor=false` trừ khi cần icon ⓘ.
Nhãn: TEXT prop `Title` trên instance lồng `[Display] Title`. Placeholder/giá trị: TEXT prop `Label` trên instance lồng `❖inputSelection`. Caption: BOOLEAN `isShowCaption` trên `❖inputSelection` + nội dung `supporting-text`. Đều là đặt prop/nội dung chữ trên instance lồng → hợp lệ.
`data entry` không có loại cần → dùng input thư viện không có 🚧 (`Input / Text`, `Select / Single Choice`, `Single date`, `Date range`…) và ghi vào `component-gaps.md`. Không bao giờ dùng component 🚧.

**Chuyển `🚧 Input normal` có sẵn sang `data entry`:** chạy [scripts/migrate-input-normal.js](scripts/migrate-input-normal.js) (mặc định chỉ báo cáo; `DRY_RUN=false` mới thay). Ánh xạ:

| `🚧 Input normal` | `data entry` |
|---|---|
| — | `Type=Input`, `-> sub type=default` |
| `state=Default\|Filled\|Focused\|Disabled\|Error\|Read-only` | `State=default\|filled\|focus\|disable\|error\|read-only` |
| text tiêu đề (`❖title`) | `Title` của `[Display] Title` |
| `Label` (placeholder/giá trị) | `Label` của `❖inputSelection` |
| `isShowCaption` + `supporting-text` | giữ nguyên trên `❖inputSelection` |
| `isShowLeadingIcon` | giữ nguyên trên `❖inputSelection` |
| `iShowTitle=False` | không có tương đương (data entry luôn có tiêu đề) → script báo, không tự xử lý |
| `size` ≠ chiều cao control của data entry (36) | script báo; data entry giữ kích thước gốc |

**Bảng** — header + ô cùng họ CRM (cao 44 / 50):

| Cột | Component | Nguồn |
|---|---|---|
| Header mọi cột | `table-header` — bật/tắt `Show Checkbox`, `Show filter`, `Show Text` | B2 |
| Ô | `table-cell` `Type=No\|Text\|Name\|Checkbox\|Radio\|Toggle\|Chips\|tag\|Dropdown\|Input\|Photo\|Yes`; hành động = `Type=Slot` (ngoại lệ clone) | B2 (45 729 lần dùng) |
| Ô tiền, số, ngày, text link | `Table-Cell` `type=currency\|number\|date\|text link` | B2 |
| Ô account (avatar + tên), ảnh, file, nút, icon | `Table / Cell` `type=account\|img\|file\|button\|icon`, `state=default` | A |
| Ô trạng thái (tag màu) | `Table / Cell` `type=tag, state=default` → `Tag / normal` lồng: đặt `Color`, sửa chữ `Label`. **Không** dùng `table-cell` `Type=tag` (lỗi độ rộng, xem `component-gaps.md`) | A |

Không trộn `Table / header` (thư viện) với `table-header` trong cùng bảng. Ô `account` cao 56, `button` 52, `img` 80 → cả hàng theo chiều cao lớn nhất; không resize ô.

Dựng màn ở file khác CRM-HR-WEB → chỉ còn nguồn A; báo người dùng phần nào thiếu.

## Bắt buộc trước khi gọi tool

1. Load skill `figma-use` (bắt buộc trước mọi `use_figma`), và `figma-generate-design` khi dựng cả màn hình.
2. `create_session` với file key đích (thường là CRM-HR-WEB), dùng lại `sessionId` cho mọi call.
3. Đọc [references/layout.md](references/layout.md) (layout chung + các pattern màn hình), [references/tokens.md](references/tokens.md) (token để bind) và [references/component-gaps.md](references/component-gaps.md) (ngoại lệ đã duyệt + component còn thiếu).

## Nguyên tắc không override (bắt buộc)

Component dùng **đúng như thiết kế gốc**: không đổi kích thước, màu, chữ, khoảng cách. Chỉ được chỉnh qua component property.

| Được phép | Không được phép |
|---|---|
| Đổi `VARIANT` bằng `setProperties` (cả trên instance lồng bên trong, vd. `_menu active=yes`) | Sửa fill, stroke, effect, opacity, radius của layer bên trong instance |
| Bật/tắt `BOOLEAN` prop | `resize()` instance; sửa padding, gap, layout bên trong instance |
| Điền `TEXT` prop, hoặc sửa nội dung (`characters`) của text node trong instance | Sửa font, cỡ chữ, màu chữ, `textStyleId` của text trong instance |
| `INSTANCE_SWAP` trong preferred values (đổi icon) | Đặt `visible` cho layer con không gắn BOOLEAN prop |
| Đặt instance vào auto layout của frame cha; **FILL theo trục được phép** (bảng dưới) | Detach; `clone()` instance có sẵn trên màn mẫu |

**Kích thước:** instance giữ nguyên kích thước main component, trừ trục được phép **FILL** dưới đây (chỉ FILL, không đặt width/height FIXED tuỳ ý):

| Component | Trục được FILL |
|---|---|
| Top bar, tab navigation, Page header, Filter, Pagination | ngang |
| `table-header`, `table-cell` (trong frame `col`; độ rộng cột đặt trên frame `col`) | ngang |
| `Input / Text`, `Input`, `Input (S)`, `Search`, `Select / Single Choice`, `❖selectDate`, `Date range`, `_inputLookup` | ngang |
| `tree navigation`, `data entry`, `Table-Cell` | ngang |
| Menu | dọc |

Component khác: giữ nguyên kích thước. Chiều còn lại luôn giữ nguyên (vd. input luôn cao đúng theo variant `Size`).

**Cách tạo instance:** luôn lấy main component (`importComponentSetByKeyAsync` / `importComponentByKeyAsync`, hoặc `getMainComponentAsync()` từ instance tham chiếu) rồi `createInstance()`. Màn mẫu có thể chứa override → **không clone instance từ màn mẫu**. Clone frame do chính mình vừa dựng sạch (vd. List → Create) thì được.

**Khi component không đáp ứng:** không tự chỉnh để lách. Ghi vào `references/component-gaps.md` (component, thiếu gì, đang dùng tạm cái gì) và báo người dùng để gửi team design system. Ngoại lệ chỉ hợp lệ khi đã có trong mục "Ngoại lệ đã duyệt" của file đó.

**Token chỉ áp cho layer không nằm trong instance** (frame layout như `body`, `content`, `main content`, `row`, `col`, Drawer container). Không bind token đè lên layer bên trong instance.

## Quy trình

### 1. Hiểu yêu cầu
- Xác định **loại màn hình** theo pattern ở `references/layout.md`: Danh sách (List), Danh sách + cây (Tree + List), Thêm mới/Sửa (Drawer form), Chi tiết (Drawer/Page detail), Dashboard/Home.
- Xác định **module** trên Menu (Workbench, Customer, Business, Marketing, Product, Basic, Public) và breadcrumb (`<Module> / <Nhóm chức năng>`).
- Với **luồng**: liệt kê các bước (ví dụ: List → Drawer thêm mới → Toast thành công → List cập nhật). Mỗi bước là một frame 1440×822 riêng.
- Nếu chưa rõ module, loại màn hình, hoặc các trường dữ liệu → hỏi người dùng trước khi dựng.

### 2. Tìm trước khi tạo
Theo thứ tự ưu tiên:
0. **Tra [references/catalog.md](references/catalog.md)** để biết component hợp lệ, nguồn, prop, instance mẫu.
1. **Màn hình tương tự trong CRM-HR-WEB** — tìm trang trong cùng module (danh sách trang: `get_metadata` không truyền nodeId). Nếu có màn hình cùng pattern, đọc cấu trúc của nó và tái dùng cách sắp xếp.
2. **Component cục bộ CRM-HR-WEB** (Top bar, Tab navigation, Page header, Menu, tree navigation, Filter, Bottom action, Activity Tag, _badge, _chipItem, _illus cho empty state…).
3. **Thư viện Component** qua `search_design_system` (chỉ lọc 2 library key ở trên).
4. Chỉ khi cả 3 không có mới tạo phần tử mới — và phải dựng từ các component/token sẵn có, đặt tên theo quy ước (mục 5).

Cách lấy component của layout chung nhanh và chắc nhất: trong `use_figma`, đọc instance trên màn hình tham chiếu (`getNodeByIdAsync` → `getMainComponentAsync()`) rồi `createInstance()` từ main component đó. Muốn copy cấu hình từ instance tham chiếu thì chỉ đọc giá trị prop `BOOLEAN`/`VARIANT` của nó rồi `setProperties` lên instance mới. Không clone, không detach.

### 3. Dựng layout chung (shell) trước
Dựng đúng khung trong `references/layout.md` → mục "Layout chung" (có bảng instance tham chiếu và danh sách lỗi đã gặp — đọc kỹ trước khi viết script), từng phần một và kiểm tra sau mỗi phần (screenshot). Màn mới đặt trong một Section trên trang người dùng chỉ định, cách xa nội dung có sẵn:
`Menu (80)` + `body (1360)` → `Top bar (48)` → `tab navigation (42)` → vùng nội dung (padding ngang 24, nền `surface/neutral/lighter-1`) → `Page header` → `main content`.

### 4. Lắp nội dung theo pattern
- Dùng instance + variant + component property; chỉnh text qua property hoặc nội dung text node bên trong instance, không vẽ lại, không đổi style (xem "Nguyên tắc không override").
- Bảng: ghép cột `col` = `table-header` + `data` (các `table-cell`), cột hành động cuối dùng `Icon Button / Ghost` (sửa, xem). Phía dưới là `Pagination`. Frame `table` **HUG dọc** (ngang FILL), **tối đa 10 dòng** — chi tiết ở Pattern 1 trong `references/layout.md`.
- Form: `Drawer` 459px bên phải + `overlay`; trường dùng `data entry` (chọn `Type`/`sub type` theo bảng ở mục "Nguồn component hợp lệ"); hành động cuối drawer là `Standard Button / Secondary` (Huỷ) + `Standard Button / Primary` (Lưu/Cập nhật).
- Trạng thái rỗng dùng `_illus` (type=empty/search/404/no task…).

### 5. Token và quy ước đặt tên
- **Mọi** fill, stroke, radius, gap, padding, typography, effect của layer **không nằm trong instance** phải bind vào variable/style (xem `references/tokens.md`). Không để hex/px raw. Nếu gặp giá trị raw trên layer cũ (ngoài instance) → tìm token khớp giá trị và bind lại. Giá trị raw bên trong instance là lỗi của component → ghi vào `component-gaps.md`, không sửa.
- Ưu tiên token **comp/** (đúng component) → **semantic** (`text/…`, `surface/…`, `border/…`, `icon/…`) → mới đến **primitive** (`primary/550`, `neutral/20`). Không dùng primitive khi đã có semantic tương đương.
- Đặt tên layer theo file mẫu: khung màn hình đặt theo trạng thái (`Management`, `Create`, `Edit`, `Detail`); khung con dùng tên thường mô tả vai trò (`body`, `main content`, `header`, `title`, `form`, `action`, `table`, `col`, `data`, `overlay`). Không để tên mặc định `Frame 1321…` cho layer mới.
- Section chứa luồng đặt tên theo chức năng (vd. `Organization Management`), các frame xếp trái → phải theo thứ tự bước, cách nhau ~89px.

### 6. Kiểm tra trước khi bàn giao
- Screenshot từng frame, so với màn hình tham chiếu cùng pattern: kích thước shell, khoảng cách, màu.
- Rà toàn bộ node mới bằng script: duyệt mọi node **không nằm trong instance**, báo fill/stroke SOLID chưa bind, padding/gap/radius > 0 chưa bind, TEXT không có `textStyleId`, tên `Frame \d+`. Giá trị lệch lưới (vd. 15) trên frame layout đổi về token gần nhất.
- **Chạy [scripts/audit-overrides.js](scripts/audit-overrides.js)** trên Section vừa dựng (thay `ROOT_ID`). Kết quả phải rỗng, trừ mục có trong "Ngoại lệ đã duyệt". Có vi phạm → chạy [scripts/reset-overrides.js](scripts/reset-overrides.js) với id các instance đó (giữ prop + nội dung chữ, xoá mọi override khác), rồi audit lại. Không có `use_figma` → audit chỉ đọc bằng [scripts/audit-overrides-rest.py](scripts/audit-overrides-rest.py) (`FIGMA_TOKEN=… python3 scripts/audit-overrides-rest.py <file_key> <node_id>`); script này còn báo nguồn từng component (local / Component / OTHER).
- Không có instance bị detach.
- Báo lại cho người dùng: link frame/section, các component đã dùng, kết quả audit override, phần nào phải tạo mới hoặc thiếu variant (đã ghi vào `component-gaps.md`).

## Ví dụ

**Input:** "Tạo màn hình quản lý cửa hàng gồm danh sách, nút thêm mới và form thêm mới."

**Output:** Section `Store Management` với 2 frame 1440×822:
- `Management`: shell chung (Menu module Product active, Top bar, tab navigation có tab "Store management" active, Page header breadcrumb `Product management / Store management` + nút `Standard Button / Primary` "Add new"), `Filter` + bảng ghép từ `Table / header`/`Table / Cell` + `Pagination`.
- `Create`: cùng shell, phủ `overlay` (`color/global/black-alpha/8`) và `Drawer` 459px, form 2 cột dùng `data entry` (`Type=Input`, `Type=Select`), chân drawer `Cancel` (Secondary) + `Save` (Primary).
Mọi màu bind token `comp/*` hoặc semantic, chữ dùng text style `body/size-m/regular`, `title/size-s/semibold`…, layer đặt tên theo quy ước.
