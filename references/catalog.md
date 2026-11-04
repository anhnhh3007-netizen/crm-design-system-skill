# Danh mục component hợp lệ (sinh tự động 03/11/2026 bởi `scripts/build-catalog.py` — không sửa tay)

Cột **Dùng** = số instance cấp ngoài trên các màn CRM-HR-WEB. **Trạng thái**: ok · cấm (có 🚧 — không dùng) · part (thành phần con, không dùng trực tiếp) · demo.
Cách tạo instance theo nguồn: xem SKILL.md → "Nguồn component hợp lệ".

## A. Thư viện Component (`m1uk68gT43hnMwKYOmv6vE`) — import theo key

| Tên | Loại | Key | Trang | Prop / variant | Cỡ | Dùng | Trạng thái |
|---|---|---|---|---|---|---|---|
| Icon Button / Primary | set | `cf73df3de7bec5f24ab5052282aebe88f6b77438` | -> Icon Button ✅ |  | 58×58 | 5 | ok |
| Bottom Sheet | component | `801c590e33e327ce5eb895e5f028a4f2abdd022b` | Bottom Sheet ✅ |  | 375×728 | 0 | ok |
| Expandable | set | `7c29765c06c38b6cfbe868739ba0dd3540f2506d` | Expandable ✅ | isShowSwap:boolean · isShowLeadingIcon:boolean · isShowSubText:boolean · isShowCaption:boolean · Size=L\|XS\|S\|M · Selected=yes\|no | 407×85 | 0 | ok |
| Master/Input Number | set | `4dea972cfb5b8df08c9580f0e5596e70d8061cd9` | Select ✅ ✅ | Label:text · isShowClear:boolean · isShowUnit:boolean · isShowTitle:boolean · isShowCaption:boolean · Unit:text · Size=M\|L\|XS\|S | 320×116 | 0 | ok |
| Master/Select Date | set | `9a1205edc17c9c439db45dfff82568f127893593` | Select ✅ ✅ | Start Date:boolean · End Date:boolean · Sufix Items:boolean · Show To:boolean · Show Caption:boolean · Show Title:boolean · Show Required:boolean · Show swap:boolean · size=L\|M\|S\|XS | 328×108 | 2 | ok |
| Master/Text Area | set | `013af1d740e50af97b00bd97993c1d952230cebd` | Select ✅ ✅ | Label:text · isShowTitle:boolean · isShowCaption:boolean · isShowCounter:boolean · isShowScrollbar:boolean · size=L\|M\|S\|XS | 320×176 | 0 | ok |
| Action list | set | `ea0307754d5ac103e1ff40251b74c0c354954275` | ❖ Action List | Show sort:boolean · Show filter:boolean · Show header title:boolean · Slot:slot · Slot2:slot · Show Scrollbar:boolean · Show slot:boolean · action list:slot · action list2:slot · action list3:slot · action list4:slot · t | 367×198 | 7 | ok |
| Alert | set | `37bbc8d8a86a06531c48df1b4dad4b11cc179e31` | ❖ Alert | isShowAction:boolean · isShowTitle:boolean · isShowContent:boolean · Type=Error\|Warning\|Success\|Information · Orientation=Horizontal\|Vertical | 400×92 | 1 | ok |
| Avatar group | set | `615b627f775310426888324a70607613cc50f70a` | ❖ Avatar | Size=24px | 104×24 | 0 | ok |
| avatar | set | `a845cadec2596fed199c50c5ef0dfc9555baa21c` | ❖ Avatar | isShowBorder:boolean · isShowDot:boolean · size=XX\|XS\|S\|M\|L\|XL\|XXL · type=text soft\|text\|icon\|img\|icon soft | 38×38 | 26 | ok |
| Badge | set | `1400c7c6beca07784f8831eac4c4f92c2d09416b` | ❖ Badge | Type=dot\|> 2\|1 · Color=default\|custom | 8×8 | 33 | ok |
| Badge / position | set | `1d335232b63abe266cb9af05b3915405e8b4f524` | ❖ Badge | Position=on avatar\|on icon · size=Largr\|Large\|Medium | 32×32 | 2 | ok |
| A logo MB | set | `7f3f6a938057446a439d6e5f9eeb3cb8858450d3` | ❖ Base | State=Default\|White | 59×24 | 0 | ok |
| Breadcrumbs | component | `00c466df061c25bd29a8897f4e943c4d26bc4f0d` | ❖ Breadcrumbs | Stage 4+:boolean | 312×22 | 45 | ok |
| Floating Button | set | `fe6cca7756688604b70b7692e72e261056682e23` | ❖ Button floating | Expanded=On\|Off · Size=L\|M · Status=Default\|Pressed\|Loading\|Disable | 56×56 | 0 | ok |
| Group Buttons / Horizontal / Primary | set | `1e22ca54203afd4dd2ecc188f91aa450909935f7` | ❖ Button group | Size=XS\|M\|S · Position=Bottom\|Sticky | 380×68 | 2 | ok |
| Group Buttons / Horizontal / Secondary | set | `90dc4915ef0fb9afa65f247c3587be3b5ae94389` | ❖ Button group | Type=Icon action\|Flow action\|Flexible · Position=Bottom\|Sticky | 375×92 | 0 | ok |
| Group Buttons / Vertical | set | `ea9fb2efbd66c834ee8ee33e456c08901af0c8bc` | ❖ Button group | Position=Bottom\|Sticky · Actions=1\|3\|2 | 375×196 | 0 | ok |
| Icon Button / Ghost | set | `205275e78d2507d5c70204a7c2b11a4fc43881f4` | ❖ Button icon | Icon:instance_swap · State=Default\|Pressed\|Disabled\|Loading · Size=S\|XL\|L\|M\|XS | 58×58 | 158 | ok |
| Icon Button / Secondary | set | `22aae69b29143853416764c48f9136ee2ac8f703` | ❖ Button icon | Icon:instance_swap · State=Default\|Pressed\|Disabled\|Loading · Size=XS\|S\|M\|L\|XL | 58×58 | 95 | ok |
| Standard Button / Ghost | set | `abd85553de5eb26bc86d6aae49314be504fd7bc8` | ❖ Button standard | Type=Only Text\|Leading icon\|Trailing icon\|Both · State=Default\|Pressed\|Disabled\|Loading · Size=M\|S\|L\|XL\|XS · Show icon left=On\|Off · Show icon right=On\|Off | 127×58 | 56 | ok |
| Standard Button / Primary | set | `fba0a8c6076b5ff6dfea80f1cbb26ac8a9fbe799` | ❖ Button standard | State=Default\|Pressed\|Disabled\|Loading · Size=XS\|S\|M\|L\|XL · Show icon left=Off\|On · Show icon right=On\|Off | 115×44 | 290 | ok |
| Standard Button / Secondary | set | `47246838ac19d21832c7d0bfc84a7eebf3e41353` | ❖ Button standard | Type=Only Text\|Leading icon\|Trailing icon\|Both · State=Default\|Pressed\|Disabled\|Loading · Size=M\|S\|L\|XL\|XS · Show icon left=On\|Off · Show icon right=On\|Off | 127×58 | 544 | ok |
| Swipe Button | set | `9964b982da6394e1eb21544cd660d2d55316cb6b` | ❖ Button swipe | Text:text · Icon:instance_swap · State=Default\|Pressed\|Disabled\|Dragged · Active=False\|True | 300×56 | 0 | ok |
| Text Button | set | `c8a709e3696efa4fa95b4b023b31b8bffaeba162` | ❖ Button text | Show icon left:boolean · Show icon right:boolean · Label:text · State=Enabled\|Pressed\|Disabled\|Loading\|Default · Size=XS\|S\|M\|L\|XL | 131×32 | 0 | ok |
| Checkbox | set | `e1dd4331f6995b8795ca3e06c0737f7b9573beb2` | ❖ Checkbox | isShowPadding:boolean · type=Selected\|Unselected\|Indeterminate · state=Disabled\|Enabled\|Focused\|Pressed · size=Large\|Medium | 24×24 | 88 | ok |
| Chips / Primary | set | `22e10fd3d17cb92732c4dd1bc05177d96a656c35` | ❖ Chips | Icon:boolean · Clear:boolean · State=Disabled\|Dragged\|Pressed\|Enabled · Type=Inactive\|Active · Size=S\|M\|L | 106×28 | 0 | ok |
| Chips / Secondary | set | `64fa993dc4c6aefe6042cfa3ac9974fdd09c0259` | ❖ Chips | Icon:boolean · Clear:boolean · Property 1=Disabled\|Dragged\|Enabled\|Pressed · Property 2=Active\|Inactive · Property 3=L\|M\|S · Property 4=no | 106×28 | 171 | ok |
| Coach mark  | set | `cd8696223b568fdfba4e3e5e4a47d5f3f5880f93` | ❖ Coach mark | align=Default\|top\|right\|left\|bottom · Type=text\|img | 290×132 | 0 | ok |
| Date picker / Primary | set | `d21d0b36908d8b34185620b17ab8c7fd3feb0cec` | ❖ Date picker | suggestion:boolean · Input:boolean · Title:boolean · Type=Default\|Lịch âm\|Gợi ý\|Date time\|Time\|Mont\|Year | 350×390 | 0 | ok |
| Date picker / Secondary | set | `c963260469fe50a5ee9c7bd1cab808a8874e0b78` | ❖ Date picker | Minute=yes\|no · Hour=yes\|no · Day=yes\|no · Month=yes\|no · Year=yes\|no | 375×224 | 0 | ok |
| Drawer | component | `9f2d8e6a1f116b3aa8b6ee028c4c67da2e9b4ccc` | ❖ Drawer |  | 459×822 | 0 | ok |
| Input / PIN | set | `2b00b45b7d3c8ef0af7d643543ac478e0eb4bd98` | ❖ Input PIN | State=Default\|Filled\|Focus\|Error · Size=S\|M\|L\|XS | 300×102 | 0 | ok |
| Counter / Compact | set | `5d5a6f5743f22978a630fe9553005177695092a3` | ❖ Input counter | size=S\|M\|L · state=disabled\|focus\|default · step=min\|current\|max | 116×28 | 0 | ok |
| Counter / Line | set | `89402512c6359595858a473b6026d0b19b01f00e` | ❖ Input counter | size=S\|M\|L · state=disabled\|focus\|default · step=min\|current\|max | 116×28 | 0 | ok |
| Counter / Split | set | `b283e6f335a13c7187f501b004f71fb4888c1d33` | ❖ Input counter | size=S\|M\|L · state=disabled\|focus\|default · step=min\|current\|max | 116×28 | 0 | ok |
| Date range | set | `5fb04aaf3b395ece58a47a095b2757244c8ee634` | ❖ Input date picker | State=Filled\|Default\|Focus\|Disable\|Error\|Read-only · Size=M\|L\|S\|XS | 300×108 | 9 | ok |
| Single date | set | `cb959221be8fcab572af35323dde747053790523` | ❖ Input date picker | State=Filled\|Default\|Focus\|Disable\|Error\|Read-only · size=M\|L\|S\|XS | 300×108 | 13 | ok |
| Single time | set | `fcde048c8a40b6df74911166ea38d114438d6702` | ❖ Input date picker | State=Filled\|Default\|Focus\|Disable\|Error\|Read-only · Size=M\|L\|S\|XS | 300×108 | 8 | ok |
| Time range | set | `71f97f5d9868275d240acffb0677233ccd6f61ab` | ❖ Input date picker | State=Filled\|Default\|Focus\|Disable\|Error\|Read-only · size=M\|L\|S\|XS | 300×108 | 7 | ok |
| Input / Number / Primary | set | `8777d2ecc51326c86897cefe2e76d19f8ef9ea5a` | ❖ Input number | State=Default\|Filled\|Disabled\|Focus\|Error\|Read-only · Size=S\|M\|L\|XS | 300×80 | 0 | ok |
| Input / Number / Secondary | set | `4dbf7f02a66860f1af7528d50417763d7000c9a7` | ❖ Input number | State=Default\|Filled\|Disabled\|Focus\|Error\|Read-only · Size=S\|M\|L\|XS | 300×92 | 0 | ok |
| Input / Search | set | `f52d276e79b96391fd9eb63931bdad69516840bd` | ❖ Input search | State=Default\|Filled\|Disabled\|Focus\|Error\|Read-only · Size=S\|M\|L\|XS | 300×80 | 0 | ok |
| Select / Multiple Choice | set | `25cd66ced55ed6b18a5e6f3c40c5342e86a1e1ff` | ❖ Input select | State=Default\|Error\|Filled\|Focus\|Disabled\|Read-only · 👉Value=inner box\|outer box · Size=M\|L\|S\|XS | 300×70 | 7 | ok |
| Select / Single Choice | set | `74d65c1deac512024126ae2fbe9eb070799c3e05` | ❖ Input select | State=Default\|Filled\|Disabled\|Focus\|Error\|Read-only · Size=S\|M\|L\|XS | 300×80 | 117 | ok |
| Input / Text | set | `9d4965e797f18efba5af34f2f6f0426c0a0b971c` | ❖ Input text | State=Default\|Filled\|Disabled\|Focus\|Error\|Read-only · Size=S\|M\|L\|XS | 300×80 | 52 | ok |
| Input / Text area | set | `7e87fa756d9fbdde4013af3217988b0e9ddbc74a` | ❖ Input text area | State=Default\|Filled\|Disabled\|Focus\|Error\|Read-only · Size=S\|M\|L\|XS | 300×164 | 17 | ok |
| Modal / Primary | component | `db8ca338cd60b4b31d53a9f6af66c3b30c9be729` | ❖ Modal |  | 720×194 | 0 | ok |
| Pagination | set | `97b49a0bbb9b64e9f11fe3d6a6aa1f90b5f1362d` | ❖ Pagination | Property 1=Default | 966×32 | 354 | ok |
| Progress bar | set | `762fb012843c521f55337bd64a5890576b163b8e` | ❖ Progress Bar | Position=Start\|Center\|End · Type=No Label\|Right Text\|Both Text\|Tooltips\|Left text | 320×21 | 3 | ok |
| Radio Button | set | `523b0191ec2a6acd06f8ee37bc936144c0c0b436` | ❖ Radio | isShowPadding:boolean · type=Selected\|Unselected · state=Enabled\|Focused\|Pressed\|Disabled | 40×40 | 19 | ok |
| Scrollbar | set | `a44f21b77c9474409236ca4e95dde16486e97c57` | ❖ Scrollbar | Orientation=horizontal\|vertical | 12×300 | 7 | ok |
| Slider | set | `9b1e4e1d9d2ba182235d51705b4eb2bb72878b55` | ❖ Slider | state=press\|disable\|default · type=single\|range\|center · position=start\|center\|end | 196×40 | 0 | ok |
| Snackbar | set | `e4ec4ff8fda974dcda58488919403032b82f3228` | ❖ Snackbar | Orientation=Vertical\|Horizontal · Status=Success\|Information\|Warning\|Error | 351×56 | 0 | ok |
| Status / emphasis | set | `c1da54c758d0ff3d325311821e109d2607c904c8` | ❖ Status | Size=M\|S\|L · Type=Customize\|Neutral\|Error\|Warning\|Success\|Infor | 85×32 | 2 | ok |
| Status / normal | set | `388a1bb311e85dc4c5006330dac8a1fc28e5a5ff` | ❖ Status | Size=S\|M\|L · Type=Customize\|Neutral\|Error\|Warning\|Success\|Infor | 64×28 | 7 | ok |
| step | set | `ff76a03559a8e01cbca6f9eb1477e38d9d1d6cfd` | ❖ Steps | type=1\|2\|3 | 808×68 | 0 | ok |
| Switch | set | `cea65225611604dc4faa70784944501719de3a77` | ❖ Switch | selected=True\|False · disable=False\|True · Size=Large\|Medium | 40×24 | 20 | ok |
| Tab Group | set | `aabd1aaf31dc15d2cf8b486fb2448ec8554d07d9` | ❖ Tab | Slot:slot · Slot 2:slot · Reverse=OFF\|ON · Level=1\|2 | 445×40 | 248 | ok |
| Table | component | `7aa4a539fdc36b2fb84649453a52fa84b67d4284` | ❖ Table |  | 2084×204 | 1 | ok |
| Table / Cell | set | `3ea77911e71d7db77c01e9aaafda0d7c74376fee` | ❖ Table | type=amount\|img\|checkbox\|radio\|select\|input\|switch\|account\|tag\|content\|button\|icon\|file\|fil · state=default\|hover\|selected\|read-only | 180×50 | 1015 | ok |
| Table / header | set | `4cc6d2c3579c1379bcc865b30673900c8339bbf1` | ❖ Table | State=default\|active\|focus · Type=text\|filter\|checkbox\|blank | 97×44 | 80 | ok |
| Tag / normal | set | `0beaef9660a72a54aedd31d9608518e30dc5ebc9` | ❖ Tag | Show icon:boolean · Show close:boolean · icon:instance_swap · Size=M\|L\|S · Color=Pink\|Customize\|Red\|Orange\|Yellow\|Green\|Blue\|Purple · Type=Rectangle\|Pill | 88×30 | 97 | ok |
| Tag fill | set | `aa17dfa89e0d03a8168a79f52a95ef2bceda82d5` | ❖ Tag | Show icon:boolean · Show close:boolean · icon:instance_swap · Size=M\|L\|S · Color=Pink\|Customize\|Red\|Orange\|Yellow\|Green\|Blue\|Purple · Type=Rectangle\|Pill | 89×30 | 9 | ok |
| Toast message | set | `53679c8f48274e2308792b5690465e07422a925b` | ❖ Toast Message | Icon:boolean · Type=Success\|Failed\|Warning\|Information | 154×40 | 0 | ok |
| tooltip | set | `ad2a8c0737da743ed0740c74fe66e36669ec8054` | ❖ Tooltip | align=left <-\|bottom\|right ->\|top · Type=Text only\|Icon text\|Action | 112×34 | 0 | ok |
| Top Bar | set | `bad4a76ac27dcd3cdbe0b27dcafe522cd6f5aa6c` | ❖ Top Bar | showIcon:boolean · Instance:instance_swap · type=Post-Login · level=L1\|2 icon\|3 icon | 375×100 | 0 | ok |
| Tree | set | `be91393b24ce5826b55485c0ebd2f9d7ef20c09d` | ❖ Tree | Property 1=Default\|Icon\|Checkbox | 300×684 | 1 | ok |
| Tree / Elements | set | `f610c51df564599dfab6e3cdd22109ef6e8c9278` | ❖ Tree | checkbox:boolean · left icon:boolean · chevon:boolean · sub text:boolean · right icon:boolean · Level=Child 3\|Parent\|Child 1\|Child 2 · State=selected\|default\|hover | 306×36 | 26 | ok |
| Bubbles | component | `dc3e6b734ab803d473ba000704f3bf093f2cc07d` | Chart |  | 684×247 | 0 | demo |
| ChartGrid | component | `450f493ceab4bb4eb099e21fa7c389145d447503` | Chart | Data visualize:slot · Legend:slot | 717×506 | 0 | demo |
| Horizontal bar chart | set | `2a0b58c6da47daf6b99ed0b0c541116ebdcbb466` | Chart | Column=1\|2\|3 · Legend=Default\|none\|out\|in · State=Default\|blue active\|green active\|orange active · Stack bar=no\|yes | 378×573 | 0 | demo |
| Tab Group | set | `74cbe9d61f8b7bb3f7039862757265d673bf06af` | Chart | Slot:slot · Slot 2:slot · Reverse=OFF\|ON · Level=1\|2 | 445×40 | 0 | demo |
| Component 1 | set | `25098f7dcf40a1d72293fe0fe732bc896880cf44` | Demo | expand=yes\|no · channel=no | 80×822 | 15 | demo |
| Menu | set | `9351cac31e73fea5812721cdcfc223d9f1d93a05` | Demo | expand=yes\|no · channel=no | 80×822 | 0 | demo |
| ❖avatarIndicators | set | `c7d36881e4aa275c7f9119101250d1528f09a080` | ​🧱 Parts | size=XXXL\|XS\|S\|M\|L\|XL\|XXL · status=online\|offline | 22×22 | 0 | part |
| ❖basicNode | set | `5571fcfdf374028bc3a8bd59571ffb76a6d2a1bb` | ​🧱 Parts | type=green\|purple\|orange\|red\|pink\|yellow\|blue | 1×1 | 0 | part |
| ❖chartBorder | component | `5fe9e0f7c99887d1e576a82a08834bc398d77000` | ​🧱 Parts |  | 2×200 | 0 | part |
| ❖chartItem/Cursors | component | `40fc353c61186e3c5d225ddaf00a31896651e3fe` | ​🧱 Parts |  | 31×30 | 0 | part |
| ❖chartItem/Tooltip | component | `9e53a9105bc605eab363aaa17a7899c95aa60c91` | ​🧱 Parts |  | 71×34 | 0 | part |
| ❖coachMarkItem | set | `81b1eb81742ab7aa3973efc5e6a73f38ed3762ac` | ​🧱 Parts | Property 1=Default\|Variant2 | 23×18 | 0 | part |
| ❖datePicker | set | `25123a2c64cf72d25a4ca99f898463207f14b7ea` | ​🧱 Parts | Today:boolean · state=focus\|default | 312×60 | 4 | part |
| ❖datePicker/day | component | `2d2e3f324c3b6ff31fdb88559f17855531e7b470` | ​🧱 Parts |  | 48×40 | 0 | part |
| ❖datePicker/optionItem | component | `d03470863d9718d7c5429c25b92e7265e23a1f4a` | ​🧱 Parts | Show sub text:boolean | 40×55 | 0 | part |
| ❖file | set | `77bc735b75e0e12f86b9bc155ea7bd860145a485` | ​🧱 Parts | type=jpeg\|doc\|xls\|svg\|pfd\|png\|ppt | 24×24 | 1 | part |
| ❖graphi&grid | set | `5103933244adf735e12c4e9814d925df905c2504` | ​🧱 Parts | type=Default\|2 chiều | 663×430 | 0 | part |
| ❖img | component | `faf9aa895dd1a6ca6f13567b333377fcbd1c868f` | ​🧱 Parts |  | 64×64 | 0 | part |
| ❖inputSelection | set | `4aa10d31d1f302cac74bf3e2f7bc20f48aca95aa` | ​🧱 Parts | Label:text · isShowClear:boolean · isShowLeadingIcon:boolean · isShowTitle:boolean · isShowCaption:boolean · Leading Icon:instance_swap · isShowSwap:boolean · isShowUnit:boolean · Type=select single choice\|select multi c | 300×108 | 10 | part |
| ❖legend | set | `2bd9cd0ebe7d0918020d4a93a47ebbb9661fa7ee` | ​🧱 Parts | active=yes\|no · Color=gray\|red\|sky\|yellow\|orange\|green\|purple\|pink\|ocean\|cyan | 92×26 | 0 | part |
| ❖pagination/Item | set | `4b35d8de6a9abfbf399e3ed9cf9958be7c82389d` | ​🧱 Parts | State=active\|hove\|default | 32×32 | 0 | part |
| ❖slider | set | `bedb07c8c7c6690aadef3450b0b19edd74b59cd4` | ​🧱 Parts | isShowMark:boolean · isShowNumber:boolean · type=range\|single\|center | 196×40 | 0 | part |
| ❖slider/handle | set | `eb28381e501728aef90f3cd357dc1d0620dee2c7` | ​🧱 Parts | state=press\|anchor\|default · disable=no\|yes | 6×6 | 0 | part |
| ❖slider/mark | set | `b6021a4c1196a1fdd865136326a697c82373355b` | ​🧱 Parts | State=Active\|Inactive\|Disabled | 2×6 | 0 | part |
| ❖slider/track | set | `bb07e6c78cdf2a9111bb22e3b06f3cd06a1f7b2f` | ​🧱 Parts | State=Disabled\|Inactive\|Active | 82×4 | 0 | part |
| ❖stepItem | set | `fe4bbd38ad9c1ed6e23963c9f9c584d51c2ab340` | ​🧱 Parts | Property 1=default\|wait\|inprgress\|done\|error · Size=L\|S | 24×24 | 1 | part |
| ❖stepLine | set | `1a78e244a896b24f23e89d5b81461e0100f2a0d3` | ​🧱 Parts | active=no\|yes\|Rectangle 309\|Rectangle 308 · oriental=horizontal\|vertical | 200×4 | 1 | part |
| ❖subText | set | `1aeb671594592fabdcf8a31381389d640dc62223` | ​🧱 Parts | icon:boolean · Size=XS\|M\|S\|L | 130×18 | 8 | part |
| ❖swap | component | `39aef4e7e3c36e29ced000221a0b865fe772e778` | ​🧱 Parts |  | 24×24 | 5 | part |
| ❖tableCell | component | `d0f18ace6233d60d3b32ddd1074e3518aff093a3` | ​🧱 Parts | Container:slot | 155×50 | 0 | part |
| ❖tableFilter | set | `ebd7c643b8d1347df410a2c1e0db90d2ca085d24` | ​🧱 Parts | state=active\|default\|focus | 20×20 | 0 | part |
| ❖text | set | `cd9fe964e53b1a2701eaa2d67902bccca8b096ac` | ​🧱 Parts | sub-text:boolean · Size=L\|S\|XS\|M | 147×52 | 99 | part |
| ❖timePicker/column | component | `86f746708897ecff3d2fe32549bd98586dbafe83` | ​🧱 Parts |  | 34×224 | 0 | part |
| ❖timePicker/row | set | `52a99ac61ffdd4e85075c9f5a83408109cf2f0c0` | ​🧱 Parts | active=no\|yes | 38×32 | 0 | part |
| ❖title | set | `df68f41b14d0d99dd623948bc4d11f3f9bab9d9b` | ​🧱 Parts | Slot:slot · require:boolean · sub-text:boolean · icon:boolean · Slot 2:slot · Slot 3:slot · Size=S\|XS\|M\|L | 172×38 | 3 | part |
| ❖topIndicator | component | `c7fa1d19d90f6d7c899da80d4866e9552ce8863e` | ​🧱 Parts |  | 375×28 | 0 | part |
| ❖treeChevron | set | `12515a915675284da0386b05a2747a569047098d` | ​🧱 Parts | type=expand\|def\|none | 20×20 | 0 | part |
| ❖treeLine | component | `092a6f16f0213074b8c36f946e7b0e633adab109` | ​🧱 Parts |  | 20×24 | 18 | part |
| ❖xAxis | set | `2d4887fa618752c371d56cb3205f52c392389860` | ​🧱 Parts | type=long\|short | 795×26 | 0 | part |
| ❖yAxis | set | `4cb05f80395d9d06395235c40ca6c39013b30696` | ​🧱 Parts | type=long\|short\|2 chiều | 38×498 | 0 | part |
| 🚧 Badge highligt | set | `4cf6c902f562d574df784c0740604c8c28448a38` | 🚧 Badge highligt | isShowLeadingIcon:boolean · isShowTraillingIcon:boolean · Size=S\|M\|L · Icon=Icon leading\|Only · Color=Error\|Warning\|Success\|Blue\|Purple\|Pink\|Orange | 81×22 | 0 | cấm |
| 🚧 Input leading dropdown | set | `211a42909c855b189d13accbf53ed83dc500ddde` | 🚧 Input dropdown | Property 1=Leading dropdown · Property 2=False · Property 3=False\|True · Property 4=False\|True · Property 5=False\|True · Property 6=False\|True · Property 7=Disabled\|Filled\|Focused\|Placeholder | 320×44 | 0 | cấm |
| 🚧 Input leading dropdown master | set | `c8c69136450721a2e24046760cfd84bcff4eeea7` | 🚧 Input dropdown | Property 1=Leading dropdown · Property 2=False\|True | 320×96 | 0 | cấm |
| 🚧 Input trailing dropdown | set | `de2ec887a2ef7fbd5849d603792dd0a3379b1d73` | 🚧 Input dropdown | Property 1=Trailing dropdown · Property 2=False · Property 3=False\|True · Property 4=False\|True · Property 5=False\|True · Property 6=False\|True · Property 7=Disabled\|Filled\|Focused\|Placeholder | 320×44 | 0 | cấm |
| 🚧 Input trailing dropdown master | set | `c7f5d471a2739b550504a19118051d1c546dbbbd` | 🚧 Input dropdown | Property 1=input · Property 2=normal · Property 3=Trailing dropdown · Property 4=False\|True | 320×96 | 0 | cấm |
| 🚧 Input normal | set | `b1f14a205122c0edf170bda9a7719dca48392ab2` | 🚧 Input normal | state=Default\|Filled\|Focused\|Disabled\|Error\|Read-only · iShowTitle=True\|False · isShowLeadingIcon=False\|True · isShowCaption=False\|True · size=L\|M\|S\|XS | 320×98 | 96 | cấm |
| 🚧 Input password | set | `5e0d9f392d721c984de0d473843fb255b5ab5806` | 🚧 Input password | state=Default\|Filled\|Focused\|Disabled\|Error · iShowTitle=True\|False · isShowCaption=False\|True · size=L\|M\|S | 320×96 | 0 | cấm |
| 🚧 Milestone | set | `4e22492f99b72ddc842d2948b502ebbd1fc1c05c` | 🚧 Timeline | state=error\|success\|active\|inactive · type=dot\|number\|icon\|line · size=M\|S | 24×24 | 0 | cấm |
| 🚧 Step | set | `4e10842fa19f7b830cc53c29f7c2653dab5b2151` | 🚧 Timeline | Show [Display] Title:boolean · Style=2\|1\|3 | 43×72 | 0 | cấm |
| 🚧 Timeline | set | `74b2600c35102f2b5cb5beeb06aa5edf9ffd500b` | 🚧 Timeline | Show [Display] Title:boolean · Swap=yes\|no | 80×40 | 0 | cấm |
| 🚧 Timeline | set | `d08905afa139cc200367f69bd0888b858acbefb9` | 🚧 Timeline | type=dot\|number\|icon · position=start\|end · state=error\|success\|active\|inactive · focus=yes\|no · swap=yes\|no | 132×69 | 0 | cấm |

## B1. CRM-HR-WEB — component cục bộ (trang `🔶 Local components`) — dùng trong CRM-HR-WEB qua node id

| Tên | Loại | Node id | Prop / variant | Cỡ | Dùng | Instance mẫu |
|---|---|---|---|---|---|---|
| data entry | set | `1068:91679` | Require:text · Required:boolean · infor:boolean · Type=Date\|Input\|Search\|Select\|Single date\|Time\|Text Area\|Time range · -> sub type=default\|currency\|look-up\|multi\|single\|date range\|time range · State=default\|focus\|filled | 320×58 | 2117 | `1335:196123` (🔶 Local components) |
| Page header | set | `893:15620` | Show action group:boolean · Level=Level 1\|Level 2\|Level 3\|Level 4 | 868×78 | 371 | `1302:113821` (🔥  Home) |
| Menu | set | `569:55704` | expand=yes\|no · channel=no | 80×830 | 351 | `569:56043` (🔶 Local components) |
| Filter | set | `893:13188` | Tab:boolean · Show table setting:boolean · Show download:boolean · Show title table:boolean · Show filter:boolean · Show search:boolean · action group:slot · filter:slot · Slot:slot · Type=default\|filter\|chip\|setting | 1320×220 | 312 | `1302:116004` (🔥  Home) |
| Top bar | set | `893:15313` | Name:boolean · State=Default\|Tab selected\|Account selected | 860×48 | 292 | `1302:113818` (🔥  Home) |
| data | component | `1548:189704` |  | 48×50 | 212 | `1979:428931` (🔥  Home) |
| Top bar | set | `569:54792` | Name=NO\|YES · State=Default · avatar=no | 1360×48 | 170 | `1293:40991` (🔥  Home) |
| tree navigation | set | `1020:15986` | checkbox:boolean · left icon:boolean · chevon:boolean · sub text:boolean · right icon:boolean · Level=Child 3\|Parent\|Child 1\|Child 2 · State=active\|default\|hover | 300×36 | 167 | `1022:25987` (-> Organization Management) |
| _calendarCell | set | `1375:253438` | state=default\|focus\|disable · type=month\|week | 187×106 | 158 | `1393:104315` (🔶 Local components) |
| Menu-item | set | `2343:119138` | Active=OFF\|ON · Name=Basic\|Business\|Customer\|Home\|Marketing\|Product\|Public\|Tools | 64×58 | 153 | `2736:344284` (-> Position Management) |
| Frame 1321315509 | set | `2736:344271` | Expand=OFF\|ON · Menu=Basic\|Business\|Customer\|Home\|Marketing\|Product\|Public\|Quản trị HO\|Tools | 80×1080 | 100 | `2736:328986` (-> Position Management) |
| _selectButton | set | `1335:192615` | state=selected\|focus\|default · -> align=left\|right | 32×32 | 79 | `1335:203572` (🔶 Local components) |
| Radio button | set | `1245:60106` | isShowButton:boolean · active=no\|yes · disable=no\|yes · type=2\|1 | 79×52 | 75 | `1245:60473` (🔶 Local components) |
| data | component | `1545:160862` |  | 112×50 | 68 | `1979:422135` (🔥  Home) |
| To do list | set | `1405:324002` | isShowButton:boolean · Checked=yes\|no | 251×44 | 60 | `1443:57531` (🔥  Home) |
| _inputLookup | set | `1004:41857` | Size=32\|36 | 447×51 | 57 | `1030:88865` (🔶 Local components) |
| bottom action | component | `1547:148436` | Slot:slot | 556×60 | 44 | `1979:384887` (🔥  Home) |
| step | set | `1075:118434` | type=1 | 1288×52 | 31 | `2086:468870` (🔥  Home) |
| Icon/base | component | `82:18889` |  | 16×16 | 30 | `1342:277336` (🔥  Home) |
| Illustration | set | `496:83607` | Property 1=Empty Inbox\|No Credits | 120×120 | 29 | `2193:237974` (🔥  Home) |
| _uploadCTA | set | `974:215810` | bodyText:text · state=Default\|Hover\|Focus\|Active\|Disabled\|icon | 350×56 | 27 | `1543:98882` (📂   Marketing Management) |
| _tabNavigation | set | `893:15233` | active=no\|yes · end=no\|yes | 73×34 | 24 | `893:15245` (🔶 Local components) |
| tab | set | `563:45783` | active=no\|yes · end=no\|yes | 82×34 | 24 | `569:49003` (📂 Product management) |
| _timeCell | component | `1398:309020` |  | 359×1 | 22 | `1398:309101` (🔶 Local components) |
| Line | set | `1073:116602` | active=no\|yes · oriental=horizontal | 48×4 | 20 | `1075:117088` (🔶 Local components) |
| tab navigation | set | `569:49000` | tab=3 | 1360×42 | 20 | `1293:40992` (🔥  Home) |
| Filter | set | `453:55508` | Tab:boolean · Type=Default | 1320×44 | 20 | `1248:26110` (-> Product Shelf Management) |
| Brand / MB / MB (Logo + Text)/Normal | component | `435:32255` | text:boolean | 60×24 | 19 | `569:55707` (🔶 Local components) |
| Top Title | set | `864:17192` | State=Level 2\|Level 3 | 1312×78 | 19 | `1401:61263` (🔥  Home) |
| line | component | `1020:16060` |  | 20×36 | 18 | `1025:67015` (🔶 Local components) |
| Form | component | `2980:175244` |  | 308×74 | 17 | `2980:175245` (🔥  Home) |
| _badge | set | `1393:98745` | color=sky\|yellow\|orange\|green\|purple\|pink\|ocean\|red\|cyan\|gray · state=default\|hover | 51×22 | 16 | `1393:104301` (🔶 Local components) |
| Form | component | `2980:175541` |  | 308×46 | 15 | `2980:175542` (🔥  Home) |
| table | set | `453:55574` | type=Default | 990×544 | 13 | `1248:26137` (-> Product Shelf Management) |
| item_step | set | `1073:116529` | Property 1=default\|done\|error\|inprgress\|wait · Size=L\|S | 24×24 | 12 | `1075:117089` (🔶 Local components) |
| chevron | set | `1022:25000` | type=def | 20×20 | 12 | `1022:25007` (🔶 Local components) |
| _eventChip | set | `1369:244096` | Type=cyan\|ocean\|yellow\|green\|gray\|red\|orange\|pink\|sky\|purple · Orientation=Horizontal\|Vertical | 85×18 | 9 | `1375:253249` (🔶 Local components) |
| _menu | set | `1348:142932` | active=yes\|no | 64×58 | 8 | `1349:172402` (🔶 Local components) |
| linePresent | set | `1402:310998` | active=yes\|no | 178×8 | 8 | `1402:311082` (🔶 Local components) |
| Activity Tag | set | `1443:97070` | Activity=Phone Call\|On-site visit\|Zalo\|SMS · Disabled=OFF\|ON | 115×22 | 8 | `1444:8699` (🔶 Local components) |
| body | component | `1158:204108` |  | 901×822 | 8 | `1158:204203` (->  Customer Contact) |
| Calendar | set | `1402:311121` | type=week\|month\|day | 936×605 | 7 | `1444:78250` (🔥  Home) |
| body | component | `1138:79819` |  | 1840×1080 | 7 | `2736:343697` (-> Position Management) |
| overlay | component | `1099:56287` |  | 1440×825 | 7 | `1099:56288` (-> Survey Groups) |
| _chipItem | set | `1059:61052` | Type=gray\|green\|cyan\|blue\|yellow\|orange\|pink\|purple | 57×22 | 6 | `1059:61092` (🔶 Local components) |
| _event | set | `1375:253267` | events=>3\|0\|1\|2\|3 | 164×165 | 6 | `1375:253269` (🔶 Local components) |
| Drawer | component | `1170:122573` |  | 459×820 | 6 | `1170:122578` (->  Customer Contact) |
| _chipGroup | component | `948:16902` | Slot:slot · Slot 2:slot · Slot 3:slot · Slot 4:slot · Slot 5:slot · Slot 6:slot | 359×30 | 5 | `1059:61207` (🔶 Local components) |
| Icon/pro | component | `82:18985` |  | 16×16 | 5 | `1342:277474` (🔥  Home) |
| Frame 1321315449 | component | `1548:190925` |  | 901×732 | 5 | `1548:190953` (📂   Marketing Management) |
| body | component | `1098:37040` |  | 1840×1080 | 5 | `2736:341942` (-> Position Management) |
| body | component | `1103:113452` |  | 1840×1080 | 5 | `2736:342152` (-> Position Management) |
| _date | set | `1375:246225` | type=default\|disable\|active\|today | 164×24 | 3 | `1375:246278` (🔶 Local components) |
| Frame 1321315449 | component | `1389:31479` |  | 1360×1980 | 3 | `1389:31497` (🔥  Home) |
| Icon | component | `869:19709` |  | 16×16 | 3 | `1875:228904` (->  My Customers) |
| Frame 1321315498 | component | `1719:110056` |  | 1312×598 | 3 | `1758:203377` (->  My Customers) |
| body | component | `1519:1551` |  | 901×822 | 3 | `1519:2113` (->  My Customers Groups) |
| Frame 1321315449 | component | `1540:86942` |  | 901×732 | 3 | `1540:86948` (📂   Marketing Management) |
| body | component | `1548:203503` |  | 1360×1106 | 3 | `1580:397612` (-> Scenerio Management) |
| body | component | `1158:184402` |  | 1360×822 | 3 | `1158:185821` (->  Customer Contact) |
| body | component | `1227:122239` |  | 1840×1080 | 3 | `2736:343704` (-> Position Management) |
| body | component | `1444:76084` |  | 1360×2188 | 2 | `1444:76087` (🔥  Home) |
| body | component | `1273:283537` |  | 1360×822 | 2 | `1552:55814` (->  Customer Deployment) |
| body | component | `1548:199645` |  | 901×1536 | 2 | `1548:199648` (📂   Marketing Management) |
| Management | component | `1030:90139` |  | 1440×822 | 2 | `1268:130156` (-> Permission Management) |
| time | component | `1398:309011` |  | 359×1 | 1 | `1398:309015` (🔶 Local components) |
| Frame 1321315449 | component | `1302:117532` |  | 901×732 | 1 | `1302:118322` (🔥  Home) |
| Frame 1321315449 | component | `1342:295382` |  | 901×732 | 1 | `1342:295388` (🔥  Home) |
| Group 639 | component | `2990:133111` |  | 1248×404 | 1 | `2990:137448` (🔥  Home) |
| body | component | `1254:257424` |  | 901×822 | 1 | `1254:258782` (->  Customer Allocation) |
| body | component | `1270:276418` |  | 901×822 | 1 | `1564:206232` (->  Customer Application) |
| Menu | set | `817:73181` | channel=no · expand=no | 80×822 | 1 | `817:73212` (📂 Product management) |
| Component 1 | set | `475:49174` | channel=no · expand=no | 80×822 | 1 | `860:71372` (📂 Product management) |
| list | component | `1004:39048` |  | 316×200 | 1 | `1004:39094` (-> Organization Management) |
| body | component | `1152:18367` |  | 1840×1080 | 1 | `2736:343700` (-> Position Management) |
| Frame 1321315449 | component | `1157:153098` |  | 1840×990 | 1 | `2736:343710` (-> Position Management) |
| Radio button / group | component | `1245:60589` |  | 882×36 | 0 |  |
| Anchor / Elements | set | `1245:61293` | checkbox:boolean · left icon:boolean · chevon:boolean · sub text:boolean · right icon:boolean · Level=Child 3\|Child 1\|Child 2 · State=selected\|default\|hover | 306×36 | 0 |  |
| tab navigation | set | `893:15242` | tab=1\|3\|n\|action list | 860×42 | 0 |  |
| step_item | set | `1075:117130` | Caption:boolean · state=wait\|inprogress\|error\|done · type=1\|2\|3 | 128×72 | 0 |  |
| _illus | set | `1353:201025` | type=upload\|empty\|404\|no task\|no noti\|no calendar\|search | 100×100 | 0 |  |
| _popup | component | `1335:198651` | filter:slot | 1288×286 | 0 |  |
| Zalo Tag | set | `1444:9718` | DIsabled=ON\|OFF | 16×16 | 0 |  |

## B2. CRM-HR-WEB — thư viện ngoài chưa publish — chỉ dùng trong CRM-HR-WEB qua instance mẫu

Không import được theo key (REST 404/403). Lấy bằng `getMainComponentAsync()` từ instance mẫu rồi `createInstance()`. Prop = giá trị quan sát được trên các màn.

| Tên | Key | Prop quan sát | Cỡ mẫu | Dùng | Instance mẫu |
|---|---|---|---|---|---|
| table-cell | `a660ee00e7d01f95d0a26a3a9e665f7d4b272eeb` | Container:slot · State=Default\|action · Type=Checkbox\|Chips\|Dropdown\|Input\|Name\|No\|Photo\|Radio\|Slot\|Text\|Toggle\|Yes\|tag | 56×50 | 45729 | `1297:96580` (🔥  Home) |
| table-header | `588bce72032319fb7a4138f60f99b66477ebbc57` | Show Checkbox:boolean · Show Text:boolean · Show filter:boolean · filter:slot · icon list2:slot | 56×44 | 5836 | `1297:96578` (🔥  Home) |
| Table-Cell | `6648042e40f5240004093d68309961da9fa38541` | type=checkbox\|currency\|date\|input\|number\|tag\|text\|text link | 56×50 | 3880 | `1342:277488` (🔥  Home) |
| Table-Cell/Body/Content | `c6f40ddb6aebdbcf5ee709cade466bb38afc99e1` | Text:text · Type=1 dòng | 57×56 | 920 | `2736:335000` (-> Position Management) |
| Tab / Line | `df01e8ac2a162928761c3efb869a7a90a6ad485c` | isShowBadge:boolean · isShowIcon:boolean · state=active\|inactive · title:text | 172×36 | 528 | `1355:230806` (🔶 Local components) |
| Tab / Solid | `bd97cc00fad484f683e2aacc6a785a451ffe5a7f` | isShowBadge:boolean · isShowIcon:boolean · level=2 · size=S · state=active\|inactive · title:text | 110×36 | 442 | `1342:292308` (🔥  Home) |
| tab navigation | `0768346e2f82311a060070b52d325f0ce4ea5a46` | tab=3 | 1360×42 | 440 | `1302:113819` (🔥  Home) |
| Filter | `a0c293e0e61d5eff225e35eeb4cc3a7fdddfba6c` | Size=20 | 20×20 | 422 | `1342:277484` (🔥  Home) |
| sort | `6958d5aedc0b49d956de36d0f26ec076b2b5fd7f` | Property 1=Default | 20×20 | 422 | `1342:277486` (🔥  Home) |
| Anchor / Elements | `1e86731b0144c99e78cad5edffca9ac0680cf129` | Level=Child 1 · State=default\|selected · checkbox:boolean · chevon:boolean · left icon:boolean · right icon:boolean · sub text:boolean | 322×36 | 384 | `1757:164792` (->  My Customers) |
| .Base/S/Open | `6aca0476b8c83d8c54149d4aa8ca4d65c355e6db` |  | 284×28 | 360 | `1867:150809` (->  My Customers) |
| Switch | `0ca7bfdf233ee5966e7bea983d9fbcb35fc73ad4` | Size=Medium · State=Default · isChecked=False\|True · isDisabled=False | 40×24 | 347 | `1540:83251` (📂   Marketing Management) |
| [Display] Title | `1a0d2f7ac0de67095fbd5df8853d3df0307d731e` | Prefix:instance_swap · Sub:text · Suffix:instance_swap · Title size=M\|XS · Title:text · isShowPrefix:boolean · isShowSub:boolean · isShowSuffix:boolean | 26×18 | 253 | `1089:150778` (🔶 Local components) |
| Search | `b39ed6827a9c5fa1a370d8cc7e6403c71df5a41e` | Caption:boolean · Size=S\|XS · State=Default\|Disabled\|Error\|Filled\|Focused\|Read-only · Title:boolean · iShowTitle=True · isShowCaption=True | 320×36 | 239 | `1068:90385` (🔶 Local components) |
| Input (S) | `73607028bedde9b5199aaad931040560196560aa` | Label=false · Leading Element=false · Secondary Label=false · State=Filled · Status=None · Supportive=false · Trailing Element=false · Type=Clearable | 300×24 | 235 | `1444:78238` (🔥  Home) |
| .Base/S/Closed | `34071dc2fa1f7b130703bd82a31b81d02c6cbde3` |  | 284×28 | 225 | `1867:150807` (->  My Customers) |
| Table-Cell/Header/Text | `5992710fd9619f87dfbd9bdea54aed640ae606a3` | P1=Header · Property 1=Header · Required:boolean · Show Filter:boolean · Show sort:boolean · Size=12px\|14px · Sort=No · Text=12px\|14px · state=default · type=text | 57×64 | 216 | `2736:334999` (-> Position Management) |
| _ActionItem/Primary | `93fecb9e325aad0f15d9829924e5a8fa0c06342d` | Show checkbox:boolean · Show left icon:boolean · Show right icon:boolean · Show switch:boolean · Size=S · Slot 2:slot · Slot 3:slot · Slot 4:slot · Slot:slot · State=active\|default | 230×38 | 91 | `1706:50371` (->  Potential Customer) |
| [Display] Supporting text | `c737b87e1d408869ec9cea6e6c6998d81ad8cbd2` | Kind=S · isShowIcon:boolean | 320×18 | 83 | `1658:117685` (->  My Customers Groups) |
| Section frame | `441bedfe05aed31b69628a456e1fd0d1bc7ac83b` | Handoff Checklist:boolean · List luồng nhỏ:boolean · Show Logo:boolean · Size=S · Title:text · Type=Local Component\|UI Flow | 1200×8773 | 71 | `1374:323727` (🔥  Home) |
| Text Field/Label | `14a04cc6cf1c556fa2bd367bdc1451734719cab4` | helper text=no · icon=no · require=no · size=L\|S | 26×16 | 63 | `2736:334902` (-> Position Management) |
| _CheckboxBase | `120eb64031ac32b1749046fc3bd2dcfe65715a37` | isChecked=False\|True · isDisabled=False · isIntermediate=False · size=Small · state=Default · validationState=None | 16×20 | 55 | `453:54922` (📂 Product management) |
| .internal_VariantProper | `586c619d631f2f07d18520f3e15d79f7a607f86c` | direction=Horizontal\|Vertical · propName:text · propValue:text · showPropType:boolean | 81×204 | 49 | `1245:11425` (🔶 Local components) |
| Button | `4e490c279c5d387b628314e2fbce3e252b8d5f1d` | Class=Standard · Content=Icon Only\|Left Icon\|Text Only · Icon (20px):instance_swap · Icon (24px):instance_swap · Size=12/24\|12/32\|12/36\|Large\|Small · State=Default\|Disable · Text:text · Type=Ghost\|Outline\|Primary\|Seconda | 101×36 | 45 | `2736:334529` (-> Position Management) |
| Icon button/32px/Edit | `ef20831b832e6a6fb69fd20a1ccbef74b55d1f4e` |  | 32×32 | 45 | `2736:338313` (-> Position Management) |
| Component 1 | `114ed0e6336e3f73077f43628f650b4e94ceb57b` | channel=no · expand=no | 80×822 | 44 | `2114:108926` (🔶 Local components) |
| .Base/S/None | `47994e04898866a57f21185af2f9003e61cbb33e` |  | 178×28 | 40 | `1600:52805` (-> Product Shelf Management) |
| Input Dropdown  | `26cc3e2b77534b621902c37f71c6831c61f6acd0` | Size=12\|16\|Medium · State=Disabled\|Filled · Text Placeholder:text · swap=no | 291×36 | 39 | `2736:334525` (-> Position Management) |
| Text Field/Text | `d4564a8a14957e23af31297119f37c4075ff1eee` | Size=L\|S · Text=normal · password=no | 96×18 | 35 | `2736:334905` (-> Position Management) |
| Status/Warning | `05786443a8750389c238a705b630bd83aba35a4f` |  | 24×24 | 35 | `2736:334907` (-> Position Management) |
| Navigation/Arrow-down | `db82a2d62918e216c68412efb88926931bfdbbd8` |  | 24×24 | 32 | `2736:334908` (-> Position Management) |
| Filter | `0051d9c5c1ecedb6b6855d650fb702680b943e4a` | Tab:boolean · Type=Default | 1312×48 | 31 | `1540:70758` (📂   Marketing Management) |
| legend | `944b7bf2ababee01038727aa9209301acbe586e8` | active=no | 351×24 | 28 | `2736:334561` (-> Position Management) |
| Pagination Item | `e7693e4a14687cc1d92a709bd2e30c00ce8bcc58` | State=Active\|Default\|Disabled · Type=Number\|Pagination-Next\|Pagination-Previous | 32×32 | 28 | `2736:335606` (-> Position Management) |
| Text Area | `b1b5314fb06aa12c2e6e7de62d90687afc14d338` | iShowTitle=True · isShowCaption=True · size=S · state=Default\|Disabled\|Error\|Filled\|Focused\|Read-only | 320×120 | 27 | `1030:88866` (🔶 Local components) |
| Location | `1e7201bff2451fa0e7332da475c51552f2fb1b9a` |  | 12×12 | 21 | `2736:336418` (-> Position Management) |
| Tablet / Salekit / Menu | `b81cc06bf452f225c701c4387ee7c06fcfe32965` |  | 298×72 | 21 | `2736:341267` (-> Position Management) |
| Master/Standard Button | `2f0655057da60ab37c583f9dc565675b73b65186` | Label:text · icon left:instance_swap · icon right:instance_swap | 76×32 | 19 | `1665:141244` (🔶 Local components) |
| Dropdown | `8fb0ff20d0a7dff8b291eb6c7693182be5b799ae` | Show Label:boolean · Size=Large\|Small\|Xsmall · State=Default\|Filled | 424×76 | 19 | `2736:336041` (-> Position Management) |
| Input / Normal | `e878883a42104e0c169b4f25715a086dd388b75d` | iShowTitle=True · isShowCaption=False\|True · isShowLeadingIcon=False\|True · size=S · state=Default\|Disabled | 421×58 | 18 | `1201:56463` (-> User Management) |
| Anchor | `0aaa96ea35b4ad1272833005966d5a3841f4ac02` |  | 149×432 | 17 | `1245:61376` (🔶 Local components) |
| tag | `eecf3dbc67944b6bc9befd77391a2d2d2e27a684` | active=no · infor:boolean · quantity:boolean | 112×34 | 17 | `2736:338806` (-> Position Management) |
| Linear/ Notice | `e8a87df552745f1a781cc5a006c538878a7a7a64` |  | 16×16 | 16 | `448:53068` (📂 Product management) |
| _stepElements | `1de8541392e52b219d6a50d48691be3f898e93c7` | Caption:boolean · state=inprogress\|wait · type=1 | 393×24 | 15 | `2990:131819` (🔥  Home) |
| Scroll Bar | `a970b20a374cb832edfed183a20efe65a7ef82b1` | Trạng thái=Mặc định · Type=Dọc\|Ngang | 6×500 | 15 | `1710:31297` (-> Product Shelf Management) |
| Table-Cell/Body/Status | `3aa30861dd35c9194af5935d8e2c73550b346ebf` | Trạng thái=1\|2\|3\|4\|5 | 150×56 | 14 | `2736:339587` (-> Position Management) |
| Icon button/36px/Row-Expand | `e2dfe9dbddb570873f1971c765940c2c3b30ba7f` |  | 28×28 | 13 | `2736:335010` (-> Position Management) |
| Master/Standard Button | `cab93aa973476094ddb7d08b8e32c026754bb1d7` | Label:text · icon left:instance_swap · icon right:instance_swap | 82×36 | 12 | `1758:203245` (->  My Customers) |
| Label | `c4a491f731608bf75ee8e5f71f4e7a762c6cbbb5` | Info:boolean · Label Text:text · Required:boolean · Size=16\|Large | 227×24 | 11 | `2736:334614` (-> Position Management) |
| menu | `f3e1c5d8cc0cce69ea37f69af7e31fdcc9456419` | Property 1=active\|default | 68×78 | 11 | `2736:344909` (-> Position Management) |
| M Input / Search | `a3e68cf1cb5496f2a856cc38948e09e896cfe749` | Show Dropdown Menu:boolean · Show Guide:boolean · Show Item L:boolean · Show Item R:boolean · Show Title:boolean · State=Default | 360×48 | 10 | `893:15315` (🔶 Local components) |
| M Button / Tertiary | `035a146be7cf166231c89f46e2776fff6805b625` | Label:text · Show Item L:boolean · Show Item R:boolean · Size=L · State=Default · ↳ Item L:instance_swap · ↳ Item R:instance_swap | 141×48 | 10 | `893:15316` (🔶 Local components) |
| spacing / m | `55537c15185f621f4372a509ff0675af089fa89c` |  | 16×64 | 10 | `893:15317` (🔶 Local components) |
| M Button / Icon | `a12fef617a85afd63e9a3536e5faa2e52371940f` | Label:text · Show Label:boolean · Show Shadow:boolean · Size=L · State=Default · Type=Light · ↳ Item:instance_swap | 48×48 | 10 | `893:15318` (🔶 Local components) |
| A Divider | `8f77809775247563a44d4bef61754ec431b0a6eb` | Spacing Bottom:boolean · Spacing Top:boolean · Style=Line · ↳ ◇ Spacing Bottom:instance_swap · ↳ ◇ Spacing Top:instance_swap | 24×48 | 10 | `893:15319` (🔶 Local components) |
| dot | `bd2d1908d7cb222f0499fbe5ed902040315cafeb` |  | 24×24 | 10 | `2736:334590` (-> Position Management) |
| value | `7be635c92528cf035f16618b912c4c2c3eac728a` |  | 49×24 | 10 | `2736:334593` (-> Position Management) |
| tag | `76b861578ac0b21feea2134d98683eddc748fe72` | type=gray\|green\|purple\|red | 88×26 | 10 | `2736:335041` (-> Position Management) |
| Text Field | `470625e194b38f6b589ec20583a91ed0016f9d70` | Content=Text · Show Label:boolean · Size=Large\|Small\|Xsmall · State=Default | 576×58 | 10 | `2736:335774` (-> Position Management) |
| Frame 40623 | `a19764d43dc6d59fdbe94afd0999bf7468ca3708` |  | 1855×56 | 10 | `2736:345332` (-> Position Management) |
| Frame 40644 | `186aa4822a753329e2f32399ecf1fe2946260aaa` |  | 1495×56 | 10 | `2736:345364` (-> Position Management) |
| .intermal_header | `df57ef038a42f3ed7c510b38f003a520acdd2499` | isShowDescription:boolean · isShowImage:boolean · isShowMetadata:boolean · mode=dark | 992×258 | 9 | `1245:11416` (🔶 Local components) |
| Brand / MB / MB (Logo + Text)/Normal | `36aa097e3b0a2f7b5ef6f8874bec9b3b406caaea` | text:boolean | 84×34 | 9 | `1630:40248` (🔥  Login) |
| Checkbox_round | `b83ed110f6f7cd3d9a3b9594fc511aeabf082a4d` | Property 1=Active\|Default | 16×16 | 9 | `2736:336408` (-> Position Management) |
| Checkbox_item | `26060d4116b4c961cef407783a46ebbb2360fde9` | Selected=No\|Yes · Show Box:boolean · Show Content:boolean · State=Default · Text Content:text · size=24 | 24×24 | 9 | `2736:338854` (-> Position Management) |
| Text Field/Content | `97c21bba6e6eceb2199fe5ff88cc0405265c402b` | Button=no · Size=S · icon left=no · icon right=yes | 174×24 | 9 | `2736:344944` (-> Position Management) |
| _datePicker/elements/primary | `78a554a63b38487acec817057e2a5ed59e257e68` | -> Position=middle · Icon:boolean · Show Chọn Tháng - Nă,:boolean · State=Active\|Default\|Disable\|Today · Today:boolean · Type=Single date | 24×24 | 8 | `1375:246177` (🔶 Local components) |
| table | `051bfd837b161b06b2e0b5cc4208fdcb39a6d83a` | type=Default | 990×2 | 8 | `1248:26136` (-> Product Shelf Management) |
| Flow Header | `77519f6e66e99014c1d4c1d1394d074b0d12e335` | Flow Name:text · Size=M | 9376×229 | 8 | `2736:329718` (-> Position Management) |
| Chip | `525958c26552bd6961a1f23b2ee0269dbc7c5cdd` | state=default | 135×26 | 8 | `2736:334617` (-> Position Management) |
| Pagination | `de062329c81a14ff2e248a52aed20b2a71ce2732` | State=Default | 1792×68 | 8 | `2736:334642` (-> Position Management) |
| Button / Search / IconText | `10454c950579d2affc55a3fbdb7109e611d37295` |  | 85×34 | 8 | `2736:335294` (-> Position Management) |
| Icon button/36px/Delete-secondary | `9cc31634c9a614dd09f1101957657dd0f1048d2c` |  | 32×32 | 8 | `2736:338314` (-> Position Management) |
| Table | `ff25523c6c6b9109155395c1cf9c4914dbdad2dd` | P1=Status · Type=Cell | 150×56 | 8 | `2736:340651` (-> Position Management) |
| Input Search | `84d2b5dbf825dbcfc93f3f2dfcd121e704b58367` | Size=12 · State=Default · Text Content:text · swap=no | 477×36 | 7 | `2736:334527` (-> Position Management) |
| cached | `49ec88aa61718a4aa8e75ec0fe36541fc5aea779` |  | 20×20 | 7 | `2736:338911` (-> Position Management) |
| Component 1/no/no | `98f374d87447fb1da3900ea572b28602de523acd` |  | 80×822 | 6 | `2736:329337` (-> Position Management) |
| Input Date | `aec86c64741595cb6b0af08bacb0d932d0ec1538` | Date Range=No · End Date:text · Error message:text · Size=12 · Start Date:text · State=Default · style=1 · swap=no | 576×36 | 6 | `2736:335292` (-> Position Management) |
| Button icon/Primary/Excel Export | `c612317d2373f29a1b27051b21b38f40ef416ca3` |  | 36×36 | 6 | `2736:335297` (-> Position Management) |
| Link | `9518091119491d350ff2c8e8614322567b088f04` | color=Primary · icon:instance_swap · iconLeading:instance_swap · iconOnly=False · iconTrailing:instance_swap · isDisabled=False\|True · label:text · size=Medium · state=Default\|Focus\|Hover · type=Action\|Anchor · ↩ trailin | 48×22 | 5 | `974:215817` (🔶 Local components) |
| State | `6a1a85cfc6f0dc7da5a30d81cec4d5e484cd7ce0` | Active=No\|Yes | 115×42 | 5 | `2736:336383` (-> Position Management) |
| Frame | `d7a2074a591ab1bada64639424440299d6284f22` | Property 1=Default\|Layer_1 | 16×16 | 5 | `2736:338892` (-> Position Management) |
| Update | `21db6b5964fd2c6b48e078deac202e90312ca62e` |  | 32×32 | 5 | `2736:339594` (-> Position Management) |
| Frame 427319800 | `200ea70291aed811833068ee6e61a9fa0ee2ccf0` |  | 32×32 | 5 | `2736:339596` (-> Position Management) |
| spacing/s050 | `d36575879606937b886639f4021d5e2d68c2d6ad` |  | 8×8 | 4 | `1402:323972` (🔶 Local components) |
| Dashboard in list | `acbf9b0f04a0d1087bc12f88d5711acd321c190b` | expand=yes | 1788×224 | 4 | `2736:338039` (-> Position Management) |
| table title | `d1e33a848b31541d13a3391ed8dc7ae5dfa3c9a0` |  | 1788×68 | 4 | `2736:338041` (-> Position Management) |
| star | `8ed03f0081dea2965f9bae2862e9a59d82506e2f` | Style=Outlined | 16×16 | 4 | `2736:339030` (-> Position Management) |
| .deprecated-pattern | `feb883a006152e8dc8a93da2d7203a7bcd490124` |  | 187×114 | 3 | `1398:309014` (🔶 Local components) |
| _tabItems | `760b3bb324107aa884ba24a640a151a470d63920` | Content:text · Prefix:instance_swap · Size=S · Surfix:instance_swap · isShowBadge:boolean · isShowLeadingicon:boolean · isShowLine:boolean | 146×36 | 3 | `1342:315341` (🔥  Home) |
| Scroll Bar with Pagination | `2d11aadad33b8537601d34b86d8d897bec1a3717` |  | 1760×50 | 3 | `2736:335188` (-> Position Management) |
| Pagination | `0bc4d91aee16733da7e4c7997b155977fedc4954` |  | 272×32 | 3 | `2736:336079` (-> Position Management) |
| Linear/ Arrow-left | `8403a56abd60816bb349718afffb1f1f7f78c803` |  | 16×16 | 3 | `2736:336315` (-> Position Management) |
| Tab | `5259291d526be6c236abe819c58172dbe3563cd2` | Type=2 Tab\|3 Tab\|5 Tab | 580×42 | 3 | `2736:336839` (-> Position Management) |
| chip 2 | `d6288d2e3ee306b8aef427d791918a4c7570e74e` | active=no · infor:boolean · quantity:boolean | 98×34 | 3 | `2736:338792` (-> Position Management) |
| Button / Search / IconText | `d7e98cdea8cbd8affcd39921ecc50b62824a942e` |  | 165×40 | 3 | `2736:340749` (-> Position Management) |
| Tablet / Button / Text Rest | `8788bf53db2b452999719f59aecff958005731e7` |  | 232×60 | 3 | `2736:341252` (-> Position Management) |
| Component 7 | `bd55eabfbfb98252e1d8463daedadf14c4b5ba43` | Property 1=sort-ascending\|sort-descending | 24×24 | 3 | `2736:345344` (-> Position Management) |
| Checkbox | `af9703decdb58ee962b74a116a7f884a2b69e2fa` | Selected=No · Show Box:boolean · Show Content:boolean · State=Default · Text Content:text · size=16 | 205×24 | 3 | `2736:345345` (-> Position Management) |
| .internal_sectionHeading | `f3c91691de00fe8753ab5067d0a008a0ef44cf36` |  | 832×133 | 2 | `1245:11557` (🔶 Local components) |
| Input | `81a6807ee4a2a282366a82934973f49153045bae` | Feedback=None · Hint=No · State=Default · Type=Regular\|Right Icon | 311×64 | 2 | `1724:31443` (🔥  Login) |
| Elements | `ff900fc618d0537314b2fc2ed8a7d294731fd689` | Element=Element 2 | 167×167 | 2 | `1724:31491` (🔥  Login) |
| Icon/pro | `b8737b2232db8a49f7f1245c99e6b2171b918408` |  | 16×16 | 2 | `1762:28920` (-> Product Catalog) |
| Linear/ Close | `208431a97bd3692c6e245511f564d1692288b66d` |  | 24×24 | 2 | `2736:334948` (-> Position Management) |
| Radio Button | `38112c54e7c406b7a6ad686ceb92ef9aedb0b85a` | Selected=No\|Yes · Show Radio:boolean · Show Text:boolean · State=Default · Text Content:text | 71×24 | 2 | `2736:336052` (-> Position Management) |
| Linear/ Add | `419de0f5f9463eb1d205864bd1e39dc326a884a5` |  | 24×24 | 2 | `2736:336379` (-> Position Management) |
| Color Base | `14bafea8cc50bf7b39786a4d78e2d30fd4102159` |  | 16×16 | 2 | `2736:336394` (-> Position Management) |
| text | `b606624b4f714d26c93d6ae9bbf8a1db37385db6` |  | 202×18 | 2 | `2736:338684` (-> Position Management) |
| filter | `d2cd050f1360212a042ee66834fad88c79502726` | Active=OFF | 326×36 | 2 | `2736:338785` (-> Position Management) |
| Tabs | `70542b0b1e8fb8a4adda7f863154cd69cc668263` | P1=Active\|Default | 182×40 | 2 | `2736:340537` (-> Position Management) |
| Date Field | `5d2915f429278ec5aa5abeb1b4dca0946057d956` | Date Range=No · Show Label:boolean · Size=XSmall · State=Default | 421×64 | 2 | `2736:340732` (-> Position Management) |
| Add icon | `92f0138e67921226afdbd01d0ee7b5b1a8f7572f` |  | 40×40 | 2 | `2736:340759` (-> Position Management) |
| Tablet / Salekit / Menu Active | `dd57b8c8bffe7ead74483e9e14d001fe58db1bbc` |  | 298×72 | 2 | `2736:341268` (-> Position Management) |
| Tablet / Section / Title Calendar | `9e9296fe7f6d138dce239102f08e826b9797c93d` |  | 1175×80 | 2 | `2736:341303` (-> Position Management) |
| tab | `b28c9045ef778624442e33512b19ded814c3290b` | active=no\|yes · end=no | 58×34 | 2 | `2736:342755` (-> Position Management) |
| Tablet / Button / Charts | `bffbe33be92f098c9a3bc1a7b04af89c84b83daf` |  | 60×60 | 2 | `2736:345303` (-> Position Management) |
| Tablet / Button / Others | `f350f784d5ae83bf77203c6823afd8b813c6a394` |  | 60×60 | 2 | `2736:345304` (-> Position Management) |
| Elements | `1a75f9bb6dfd925ebd4432e761adebd474b5aaec` | Element=Element 3 | 631×631 | 1 | `1724:31257` (🔥  Login) |
| Button | `946caba9d27febab8726eb3eb526c3faae761873` | Property 1=blue · Property 2=no · Property 3=40px | 311×40 | 1 | `1724:31445` (🔥  Login) |
| Brand / MB / MB (Logo + Text)/Normal | `41799ae45cfc5844dbe1f0f35bdbe554fb7abf65` |  | 90×39 | 1 | `1724:31513` (🔥  Login) |
| Menu/no/no | `c54b33d9ae72ea61912e7855e45b979c7c472b62` |  | 80×822 | 1 | `817:73240` (📂 Product management) |
| Chips | `06c7e5616cae0c4670f76ffb3582792369f529c9` |  | 97×22 | 1 | `1600:52889` (-> Product Shelf Management) |
| filter | `5efed2557a51be2ac32252cfb23b5585da5747c6` | Property 1=Default | 105×36 | 1 | `2736:334530` (-> Position Management) |
| ChartGrid | `1f76ae0c4777fc51b7f7b30756a7e3b09f72f525` | State=Default · Type=Full | 559×276 | 1 | `2736:334540` (-> Position Management) |
| tooltip | `03400f1a3be60104126b792d5d59a0c6b3980eb7` |  | 163×54 | 1 | `2736:334564` (-> Position Management) |
| Mức độ ưu tiên | `757d8fecb61d9fe44f98f0d86fb5a900b080d640` | type=Default | 326×276 | 1 | `2736:334609` (-> Position Management) |
| tooltip | `4aeb854f12170abf0efd93e2c5fe2feeda70d012` | active=no | 16×16 | 1 | `2736:334628` (-> Position Management) |
| table - 6 tháng | `4bc33c3f998a739fd269bf5b3b62ad5f6e3efefb` | Property 1=RM | 1792×330 | 1 | `2736:334641` (-> Position Management) |
| Frame 280999 | `77db654b612849efcbc52e802a5fef51c84b0b8f` |  | 1760×34 | 1 | `2736:334996` (-> Position Management) |
| Frame | `bd8a93cfde08f005cad60b393b77976426525d78` |  | 24×24 | 1 | `2736:335675` (-> Position Management) |
| Linear/ Search | `6b1287917160220995f45713253ab1a32e9d49b4` |  | 20×20 | 1 | `2736:336045` (-> Position Management) |
| Linear/ Arrow-down | `e0c3b02ba174136b1b1f613b46aaf2780768c52a` |  | 16×16 | 1 | `2736:336078` (-> Position Management) |
| Scroll Bar with Pagination | `3ceb0544f8befcd3a33d3a50e9d74f898f1dac99` |  | 1792×82 | 1 | `2736:336234` (-> Position Management) |
| Tablet/ Icon/Product - TheMB1 | `1ac1cfcfd81b915777f04e48d2035585b54ebeee` |  | 32×32 | 1 | `2736:336261` (-> Position Management) |
| Frame | `63b6641359537dd2b42259b23a8accca31dd7f2c` |  | 26×26 | 1 | `2736:336262` (-> Position Management) |
| CRM/bold/star | `5785c60dbc9b5f8a83edc7e37db72d411ae06601` |  | 28×28 | 1 | `2736:336323` (-> Position Management) |
| _icon-tong quan | `eb064db8c420c7264f5e308c635e71ccdf473292` |  | 26×26 | 1 | `2736:336336` (-> Position Management) |
| Linear/ Báo cáo | `cd86c661add8ba2e0a4402c176bb00c417c76136` |  | 24×24 | 1 | `2736:336374` (-> Position Management) |
| Linear/ Lịch | `f0655be81d2659ef8cd59c6b069632ffc47223a3` |  | 24×24 | 1 | `2736:336836` (-> Position Management) |
| Frame 1321315362 | `e6236ae73e52d7010fbb614166edd3b78d3ed2f5` |  | 580×46 | 1 | `2736:336863` (-> Position Management) |
| Frame 40614 | `15a3597c143085e8270613e64e85d383b5d6d57d` |  | 1114×214 | 1 | `2736:337315` (-> Position Management) |
| Icon | `4491c3671149b99070f084ba6bf24aeafc131d41` | Name=AngleUp | 20×20 | 1 | `2736:337325` (-> Position Management) |
| Frame 1321314329 | `bc4828fc25c9d85fc28fe1bebe2534520814b388` |  | 140×36 | 1 | `2736:338830` (-> Position Management) |
| Warning | `e3853a436580356c9950c7709c0a6cf2c932d947` |  | 1756×32 | 1 | `2736:338845` (-> Position Management) |
| Kênh | `5eab9c37b6302071ea66e9d4bc5ac69e9e34d735` | type=Default | 251×88 | 1 | `2736:339499` (-> Position Management) |
| Frame 1321315339 | `53ef4661743ec74c2dfb832765241e4dca3db549` |  | 401×168 | 1 | `2736:339502` (-> Position Management) |
| table title | `3f971c3e00ee6b35c28ceffdd0060904d1645618` |  | 1789×80 | 1 | `2736:339552` (-> Position Management) |
| Input / Resource / Search 1  | `fd8d461a0f3da642d19149326484461ebf3e817f` |  | 348×40 | 1 | `2736:340705` (-> Position Management) |
| Buttons / Plain / Outline / ActiveButton | `49b5dc25f6ca2915ea3a49d2b110cac9ec48011c` |  | 167×40 | 1 | `2736:340706` (-> Position Management) |
| Buttons / Plain / Primary / Ghost | `9d3ad4eee69a87b701e027c636a407b9f070bb4f` |  | 98×40 | 1 | `2736:340755` (-> Position Management) |
| Buttons / Plain / Primary / Active | `34fa34594a8a91068f66f27b55bda8250321cbe1` |  | 98×40 | 1 | `2736:340756` (-> Position Management) |
| Export Icon | `f2f0b4b05c6ecaf43597bddbe6e7db2633ea6dbe` |  | 40×40 | 1 | `2736:340758` (-> Position Management) |
| Button / Action / Edit | `a14902f51d3d70df7282148ac109f43dea34bc3b` |  | 40×40 | 1 | `2736:340760` (-> Position Management) |
| Salekit Title | `03f1d79d413f1741cd4c136a6c706eb6817afde3` |  | 1175×80 | 1 | `2736:341309` (-> Position Management) |
| Brand / MB / MB (Logo + Text)/Normal | `9a70297b257c14dd5e9cc38e868448b951e057d2` |  | 64×28 | 1 | `2736:344900` (-> Position Management) |
| Frame 40643 | `6205040ee4a0c0c1f6f26c20a1110e4f8ea574ae` |  | 1315×56 | 1 | `2736:345363` (-> Position Management) |
| _uploadCTA | `382faebc9dd07290d34e2acbdf1807f33ced8179` | bodyText:text · state=Default | 381×100 | 1 | `1682:175094` (-> Marketing Material Management) |

## Icon (thư viện Icon) — 96 icon đang dùng, tìm bằng `search_design_system` (lọc library key Icon)
