# Prior-art research：2026-08-30

## Sources

- `SoloEnt-AI/5min-drama-contest`：公开仓库与 `SKILL.md`、`references/beats-5min.md`、`references/format-storyboard.md`。
- `AAAAAAJ/asset-photorealism-lighting-optimizer`：公开仓库与 `SKILL.md`、`references/core-workflow.md`、`references/lighting-camera.md`、`references/scenes-vfx.md`。
- `AAAAAAJ/ai-film-general-skill`：公开仓库与 `SKILL.md`、`references/cinedance-v4-four-section-adapter.md`、`references/prompt-granularity-contract.md`、`references/review-iteration-post.md`。
- 用户提供的《AI影像真实感大师课》PPT 与 Wan2.7 人像提示词模板：只提取自然皮肤、脸部结构、光线来源、材质与抓拍/资产图区分的通用机制。

## Keep / adapt / reject / invent

- Keep：分阶段锁定故事种子、世界规则、角色支点、开场承诺和结尾兑现；四段推进必须持续新增信息或后果。
- Adapt：把短剧的场景/动作/台词/音效字段与视频 Prompt 的首帧、物理、尾帧合同合并；把参考图职责拆分为构图、身份、道具、光色和材质。
- Adapt：将主光源位置、软硬、色温、遮挡、衰减、投影和反射写进每镜灯光；把尺度、粗糙度、接触、受力、摄影响应作为真实感证据。
- Adapt：先做任务/输入闸门与独立颗粒度检查，再按“素材描述—一句话概括—画面内容描述—全局补充”组织直出提示词；审片顺序从结构和时长开始，逐层到身份、空间、物理、表演、特效、光声质感。
- Adapt：把比赛规则视为发布门禁，区分最终成片与样片，并把危险动作、真人/第三方素材、片尾广告和文件交付问题纳入复核。
- Adapt：人物资产先锁成年原创身份、脸部结构、少量皮肤微观状态、衣物/道具接触和主光；身份资产与剧情抓拍分别处理，避免故意失焦破坏后续连续性。
- Reject：不复制上游赛道名、人物、示例剧情、专属图片编辑平台约束、总导演专属方法名或固定字符承诺；不把上游文案整段拼接进本 Skill。
- Reject：不继承课程示例中可能产生低俗联想的身体细节、失焦作为默认人物资产策略，或任何未授权真人肖像暗示。
- Invent：方法论隐形输出门禁；故事成稿默认不出现 STAR、比例名、阶段名或检查表术语，改用剧情、动作和声音表达。

## Evidence limits

公开仓库结构与文本规则已本地读取；没有执行其未审查代码，也没有进行 FLUX/Seedance 提供商 A/B 生成。因此人物一致性、光线真实感和平台质量提升仍为 `missing evidence`。
