# 视频提示词导演系统

## 先写变化，不先写风格

好的技术纪录片镜头回答“谁在什么空间里，因为什么触发，画面中什么按怎样的速度变化，最后稳定成什么构图”。“电影感、震撼、高清”只能是修饰，不能替代事件。

## 时长容量

| 时长 | 建议事件数 | 节奏 |
|---|---:|---|
| 5-8 秒 | 1 个主动作 | 立刻发生，1 秒稳定尾帧 |
| 10 秒 | 2-3 个阶段 | 0-2 秒建因，2-8 秒反应，结尾停住 |
| 20 秒 | 4-6 个阶段 | 首秒动作，约每 2-4 秒产生一次明确状态变化，18-20 秒稳定 |

## 20 秒骨架

```text
FORMAT AND INTENT. [one shot, duration, viewer change]
INVARIANT LOCK. [person, wardrobe, room geometry, light, palette]
CAMERA LOCK. [lens, starting frame, one camera direction]
OBJECT PHYSICS. [material, origin, path, inertia]
TWENTY-SECOND PERFORMANCE SCORE.
0-2 seconds: [event already happening]
2-6 seconds: [cause becomes visible]
6-10 seconds: [pressure or transformation]
10-15 seconds: [human decision/action]
15-18 seconds: [result becomes legible]
18-20 seconds: [stable end frame for next shot]
POST-PRODUCTION PLACEHOLDER. [real screenshot/title space]
HARD NEGATIVES. [only relevant failure prevention]
```

## 连续性契约

相邻镜头复述：同一人物、服装、空间几何、光向、色板、镜头轴、上一镜尾帧中的物体位置。只让一个主变量变化；例如“卡片堆积”变成“桌面任务图”，不要同时换房间、换衣服、换机位、换时间。

## 成果证据

GitHub、网页、学习笔记、项目数据和中文标题由真实截图或后期合成完成。生成 Prompt 只制作无字的平面或留白，避免模型生成不可核验的假 UI 和乱码。
