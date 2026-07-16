# Regional Culture Poster

![Version](https://img.shields.io/badge/version-v0.1.1-blue)
![Skill](https://img.shields.io/badge/skill-regional--culture--poster-6f42c1)
![Codex](https://img.shields.io/badge/Codex-supported-2ea44f)
![GPT Image 2](https://img.shields.io/badge/GPT%20Image%202-supported-00a3ff)
![Mode A](https://img.shields.io/badge/Mode%20A-structural%20character-orange)
![Mode B](https://img.shields.io/badge/Mode%20B-editorial%20poster-teal)
![Direct Generation](https://img.shields.io/badge/direct%20generation-preferred-brightgreen)

## Current update

MODE B now includes the final patch: city-specific background base colors, stronger but still legible regional title creativity, crafted boundary effects such as cut-paper/torn-paper/material-collage/embossed/architectural sectional edges, and stricter anti-repetition rules for batch series.

一个用于生成中国地域文化海报的 Codex Skill。它把省份、城市、县域、古城或文化区域转译成“一个主字 + 一个地方文化机制 + 一个克制版式系统”的当代视觉海报。

核心目标不是做旅游明信片，也不是堆地标，而是让地域文化变成可识别的结构、材料、空间和字形关系。

## 精选实例

以下图例来自本地生成批次 `D:\Codex_Outputs\exports\regional-20-text-removal-culture-image2`，包含随机样例和人工勾选样例。

| 苏州 | 西安 | 成都 |
|---|---|---|
| ![苏州](assets/examples/suzhou.jpg) | ![西安](assets/examples/xian.jpg) | ![成都](assets/examples/chengdu.jpg) |

| 北京 | 长沙 | 大理 |
|---|---|---|
| ![北京](assets/examples/beijing.jpg) | ![长沙](assets/examples/changsha.jpg) | ![大理](assets/examples/dali.jpg) |

| 大连 | 重庆 | 佛山 |
|---|---|---|
| ![大连](assets/examples/dalian.jpg) | ![重庆](assets/examples/chongqing.jpg) | ![佛山](assets/examples/foshan.jpg) |

| 桂林 | 杭州 | 呼和浩特 |
|---|---|---|
| ![桂林](assets/examples/guilin.jpg) | ![杭州](assets/examples/hangzhou.jpg) | ![呼和浩特](assets/examples/hohhot.jpg) |

| 嘉兴红船 | 景德镇 | 绍兴 |
|---|---|---|
| ![嘉兴红船](assets/examples/jiaxing-redboat.jpg) | ![景德镇](assets/examples/jingdezhen.jpg) | ![绍兴](assets/examples/shaoxing.jpg) |

| 沈阳 | 昆明 | 贵阳 |
|---|---|---|
| ![沈阳](assets/examples/shenyang.jpg) | ![昆明](assets/examples/kunming.jpg) | ![贵阳](assets/examples/guiyang.jpg) |

| 乌鲁木齐 | 上海 |
|---|---|
| ![乌鲁木齐](assets/examples/urumqi.jpg) | ![上海](assets/examples/shanghai.jpg) |

## 适合做什么

- 城市文化海报
- 省域 / 地域视觉系统
- 城市系列主视觉
- 展览 KV
- 文旅之外的高设计感地方文化表达
- 公众号、小红书、封面、出版物视觉
- 直接使用 GPT Image 2 生成完整成图

## 设计原则

## 两种模式

### MODE A：结构造字海报

汉字结构是主视觉。城市元素参与字形生长，适合“城市字体 / 大字 / 造字 / 一个主字”的方向。

### MODE B：地域编辑海报

城市空间是主视觉，城市名是编辑锚点。适合“杂志感 / 城市文化研究 / 图文丰富 / 不要只有大字”的方向。

MODE B 不把整张照片裁进大字里，而是先判断城市文化，再推导空间原型、裁切边界、图文比例和地域化字体细节。新版 MODE B 额外强化边界克制与主标题字体骨架差异。

### 1. 一个主字作为视觉骨架

优先使用一个地域凝练字，例如：

- 北京：京
- 上海：沪
- 重庆：渝
- 苏州：苏
- 泉州：泉
- 西安：秦

当单字会误导或过于抽象时，可以使用完整地名，例如“拉萨”“台湾”。

### 2. 遮字后仍应能识别地域

这是本 skill 的关键校验规则。

如果把城市名、主题、关键词都遮掉，画面里仍应有至少一个不可替换的地方文化机制，例如：

- 重庆：山城梯坎、桥柱、吊脚空间、江雾
- 泉州：红砖燕尾脊、骑楼、海丝寺庙门影
- 苏州：园林漏窗、白墙、水影、太湖石
- 嘉兴：红船、南湖、水院、粽叶
- 哈尔滨：冰砖、冬街、拱窗、雪光

玻璃、桥、水面、混凝土、雾、霓虹、天际线等通用现代元素只能辅助，不能单独作为文化证据。

### 3. 当代，不土，不旅游广告

默认避免：

- 旅游宣传海报
- 地标拼贴
- 民俗宣传板
- 非遗展板感
- 复古拓印
- 土黄旧墙
- 红金国潮模板
- 电影海报式城市夜景
- 商业地产 KV

优先使用：

- 冷灰、雾白、深绿黑、湿石、玻璃反射、金属边缘
- 局部红砖、木构、青瓷、冰蓝、湖绿等由地方材料自然带出的色彩
- 空间切口、门洞、廊柱、楼梯、桥墩、水面、墙体厚度、雨痕、阴影

### 4. 直接生成优先

当用户要求“直接出图”“不要合成”“用图像生成”时，本 skill 默认采用 direct mode：

- 一次生成完整扁平海报
- 图像、主字、排版、遮罩、空间关系同时生成
- 不做本地二次合成
- 不用浏览器
- 如果文字失败，优先整张重生，而不是局部修补

## 推荐输出目录

遵循当前 Codex 工作习惯：

- 图片：`D:\Codex_Outputs\images`
- 最终导出：`D:\Codex_Outputs\exports`
- Prompt / 过程稿：`D:\Codex_Outputs\drafts`
- 临时文件：`D:\Codex_Outputs\temp`

## 快速使用示例

用户可以直接说：

```text
用 regional-culture-poster 做 10 个城市，直接用图像生成，不要合成。
```

或者：

```text
做嘉兴，加入：红船启航地，嘉兴醉江南。
```

或者：

```text
南京这张看不懂，完整写上南京，但保持创意。
```

## 典型工作流

1. 分析地区文化候选池  
   地理气候、建筑结构、材料颜色、历史文学、日常生活、当代状态、精神气质。

2. 选定一个不可替换的地方机制  
   例如“红船 + 南湖 + 水院 + 粽叶”，而不是泛泛的“江南水乡”。

3. 选择主字  
   单字优先，完整地名作为可读性 fallback。

4. 写成 direct-generation prompt  
   包含主字、文化结构、版式、色彩、精确文案、负面约束。

5. 用 GPT Image 2 直接生成  
   推荐参数：`1024x1536`、`quality=high`、`background=opaque`、PNG。

6. 做遮字识别检查  
   如果遮掉文字后只剩通用城市材料，重写方向。

## 文件结构

```text
regional-culture-poster/
├─ SKILL.md
├─ README.md
├─ agents/
│  └─ openai.yaml
├─ references/
│  ├─ cultural-analysis.md
│  ├─ direct-generation.md
│  ├─ production.md
│  ├─ series-and-examples.md
│  └─ visual-system.md
└─ assets/
   └─ examples/
```

## 参考文件

- `SKILL.md`：主流程、路由规则、默认行为、校验门槛
- `references/cultural-analysis.md`：文化分析维度与反刻板印象
- `references/visual-system.md`：构图、字形、材料、色彩、禁忌
- `references/direct-generation.md`：直接生成模式的 prompt 结构
- `references/mode-b-editorial.md`：地域编辑海报模式，适合杂志感、图文层级、城市文化研究、边界克制和地域字体多样化方向
- `references/production.md`：生产模式选择
- `references/series-and-examples.md`：系列化去重与案例逻辑

## 维护重点

后续继续迭代时，优先改进这三件事：

1. 提高“遮字后地域识别”的强度。
2. 避免从“土味”过度修正成“通用商业 KV”。
3. 保持字形和文化机制的空间碰撞，而不是退回普通地名海报。
