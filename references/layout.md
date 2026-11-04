# Layout chung và pattern màn hình CRM

Đo từ màn hình mẫu trong CRM-HR-WEB (`GztI8Yyl0PJ1GE0pptPi48`), trang `-> Organization Management` (`962:125160`), section `Organization Management` (`962:126256`).

## Màn hình tham chiếu

| Pattern | Frame | Node id |
|---|---|---|
| Tree + List (danh sách có cây bên trái) | `Management` | `962:134238` |
| Tree + List, biến thể khác | `Management` | `1568:277670` |
| Drawer form sửa (Edit) | `Edit` | `962:133592` |
| Chi tiết (Detail) | `Detail` | `962:133884` |
| Header component (Top bar, state=Default) | `State=Default` | `893:15314` |

Trước khi dựng một pattern, chụp màn hình frame tham chiếu tương ứng (`get_screenshot`) để đối chiếu.

> **Lưu ý:** màn mẫu `962:134238` có 61 override vi phạm và nhiều component đến từ thư viện ngoài (xem `component-gaps.md`). Dùng màn mẫu để tham chiếu **bố cục** và **giá trị prop**, không sao chép override, không coi kích thước/màu trên màn mẫu là chuẩn khi khác main component.

## Layout chung (shell) — frame 1440 × 822, desktop

```
Management (1440×822, auto layout ngang, gap 0, clip, fill Background)
├── Menu                        instance  w80, FILL dọc
└── body                        frame     auto layout dọc, gap 0, FILL × FILL, không fill
    ├── Top bar                 instance  h48, FILL ngang
    ├── tab navigation          instance  h42, FILL ngang
    └── content                 frame     auto layout dọc, FILL × FILL, fill surface/neutral/lighter-1
        │                                 padding 0 / 24 / 16 / 24 (s300, s200), gap 16 (s200)
        ├── Page header         instance  h78, FILL ngang
        └── main content        frame     FILL × FILL, fill neutral/0 (trắng), radius/md (8), clip
```

### Dựng shell nhanh nhất (đã chạy thử, ổn định)

Lấy main component từ instance trên màn hình tham chiếu `962:134238` rồi `createInstance()`:

| Phần | Instance tham chiếu | Main component |
|---|---|---|
| Menu | `2873:437560` | set `Menu` cục bộ, variant `expand=no, channel=no` |
| Top bar | `2888:791426` | set `Top bar` cục bộ, `avatar=no, State=Default, Name=YES` |
| tab navigation | `962:134242` | set `tab navigation` (B2 CRM-ext), `tab=3` |
| Page header | `965:180819` | set `Page header` cục bộ, `Level=Level 3`, bool `Show action group#962:0` |
| Filter | `962:134269` | set `Filter` cục bộ |
| table-header (cột No.) | `962:134272` | `table-header` (B2 CRM-ext) |
| table-header (cột thường) | `962:134285` | `table-header` (B2 CRM-ext) |
| table-cell chữ | `962:134274` | `table-cell` `Type=Text` (B2 CRM-ext; text node tên `Item Text`) |
| table-cell hành động | `962:134438` → `data` → cell đầu | `table-cell` `Type=Slot` (sửa + xem) |
| Pagination | `962:134501` | set `Pagination` (A thư viện Component) |

Tuỳ biến sau khi tạo:
- **Menu**: các instance con tên `_menu` có text là tên module; đặt `active=yes` cho module hiện tại, `no` cho phần còn lại.
- **tab navigation**: các instance con tên `tab` (`active`, `end`). Mặc định tab "Home" đang active, cần đổi `active=no` cho Home và `active=yes` cho tab của màn hình.
- **Page header**: breadcrumb mặc định là `Level 1` / `Level 2`, tiêu đề là text `Title` (sửa nội dung chữ, không đổi style). Nhóm hành động có 3 nút (Ghost, Secondary, Primary); chỉ ẩn qua BOOLEAN prop (`Show action group#962:0` hoặc prop của từng nút nếu có). Không có prop cho nút cần ẩn → giữ nguyên và ghi vào `component-gaps.md`, không đặt `visible=false` trực tiếp.

### Lỗi đã gặp khi chạy thử (phải xử lý)
- **Chữ gắn TEXT prop của instance lồng** (breadcrumb/nút của `Page header`, nhãn `tab`, nút `Standard Button`): sửa `characters` không giữ được → đọc `componentPropertyReferences.characters` của text node rồi `setProperties({[ref]: …})` trên instance lồng sở hữu prop đó.
- **Tìm frame theo tên phải đi từ cha trực tiếp** (`content.children.find(...)`), không dùng `M.findOne(n => n.name === 'main content')`: `Page header` cũng có frame con tên `main content` → sửa nhầm layout bên trong instance (thành override).
- **Frame layout HUG tạo bằng script có thể render sai chiều cao** (screenshot/server vẫn giữ 100px mặc định của `createFrame()` dù plugin báo đúng). Sau khi thêm đủ con: đặt `layoutSizingVertical='FIXED'`, `resize(w, h thật)`, rồi trả lại `counterAxisSizingMode='AUTO'` / HUG; chụp lại để xác nhận.
- **Đổi `active` của `tab` lồng trong `tab navigation`** có thể sinh override `width/height` trên `tab` → thay bằng bản clone `tab navigation` từ frame mình vừa dựng sạch (đã đúng tab active), hoặc tạo lại instance.
- **Filter** tạo mới hiện cả tab và tiêu đề → copy prop BOOLEAN/VARIANT từ `962:134269` (`Tab=false`, `Show title table=false`).
- **table-header** tạo mới hiện checkbox → copy prop từ header tham chiếu (`Show Checkbox=false`; cột No. còn `Show filter=false`).
- **Cell hành động** (`Type=Slot`): nội dung slot là override trên instance, `createInstance()` cho ra ô trống → `clone()` cell tham chiếu. Đây là **ngoại lệ đã duyệt** duy nhất được clone (xem `component-gaps.md`); audit sẽ bỏ qua override bên trong cell này.
- **Pagination** tạo mới không có padding như màn mẫu (màn mẫu đang override padding). **Không** bind padding lên instance. Dùng đúng component; nếu cần lề, đặt Pagination trong frame layout `pagination` có padding token (s100 / s200). Đã ghi vào `component-gaps.md`.
- Khi copy prop từ instance khác, **chỉ** lấy prop `BOOLEAN`/`VARIANT`; prop `INSTANCE_SWAP` gây lỗi `setProperties`.

Chi tiết từng phần:

- **Menu** (80px): logo MB trên cùng, các item `_menu` (64×58, `active=yes/no`) theo thứ tự Workbench, Customer, Business, Marketing, Product, Basic, Public. Item đang ở module hiện tại dùng `active=yes` (ô nền brand, chữ brand). Component set cục bộ `Menu` (`569:55704`, variant `expand=no|yes`, `channel=no`).
- **Top bar** (48px): trái là `Tab Group` (To do list, My customer/My clients — `comp/tabs/level 1/default/title`), phải là `Icon Button / Ghost` tìm kiếm, `Icon Button / Ghost` thông báo (có badge đỏ), khối avatar + tên + chức danh/tổ chức + nút mũi tên. Đường kẻ dưới `border/subtle`.
- **tab navigation** (42px): các tab trang đã mở (`_tabNavigation`, `active=yes/no`, `end=yes/no`): "Home", tab hiện tại active có nút đóng, các tab khác; mũi tên dropdown ở cuối phải.
- **Page header** (78px): breadcrumb (`comp/breadcrumbs/default/text`, separator `/`) phía trên, tiêu đề trang bên dưới (đậm, `text/neutral/default`); nút hành động chính (nếu có) căn phải.
- **main content**: card trắng chiếm hết phần còn lại, cách mép dưới 16px.

## Pattern 1 — List (danh sách)

```
main content
└── Table (w1312)
    ├── Filter      instance h48 (chỉ search) hoặc h92 (title + action)
    │                 nút filter (Icon Button / Secondary) + ô search "Label" + bên phải: setting, download
    ├── table       frame (cột ngang), FILL ngang × HUG dọc — cao theo số dòng, không FILL dọc
    │   └── col ×N  = table-header (h44) + data (table-cell h50 mỗi dòng)
    │                 cột 1: "No." (w56); cột cuối: action (Icon Button / Ghost: sửa, xem), ghim phải
    │                 tối đa 10 dòng (khớp "10/page" của Pagination); col và data cũng HUG dọc
    └── Pagination  instance h48 ("10/page" + "Total N items" trái, số trang phải), nằm ngay dưới table
```

- `table` **HUG dọc**: `table.layoutSizingVertical = 'HUG'` (ngang giữ FILL để cột FILL như Email co giãn theo `main content`).
- **Tối đa 10 dòng** dữ liệu mỗi bảng. Dữ liệu nhiều hơn → chỉ dựng 10 dòng và thể hiện phần còn lại qua `Pagination` ("Total N items", số trang).
- 10 dòng = 44 + 10 × 50 = 544px. Cộng `Filter` (48) và `pagination` (48) là 640px, cao hơn phần `main content` còn lại trong frame 1440×822 (622px). Muốn đủ 10 dòng thì cho frame màn hình cao theo nội dung (HUG dọc, hoặc đặt chiều cao ≥ 840); giữ 822 thì tối đa 9 dòng.

## Pattern 2 — Tree + List

Như Pattern 1, nhưng `main content` chia đôi:
- **Tree Group (S)** w316: `header` (tiêu đề nhóm 14/semibold + `Search`), bên dưới `tree navigation` (variant `Level=Parent|Child 1|Child 2|Child 3`, `State=default|hover|active`; active có nền highlight + vạch trái brand + dấu tick), mỗi dòng có nút `⋮`.
- **Table** w996 bên phải, ngăn cách bằng đường kẻ `border/subtle`.

## Pattern 3 — Drawer form (Create / Edit)

Cách dựng: `clone()` frame List **vừa dựng sạch** (được phép vì không chứa override), rồi tự dựng `overlay` và `Drawer` bằng frame layout, đặt `layoutPositioning='ABSOLUTE'` (overlay 0,0 1440×822; Drawer x981). **Không clone overlay/Drawer từ màn `Edit`** — các trường trong đó đang ở state `Filled`/`Read-only` và có thể mang override. Container Drawer (frame `header` / `body` / `footer`, các `row`) là frame layout → bind token (gap/padding s200, s300; nền `surface/neutral/white`; `shadow/E2`). Mọi trường và nút bên trong tạo mới bằng `createInstance()` từ key, đặt variant `state` qua `setProperties` (`data entry`: Create → `default`, Edit → `filled`, chỉ đọc → `read-only`), điền nhãn qua TEXT prop/nội dung chữ, FILL ngang trong `row`. Tiêu đề drawer: text node trong frame layout, text style `title/size-m/medium`. Nếu component `Drawer` thư viện (key `9f2d8e6a…`) có slot nội dung dùng được thì ưu tiên dùng nó thay cho frame tự dựng — cần xác minh (xem `component-gaps.md`).

Giữ nguyên shell + nội dung List phía sau, thêm:
```
overlay   frame 1440×822, fill color/global/black-alpha/8 (#00000066)
Drawer    frame x981 w459 h822, nền trắng, shadow E2
├── header  h48: tiêu đề (title/size-m/medium) + Icon Button / Ghost đóng (ic_cancel_01)
├── body    h714: form, padding s300 (24), các frame `row` (gap s200 = 16), mỗi row 1–2 trường
│            instance trường FILL ngang trong row; chiều cao giữ theo variant (58)
│            trường dài (Region, Title…) một mình một row
│            control: `data entry` (B1) — Type/sub type theo SKILL.md (instance mới, không clone)
│            trường chỉ đọc: variant State=read-only (không tô nền thủ công)
└── footer  h60: căn phải — Standard Button / Secondary (Cancel) + Standard Button / Primary (Update/Save), giữ nguyên kích thước
```

## Pattern 4 — Detail

Cùng shell; nội dung hiển thị dạng cặp label/giá trị (label `text/neutral/lighter`, giá trị `text/neutral/default`), có thể trong Drawer như Pattern 3 hoặc full trang với `Bottom action`. Xem `962:133884` để chọn đúng biến thể trước khi dựng.

## Pattern luồng (flow)

- Tạo một **Section** đặt tên theo chức năng; bên trong mỗi bước là một frame 1440×822 dùng chung shell.
- Thứ tự trái → phải: `Management` → `Create` → `Edit` → `Detail` (bỏ bước không cần). Khoảng cách giữa các frame ~89px, hàng thứ hai (biến thể/trạng thái) cách hàng trên ~74px.
- Các frame cùng luồng dùng **cùng** Menu active, cùng tab navigation, cùng breadcrumb — chỉ khác phần nội dung/overlay.

## Component cục bộ trong CRM-HR-WEB (trang `🔶 Local components`, `962:148876`)

| Component | Node id | Variant chính |
|---|---|---|
| Menu (sidebar) | `569:55704` | expand=no/yes, channel=no |
| _menu (item sidebar) | `1348:142932` | active=yes/no |
| _tabNavigation | `893:15233` | active, end |
| Tab Group | `1355:230805` | gồm `Tab / Line` |
| tree navigation | `1020:15986` | Level × State |
| Page header (doc) | `1245:62164` | — |
| Top bar (doc) | `1245:66361` | — |
| Filter (doc) | `1335:184220` | — |
| Bottom action (doc) | `1547:152294` | — |
| Data entry (doc) | `1339:107686` | — |
| _badge | `1393:98745` | color × state |
| _chipItem | `1059:61052` | Type=màu |
| _illus (empty state) | `1353:201025` | type=empty/search/404/no task/no noti/upload/no calendar |
| step_item | `1075:117130` | state × type |
| _inputLookup | `1004:41857` | Size=32/36 |
| _uploadCTA | `974:215810` | state |
| Activity Tag | `1443:97070` | Activity × Disabled |

## Component trong thư viện Component (key để `importComponentSetByKeyAsync` / `importComponentByKeyAsync`)

| Component | Loại | Key |
|---|---|---|
| Menu | set | `9351cac31e73fea5812721cdcfc223d9f1d93a05` |
| Top Bar | set | `bad4a76ac27dcd3cdbe0b27dcafe522cd6f5aa6c` |
| Filter | component | `c00c1211651634ff38cf3b83f42c5df56c1e6835` |
| Pagination | set | `97b49a0bbb9b64e9f11fe3d6a6aa1f90b5f1362d` |
| Table / header | set | `4cc6d2c3579c1379bcc865b30673900c8339bbf1` |
| Table_Header | set | `03f22f680d84862547ec51036d6712c525ee773b` |
| Table / Cell | set | `3ea77911e71d7db77c01e9aaafda0d7c74376fee` |
| Standard Button / Primary | set | `fba0a8c6076b5ff6dfea80f1cbb26ac8a9fbe799` |
| Standard Button / Secondary | set | `47246838ac19d21832c7d0bfc84a7eebf3e41353` |
| Standard Button / Ghost | set | `abd85553de5eb26bc86d6aae49314be504fd7bc8` |
| ~~🚧 Input normal~~ | set | **Cấm** — dùng `data entry` (CRM-HR-WEB `1068:91679`) |
| Input | set | `fe54618994e3f8a86ca856e82647bfd4d3222be2` |
| Select / Single Choice | set | `74d65c1deac512024126ae2fbe9eb070799c3e05` |
| Drawer | component | `9f2d8e6a1f116b3aa8b6ee028c4c67da2e9b4ccc` |

Key có thể đổi khi thư viện publish lại. Nếu import lỗi, tìm lại bằng `search_design_system` (lọc library key Component) hoặc lấy main component từ instance trên màn hình tham chiếu.
