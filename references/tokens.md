# Token CRM (đọc từ màn hình `Edit` — `962:133592`, CRM-HR-WEB)

Bind bằng variable/style có tên dưới đây. Giá trị hex chỉ để đối chiếu khi chuyển layer raw sang token; **không** tô hex trực tiếp. Muốn danh sách đầy đủ hơn: `get_variable_defs` trên frame tham chiếu, hoặc `search_design_system` với `entity: "variable"`/`"style"`.

## Thứ tự ưu tiên khi chọn token
1. `comp/<component>/<variant>/<state>/<part>` — khi tô phần của một component.
2. Semantic: `text/…`, `surface/…`, `border/…`, `icon/…`.
3. Primitive (`primary/550`, `neutral/20`, `grey/0`…) — chỉ khi không có semantic phù hợp.

## Màu semantic

| Token | Giá trị | Dùng cho |
|---|---|---|
| `Background` | #F4F4F6 | fill frame màn hình ngoài cùng |
| `surface/neutral/white` · `neutral/0` | #FFFFFF | card `main content` (mẫu dùng `neutral/0`), drawer, bảng |
| `surface/neutral/lighter-1` | #FAFAFB | fill frame `content` (vùng dưới tab navigation), nền trường chỉ đọc |
| `surface/semantic/brand` | #131CD2 | nền brand (menu active, avatar) |
| `color/alias/surface/highlight/lighter-2` | #F3F4FE | nền dòng/tree active |
| `text/neutral/default` | #14141D | chữ chính |
| `text/neutral/lighter` | #7A7D9D | chữ phụ, label |
| `text/semantic/brand` | #131CD2 | chữ brand / active |
| `text/disabled` | #ADAEB1 | chữ disabled |
| `text/semantic/on-surface-semantic` | #FDFDFE | chữ trên nền màu |
| `border/subtle` | #EEEEEF | đường kẻ phân vùng |
| `border/neutral/lighter-2` | #EDEEF2 | viền nhạt |
| `border/neutral/default` | #CACBD9 | viền mặc định |
| `icon/neutral/default` | #14151F | icon chính |
| `icon/secondary` | #7E8084 | icon phụ |
| `icon/semantic/success` | #21C396 | trạng thái online/thành công |
| `icon/semantic/disabled` | #9899B2 | icon disabled |
| `Semantic/red` | #EB2D4B | lỗi, cảnh báo |
| `color/global/black-alpha/8` | #00000066 | overlay sau drawer/modal |

## Màu component (hay dùng)

| Nhóm | Token |
|---|---|
| Bảng | `Table/header/surface` #F4F4F6, `Table/header/text` #7B7EA7, `Table/header/border`, `Table/header/icon`, `comp/table/cell/surface`, `comp/table/cell/text` #14151F, `comp/table/cell/border` #EAEAF1 |
| Input | `comp/input-normal/{default,filled,information}/{surface,border,label,title}` |
| Select | `comp/select/single/{default,filled}/{surface,border,label,trailing-icon}` |
| Date | `comp/select/date-time/{default,information}/{surface,border,label,trailing-icon}` |
| Button primary | `comp/button_standard/primary/default/{surface,title,border}` (#141DD2 / #FFFFFF) |
| Button secondary | `comp/button-standard/secondary/default/{surface,title,border}` |
| Icon button | `comp/button-icon/{ghost,secondary}/default/{surface,icon,border}` |
| Tabs | `comp/tabs/line/default/{title,border}`, `comp/tabs/level 1/default/title` |
| Breadcrumb | `comp/breadcrumbs/default/{text,Separator}` #9899B2 |
| Avatar / badge | `comp/avatar/emphasis/{surface,text}`, `comp/badge-noti/red/{surface,border}` |

## Spacing

| Token | px |
|---|---|
| `spacing/s0` | 0 |
| `spacing/s025` | 2 |
| `spacing/s050` | 4 |
| `spacing/s075` | 6 |
| `spacing/s100` | 8 |
| `spacing/s125` | 10 |
| `spacing/--spacing-12` | 12 |
| `spacing/s200` | 16 |
| `spacing/s300` / `spacing/l` | 24 |

Key để `figma.variables.importVariableByKeyAsync` (thư viện Component, collection "5. Sizing"):
`spacing/s100` `49224ff0eb8334f7f3c596b2978b2b5182e25c27` · `spacing/s150` `22002ff562c254f02111c7fc6c19c53abf6703d2` · `spacing/s200` `344d508895e9a47ac91ac7d1dc7d849f43a037f3` · `spacing/s300` `5c2b7b534470e2e6c3b9deb66107e9aecc5027da` · `radius/md` (= 8) `5d77fc135c7a5a2a66e837a0b93e9b9322a5af0e` · `radius/s` (= 6) `c14367a25898d90787dd991bf8fc34eb4a10d9e6`.
Collection "CRM Design System" cũng có `radius/lg` "Cards" nhưng giá trị là 12, không khớp card 8px của màn mẫu → dùng `radius/md`.

## Kích thước, bo góc, viền

| Token | Giá trị |
|---|---|
| `comp/button-standard/size/xs` / `High/xs` | 32 (cao control nhỏ) |
| `comp/button-standard/size/s` / `High/s` | 36 (cao control mặc định trong form) |
| `comp/button-standard/border-radius/radius-S`, `base/border_radius/radius_S` | 6 |
| `component/button/radius` | 8 |
| `border-radius/--border-radius-360` | 360 (tròn: avatar, badge) |
| `stroke/sm` | 1 |

## Typography (font Inter — `typo/font-family/Main`)

| Text style | Size / line-height / weight | Dùng cho |
|---|---|---|
| `body/size-s/regular` | 12 / 18 / 400 | caption, label nhỏ, breadcrumb |
| `body/size-s/medium` | 12 / 18 / 500 | label nhỏ nhấn |
| `body/size-m/regular` | 14 / 22 / 400 | nội dung, ô bảng, giá trị input |
| `body/size-m/medium` | 14 / 22 / 500 | nút, tab active |
| `title/size-xs/regular` · `title/size-xs/medium` | 12 / 18 | tiêu đề nhỏ |
| `title/size-s/regular` · `title/size-s/semibold` | 14 / 22 / 400·600 | tiêu đề nhóm, tên người dùng |
| `title/size-m/medium` | 16 / — / 500 | tiêu đề drawer |

Key text style (`figma.importStyleByKeyAsync`): `title/size-m/medium` `3db211446d03d72644e9caf0b89c05d2e0b76fef` · `title/size-s/semibold` `b7f46959706a7685a2d5cfa8d18a08d0bd24e8ea` · `title/size-l/semibold` `a1c75410fdd60450b969f6087570a91f61bb1116`.

Không dùng `body-2` (Public Sans) — đó là style cũ còn sót lại.

## Effect
- `shadow/E2` — drawer, popup, dropdown.
- `E-CTA` — nút CTA.
