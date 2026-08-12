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
- “用二八法则写六段连续镜头的英文 Prompt。”
- “按 STAR 法则把 GitHub 项目做成一条技术纪录片视频。”

## 你可以直接这样说

- “按二八法则把这份学习笔记写成一个 20 秒 FLUX 3 视频提示词。”
- “为我的 GitHub 项目设计六段连续镜头的英文 Prompt，每段 20 秒。”

## 不负责的工作

- 不点击 Playground、提交 API、上传素材或下载视频。
- 不负责剪映剪辑、配音、字幕烧录。

需要真实连续生成时，配合 `starline-flux-video-director`：本 Skill 先写 prompt，该 Skill 再负责首尾帧链与受控提交。

## 默认产物

每个镜头会得到中文节拍表、英文 Prompt、建议参数、真实截图替换位和必要负面词。20 秒 Prompt 默认采用 20/80：短的不可变约束 + 高密度、可读的时间线。

## 本地检查

要求 Python 3.10+。校验脚本只使用标准库；`requirements.txt` 保留为空依赖说明文件，无需安装第三方包。

```powershell
python scripts/validate_prompt.py path/to/prompt.md --limit 10000 --confirmed-limit --require-timed-score
```

该检查只验证长度和结构，不能代替 BFL 生成结果或人工审片。

## 安装与排障

将本目录放入本机 Skills 目录后，用 `$starline-video-prompt` 调用即可。若提示词超过平台上限，先压缩重复负面词和声音描述，保留人物/空间锁定、按秒节拍和稳定尾帧。该 Skill 借鉴了用户提供的 Seedance 2.0 教程的“先控参数、再控镜头、保留续接余量”思路。

Verify the package after installation with `npx skills list` or `npx skills list --global`. Validate its source structure with `python C:\Users\xiaoy\.agents\skills\starline-meta-skill\scripts\validate_skill.py .`.

## Troubleshooting

当人物或场景漂移时，不要再增加风格词；收紧人物、服装、空间几何与镜头轴。若 20 秒片段节奏过慢，明确把第一个事件置于 0-1 秒，并增加 2-4 秒一次的因果阶段。来源：Seedance 2.0 public tutorial supplied by user; local Starline FLUX Video Director skill。
