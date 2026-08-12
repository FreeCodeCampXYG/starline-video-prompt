---
name: starline-video-prompt
description: Create director-grade, BFL FLUX 3-ready video prompts and multi-shot prompt packs for 5-20 second clips. Use when the user asks for 视频提示词, 导演级提示词, 20秒镜头提示词, FLUX 3 prompt, 即梦/Seedance 镜头设计, 二八法则分镜提示词, 首尾帧连续提示词, or wants to turn a topic, study notes, STAR story, project achievements, or storyboard into timed cinematic prompts. Do not use for browser clicking, API submission, video downloading, or ordinary editing-only tasks.
metadata:
  author: "澧点星痕 (starline)"
  version: "1.1.0"
---

# Starline Video Prompt

把抽象主题转成可生成、可剪辑、可接力的动态视频提示词；默认服务于 FLUX 3 的 5-20 秒片段，而不是写一段堆满形容词的静态画面描述。

## Router Rules

- 先确认目标是单镜头、连续多镜头，还是剪辑用的关键视觉素材。
- 优先读取用户提供的笔记、项目说明、脚本或画面参考；没有来源时，明确把事实性成果留给后期真实截图，不在生成画面里虚构。
- 需要真实 BFL 生成、Playground 自动填写、末帧提取或断点续跑时，转交 `$starline-flux-video-director`；本 Skill 只产出提示词与审查结果。
- 纯图片封面、已有成片剪辑、旁白润色，不触发本 Skill。

## Compact Workflow

1. 定义一句话视觉命题：观众要在画面中看见的变化，而非主题口号。
2. 区分 20% 不变量与 80% 可见事件：不变量锁定人物、服装、空间、光线、镜头方向；事件按秒写清可见因果。
3. 选择时长：5-8 秒只容纳一个动作；10 秒容纳 2-3 个节拍；20 秒容纳 4-6 个节拍且首秒必须发生事件。
4. 先让用户确认目标平台的提示词字符上限；未确认时，提供正常密度草案并明确标注“待确认上限”，不得擅自按 10,000 字符或任何其他上限扩写。确认后才决定精简版或接近上限的长版。
5. 写成英文生成提示词：结构为 `intent → invariants → camera → object physics → timed score → end frame → negatives`。生成画面不要求可读文字、真实 UI、GitHub 页面或字幕。
6. 连续多镜头时，把上一镜尾帧的构图、人物位置、光向、镜头方向、道具状态写成下一镜的起始锁定；相邻镜头一次只改变一个连续性变量。
7. 输出中文导演说明、英文可粘贴 Prompt、时长/参数建议、后期替换位与负面约束。若适用，运行 `scripts/validate_prompt.py --limit <用户确认值> --confirmed-limit` 检查长度与结构。

## 80/20 Prompt Rule

- 20%：只写能防止漂移的变量。一个人物、同一服装、同一空间几何、主光方向、焦段、机位与运动方向。
- 80%：按时间段描述触发原因、物理反应、主体动作、镜头推进和稳定尾帧。每 2-4 秒应有一个清晰可见的新阶段，而不是增加无意义粒子。
- 只有用户明确确认平台上限且要求长版时，才接近该上限；优先删掉重复负面词和声音细节，绝不删人物/空间/时间轴/尾帧契约。

## Output Contract

每次至少交付：

1. `视觉命题`：一句中文。
2. `镜头设计`：时长、节拍表、镜头运动和尾帧用途。
3. `English prompt`：可直接粘贴；必须标明“上限：用户确认 N 字符”或“上限待确认”，不得把假定值伪装成平台事实。
4. `参数建议`：模式、时长、画幅、分辨率、音频与安全级别；不含密钥。
5. `后期真实素材位`：何处替换为真实 GitHub、学习站或字幕。
6. `负面约束`：只保留和该镜头失败模式有关的约束。

## Quality Gates

- 不把“电影感、世界级、高清”当作镜头设计；每一镜必须有主体动作和物理因果。
- 不用生成的可读文字证明真实成果；涉及项目、提交、指标时，标注为后期叠加真实截图。
- 不为接近字数上限而加入相互矛盾的动作、镜头或风格。
- 20 秒镜头末尾至少稳定 1.5-2 秒，供提取末帧与衔接下一镜。
- 用户提供了人物参考图时，保留人物身份描述并建议使用其作为首帧；没有参考图时不声称可保证同一张脸。

## Boundaries

- 不调用 BFL API、不访问账户、不读取密钥、不点击网页按钮。
- 不生成虚假的 GitHub 提交、项目数据、品牌标识或可读 UI。
- 不声称提示词已经通过提供商质量验证；实际生成效果属于 `missing evidence`，需要人工审片。
