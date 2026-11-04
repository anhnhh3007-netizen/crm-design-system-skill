# Ngoại lệ và component còn thiếu

Theo "Nguyên tắc không override" trong SKILL.md: component không đáp ứng thì **không** chỉnh để lách, mà ghi vào đây và báo người dùng gửi team design system. Khi DS cập nhật component → xoá dòng tương ứng và cập nhật `layout.md`.

## Kết quả audit màn mẫu `962:134238` (Tree + List, 03/11/2026, qua REST)

125 instance cấp ngoài, **61 override vi phạm** → **màn mẫu không phải chuẩn để học theo về override**; chỉ dùng để tham chiếu bố cục và lấy cấu hình prop.

**Nguồn component:** `table-header` (10), `table-cell` (100), `tab navigation`, `Search`, `Input (S)` đến từ thư viện ngoài chưa publish (REST 404/403), key khác thư viện Component. **Đã chốt 03/11/2026:** được dùng cả thư viện Component lẫn component của CRM-HR-WEB → các set này hợp lệ là nguồn **B2 (CRM-ext)** trong `catalog.md`, tạo qua instance mẫu, chỉ dùng được trong file CRM-HR-WEB. Rủi ro còn lại: thư viện gốc của chúng chưa publish → không cập nhật được từ nguồn; nên đề xuất DS publish hoặc chuyển vào thư viện Component.

| Instance trên màn mẫu | Override | Ý nghĩa |
|---|---|---|
| `table-cell` › Item Text (×50) | `layoutAlign` | Text bị đổi sang STRETCH trong cell — chỉnh layout bên trong |
| `Menu` › Shape (×2) | `fills` | Tô màu đè trong menu |
| `tab navigation` › tab | `visible` | Ẩn tab thủ công, không qua prop |
| `Page header` (gốc) | `effects`, `paddingLeft/Right` | Padding và effect đè lên instance |
| `Search` › Label · Input / Normal | `effects` · `layoutAlign` | Effect và layout đè |
| `Input (S)` › Base · Input Container · Cursor | `width/height/name` · `strokes` · `visible` | Resize, đổi viền, ẩn con trỏ |
| `Pagination` (gốc) | `boundVariables` | Padding bind đè (chính là hướng dẫn cũ của skill — đã gỡ) |

Field override chuẩn hoá từ dữ liệu thật: `characterStyleOverrides`, `styleOverrideTable`, `lineIndentations`, `lineTypes` luôn đi kèm khi sửa nội dung chữ (102/102 text node, không có style trộn) → script coi là nhiễu. `counterAxisSizingMode` trên instance gốc là cách sizing trong auto layout cha → hợp lệ.

## Ngoại lệ đã duyệt

Chỉ những mục dưới đây được phép vi phạm nguyên tắc; `audit-overrides.js` đã bỏ qua override bên trong của chúng.

| Component | Ngoại lệ | Lý do | Hướng xử lý lâu dài |
|---|---|---|---|
| `table-cell` `Type=Slot` (cột hành động) | `clone()` cell tham chiếu (trong `962:134438` → `data`); nội dung slot là override | `createInstance()` cho ra ô trống, chưa có variant chứa sẵn nút sửa/xem | Đề xuất DS thêm variant `Type=Action` (Icon Button / Ghost sửa + xem) |

## Component còn thiếu / lệch (chưa được phép override — đang dùng tạm)

| Component | Vấn đề | Đang làm tạm | Đề xuất cho DS |
|---|---|---|---|
| `Pagination` | Instance mới không có padding; màn mẫu đang override padding (s100 / s200) | Bọc trong frame layout `pagination` có padding token | Thêm padding vào main component |
| `Drawer` (thư viện, key `9f2d8e6a…`) | Chưa xác minh có slot nội dung dùng được không; màn mẫu dùng frame tự dựng (gap 15, padding 10 lệch lưới) | Drawer = frame layout tự dựng, bind token | Xác nhận Drawer có slot `body`; nếu có thì chuyển sang dùng |
| `Page header` | Chưa xác nhận từng nút trong nhóm hành động có BOOLEAN prop riêng không | Chỉ dùng `Show action group#962:0` | Thêm BOOLEAN prop cho từng nút (Ghost / Secondary / Primary) |
| `table-header`, `table-cell`, `tab navigation`, `Search`, `Input (S)` (B2) | Thư viện gốc chưa publish; chỉ dùng được trong CRM-HR-WEB qua instance mẫu | Dùng theo `catalog.md` mục B2 | Publish thư viện gốc hoặc chuyển vào thư viện Component |

| `🚧 Input password` | Component 🚧 bị cấm; `data entry` không có loại mật khẩu | Chưa có — hỏi người dùng khi cần | Thêm `-> sub type=password` vào `data entry` |

| `🚧 Timeline`, `🚧 Milestone` | Component 🚧 bị cấm; chưa xác minh thay thế tương đương | `step` / `item_step` cho dạng bước; timeline/milestone → hỏi người dùng | Hoàn thiện Timeline và bỏ 🚧 |
| `🚧 Badge highligt` | Component 🚧 bị cấm | `Badge` (thư viện) | Hoàn thiện hoặc gộp vào `Badge` |
| `data entry` `Type=Select, State=filled` | Cao 80 thay vì 58: `❖inputSelection` lồng bên trong bật `isShowTitle=true` → hiện thêm chữ "Title" dưới nhãn | Tắt `isShowTitle` của `❖inputSelection` lồng qua prop (hợp lệ) → cao 58 | Đặt `isShowTitle=false` trong main component |
| `data entry` `-> sub type=look-up` | Không có `State=view` | Màn Detail dùng `Type=Input, -> sub type=default, State=view` | Thêm variant `look-up` + `view` |
| `Menu` (đổi `_menu` active) | Đổi `active` của `_menu` lồng qua prop (hợp lệ) vẫn sinh override `width/height/targetAspectRatio` của icon, `fills` của Shape và `characters` — do main `Menu` có sẵn override trên item Product | `reset-overrides.js` không xoá được (reset rồi đặt lại prop thì override quay lại) → audit báo dương tính giả | Bỏ override trong main `Menu`, hoặc thêm variant chọn module |
| `table-cell` `Type=tag` | Khung trong `.table-cell` cố định 72px (variant `Text` là FILL) → cột rộng hơn thì viền dưới/nền dừng ở 72px, đứt đường kẻ hàng; `Tag outline` cố định 48px nên chữ dài ("On leave", "Resigned") tràn ra ngoài tag; đổi `Color` còn sinh override `primaryAxisSizingMode` | **Không dùng.** Ô trạng thái dùng `Table / Cell` `type=tag, state=default` (thư viện, nguồn A): giãn đúng chiều ngang, tag HUG theo chữ, không sinh override. Lưu ý tag căn giữa ô | Cho `.table-cell` và `Tag outline` FILL/HUG như variant `Text` |
| `data entry` `Type=Select, -> sub type=multi` (`filled`, `view`) | Luôn hiện đúng 5 chip `Chips / Secondary`, không có prop ẩn bớt chip → không thể hiện số lựa chọn khác 5 | Điền nội dung cả 5 chip qua chữ (hợp lệ); màn Lead Management đang dùng 5 sản phẩm | Thêm prop số chip / BOOLEAN ẩn từng chip |

## Mẫu ghi mục mới

`| <Component> | <thiếu variant/prop gì, hoặc giá trị raw/lệch lưới nào trong component> | <đang dùng tạm cái gì> | <đề xuất> |`
