# Starline Video Prompt

## Install with npx

Install this skill for Codex, Claude Code, Cursor, and other supported agents:

```bash
npx skills add FreeCodeCampXYG/starline-video-prompt --skill starline-video-prompt --all
```

For a global user-level installation, add `--global`:

```bash
npx skills add FreeCodeCampXYG/starline-video-prompt --skill starline-video-prompt --all --global
```

为 FLUX 3、即梦/Seedance 风格工作流生成可直接使用的导演级视频提示词。它把“主题”拆成可控的镜头不变量和有节奏的可见事件，并把真实项目证据留给后期素材叠加。

## 适合的请求

- “把我的学习笔记做成 20 秒的 FLUX 3 提示词。”
- “按六段连续镜头写英文 Prompt，正文不要出现方法论标签。”
- “按 STAR 法则把 GitHub 项目做成一条技术纪录片视频。”

## 你可以直接这样说

- “把这份学习笔记写成一个有开场冲突和稳定尾帧的 FLUX 3 视频提示词。”
- “为我的 GitHub 项目设计六段连续镜头的英文 Prompt，每段 20 秒。”

## 不负责的工作

- 不点击 Playground、提交 API、上传素材或下载视频。
- 不负责剪映剪辑、配音、字幕烧录。

需要真实连续生成时，配合 `starline-flux-video-director`：本 Skill 先写 prompt，该 Skill 再负责首尾帧链与受控提交。

## 默认产物

每个镜头会得到中文节拍表、英文 Prompt、建议参数、真实截图替换位和必要负面词。内部会先锁少量防漂移变量，再把主要篇幅用于有因果的时间线；故事成稿默认不显示内部方法名。

## 本地检查

要求 Python 3.10+。校验脚本只使用标准库；`requirements.txt` 保留为空依赖说明文件，无需安装第三方包。

```powershell
python scripts/validate_prompt.py path/to/prompt.md --limit 10000 --confirmed-limit --require-timed-score
```

该检查只验证长度、结构和可选的故事成稿禁泄露规则，不能代替 BFL 生成结果或人工审片。

本版本吸收并改写了 [SoloEnt-AI/5min-drama-contest](https://github.com/SoloEnt-AI/5min-drama-contest) 的阶段锁定、开场承诺/结尾兑现和四段因果推进，以及 [AAAAAAAJ/asset-photorealism-lighting-optimizer](https://github.com/AAAAAAAJ/asset-photorealism-lighting-optimizer) 的参考图职责、光源因果链和材质证据规则；未复制其专属剧情或平台流程。

同时借鉴 [AAAAAAAJ/ai-film-general-skill](https://github.com/AAAAAAAJ/ai-film-general-skill) 的输入闸门、四段式视频出口、提示词独立颗粒度和按结构到光声质感的审片顺序；比赛投稿禁限规则沉淀在 `references/submission-compliance.md`。

Upstream inspiration: SoloEnt-AI/5min-drama-contest (staged story locking and opening/ending payoff); AAAAAAJ/asset-photorealism-lighting-optimizer (reference responsibilities, light-source causality, material evidence); AAAAAAJ/ai-film-general-skill (task/input gates, four-section video output, granularity and review order); user-supplied Seedance directing materials; local Starline FLUX Video Director skill

## 安装与排障

将本目录放入本机 Skills 目录后，用 `$starline-video-prompt` 调用即可。若提示词超过平台上限，先压缩重复负面词和声音描述，保留人物/空间锁定、按秒节拍和稳定尾帧。该 Skill 借鉴了用户提供的 Seedance 2.0 教程的“先控参数、再控镜头、保留续接余量”思路。

Verify the package after installation with `npx skills list` or `npx skills list --global`. Validate its source structure with `python C:\Users\xiaoy\.agents\skills\starline-meta-skill\scripts\validate_skill.py .`.

## 前置条件

- [ ] Python 3.10+（仅本地提示词校验需要）
- [ ] Node.js 与 `npx skills`（安装 Skill）
- [ ] GitHub CLI 仅在发布 Skill 时需要：`gh auth status`

## 致谢与许可

本版本吸收并改写了 `SoloEnt-AI/5min-drama-contest` 的阶段锁定、开场承诺/结尾兑现和四段因果推进，以及 `AAAAAAJ/asset-photorealism-lighting-optimizer` 的参考图职责、光源因果链和材质证据规则；未复制其专属剧情或平台流程。

本 Skill 代码与原创文档采用 MIT License；上游项目、示例剧情、图片和第三方素材不在本许可范围内。

## License

MIT. Third-party upstream projects and their assets remain under their own licenses.

Upstream inspiration: SoloEnt-AI/5min-drama-contest (staged story locking and opening/ending payoff); AAAAAAJ/asset-photorealism-lighting-optimizer (reference responsibilities, light-source causality, material evidence); user-supplied Seedance directing materials; local Starline FLUX Video Director skill

## Troubleshooting

当人物或场景漂移时，不要再增加风格词；收紧人物、服装、空间几何与镜头轴。若 20 秒片段节奏过慢，明确把第一个事件置于 0-1 秒，并增加 2-4 秒一次的因果阶段。来源：Seedance 2.0 public tutorial supplied by user; local Starline FLUX Video Director skill。
