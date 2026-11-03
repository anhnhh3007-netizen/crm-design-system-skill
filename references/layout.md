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
| tab navigation | `962:134242` | set `tab navigation` (thư viện), `tab=3` |
| Page header | `965:180819` | set `Page header` cục bộ, `Level=Level 3`, bool `Show action group#962:0` |
| Filter | `962:134269` | set `Filter` cục bộ |
| table-header (cột No.) | `962:134272` | `table-header` (thư viện) |
| table-header (cột thường) | `962:134285` | `table-header` (thư viện) |
| table-cell chữ | `962:134274` | `table-cell` `Type=Text` (text node tên `Item Text`) |
| table-cell hành động | `962:134438` → `data` → cell đầu | `table-cell` `Type=Slot` (sửa + xem) |
| Pagination | `962:134501` | set `Pagination` (thư viện) |

Tuỳ biến sau khi tạo:
- **Menu**: các instance con tên `_menu` có text là tên module; đặt `active=yes` cho module hiện tại, `no` cho phần còn lại.
- **tab navigation**: các instance con tên `tab` (`active`, `end`). Mặc định tab "Home" đang active, cần đổi `active=no` cho Home và `active=yes` cho tab của màn hình.
- **Page header**: breadcrumb mặc định là `Level 1` / `Level 2`, tiêu đề là text `Title`. Nhóm hành động có 3 nút (Ghost, Secondary, Primary); ẩn nút không dùng bằng `visible=false`.

### Lỗi đã gặp khi chạy thử (phải xử lý)
- **Filter** tạo mới hiện cả tab và tiêu đề → copy prop BOOLEAN/VARIANT từ `962:134269` (`Tab=false`, `Show title table=false`).
- **table-header** tạo mới hiện checkbox → copy prop từ header tham chiếu (`Show Checkbox=false`; cột No. còn `Show filter=false`).
- **Cell hành động** (`Type=Slot`): nội dung slot là override trên instance, `createInstance()` cho ra ô trống → phải `clone()` cell tham chiếu.
- **Pagination** tạo mới mất padding → bind `paddingTop/Bottom = spacing/s100`, `paddingLeft/Right = spacing/s200`.
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
    ├── table       frame (cột ngang)
    │   └── col ×N  = table-header (h44) + data (table-cell h50 mỗi dòng)
    │                 cột 1: "No." (w56); cột cuối: action (Icon Button / Ghost: sửa, xem), ghim phải
    └── Pagination  instance h48 ("10/page" + "Total N items" trái, số trang phải)
```

## Pattern 2 — Tree + List

Như Pattern 1, nhưng `main content` chia đôi:
- **Tree Group (S)** w316: `header` (tiêu đề nhóm 14/semibold + `Search`), bên dưới `tree navigation` (variant `Level=Parent|Child 1|Child 2|Child 3`, `State=default|hover|active`; active có nền highlight + vạch trái brand + dấu tick), mỗi dòng có nút `⋮`.
- **Table** w996 bên phải, ngăn cách bằng đường kẻ `border/subtle`.

## Pattern 3 — Drawer form (Create / Edit)

Cách dựng nhanh: `clone()` frame List vừa dựng, rồi `clone()` `overlay` (`962:133856`) và `Drawer` (`962:133857`) từ màn `Edit`, đặt `layoutPositioning='ABSOLUTE'` (overlay 0,0 1440×822; Drawer x981). Sau đó đổi tiêu đề, nhãn nút, `Title`/`Label` của từng trường, và đưa `state` của trường về `Default` (bản mẫu có trường `Filled`/`Read-only`). Drawer mẫu có gap 15 và padding 10 lệch lưới → đổi về token (16 = s200, 8 = s100). Đổi tên `title` trên/dưới thành `header`/`footer`, các hàng `Frame 13213155xx` thành `row`. Tiêu đề drawer dùng text style `title/size-m/medium`.

Giữ nguyên shell + nội dung List phía sau, thêm:
```
overlay   frame 1440×822, fill color/global/black-alpha/8 (#00000066)
Drawer    frame x981 w459 h822, nền trắng, shadow E2
├── title   h48: tiêu đề (title/size-s/semibold hoặc lớn hơn theo mẫu) + nút đóng ic_cancel_01
├── body    h714: form, padding 24, lưới 2 cột (gap 16), mỗi trường = label trên + control h36
│            trường dài (Region, Title…) chiếm cả 2 cột
│            control: 🚧 Input normal / Select / Single Choice / ❖selectDate
│            trường chỉ đọc dùng state "information" (nền surface/neutral/lighter-1)
└── action  h60: căn phải — Standard Button / Secondary (Cancel) + Standard Button / Primary (Update/Save)
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
| 🚧 Input normal | set | `b1f14a205122c0edf170bda9a7719dca48392ab2` |
| Input | set | `fe54618994e3f8a86ca856e82647bfd4d3222be2` |
| Select / Single Choice | set | `74d65c1deac512024126ae2fbe9eb070799c3e05` |
| Drawer | component | `9f2d8e6a1f116b3aa8b6ee028c4c67da2e9b4ccc` |

Key có thể đổi khi thư viện publish lại. Nếu import lỗi, tìm lại bằng `search_design_system` (lọc library key Component) hoặc lấy main component từ instance trên màn hình tham chiếu.
