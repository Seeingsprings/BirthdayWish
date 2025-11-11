一个基于 Python Tkinter 的轻量级桌面祝福动画。程序会沿着心形轨迹依次弹出小窗提示，播放完成后进入居中的祝福界面（渐变背景 + 心形粒子上浮）。心形轨迹支持“心跳式”微微脉动，整体视觉更富生命力与氛围感。

### 功能特性
- 心形轨迹弹窗：小窗按心形路径逐个出现，自动居中、定时关闭。
- 祝福界面：渐变色背景，心形粒子上浮动画，支持自定义标题（已示例“祝你生日快乐”）。
- 心跳脉动：统一对弹窗位置做正弦缩放，模拟心脏轻微搏动（可开关与调参）。
- 中文友好：默认使用“微软雅黑”字体与多条温馨提示语。

### 展示

![26dc6053e96554004785e135f3f61f8a](https://github.com/user-attachments/assets/fcfc1473-fe55-49ab-86c3-09c4e9389de2)

<img width="2000" height="1060" alt="92316a5a4ca48e536f2dd40ea78ff5d7" src="https://github.com/user-attachments/assets/5dfee5a1-18ff-4b09-abca-83b2ce104f4b" />



### 环境要求
- Python 3.x
- 标准库：tkinter、time、math、random（均为 Python 自带）
- 系统建议：Windows（已适配窗口置顶与布局）

你也可以直接下载.exe文件。

### 快速开始
1. 安装 Python 3（若未安装）。
2. 在本目录下运行：

```bash
python demo.py
```

运行后即可看到弹窗沿心形出现，随后进入祝福界面。



### 文件结构
- `demo.py`：主程序，包含弹窗轨迹、祝福界面与脉动动画逻辑。
- `README.md`：说明文档（本文件）。

### 关键参数（可在 demo.py 顶部或对应位置调整）
- 轨迹与节奏
  - `desired_points`：心形轨迹上的点数量（默认 50）。
  - `delay_ms`：相邻弹窗出现间隔（默认 90ms）。
  - `hold_seconds`：每个小窗停留时长（默认 6 秒）。
  - `WINDOW_W / WINDOW_H`：每个小窗的宽高（默认 120x60）。
- 脉动动画
  - `PULSE_ENABLED`：是否开启脉动（默认 True）。
  - `PULSE_AMPLITUDE`：脉动幅度（建议 0.03–0.08，默认 0.06）。
  - `PULSE_SPEED_HZ`：脉动频率（默认 0.8 Hz）。
- 主题样式（`THEME`）
  - 字体：`font_primary`、`font_title`（默认“微软雅黑”）。
  - 颜色：`bg_grad_top`/`bg_grad_bottom`（祝福界面渐变），`accent`/`accent_light` 等。

### 自定义与二次创作
- 修改提示文案：在 `show_warn_tip` 中的 `tips` 列表增删内容即可。
- 修改祝福标题：`show_final_blessing` 中 `title_id` 的文本（示例为“祝你生日快乐”）。
- 调整祝福界面风格：修改 `THEME` 渐变色、标题字体大小等。
- 想要更多主题：可将 `tips` 与主题色抽到独立 JSON 文件，运行时加载。

### 常见问题
- 闪烁/卡顿：适当增大 `delay_ms`、缩短 `hold_seconds`，或降低 `desired_points`。
- 字体不生效：Windows 默认存在“微软雅黑”；若无请安装或换成系统可用字体。
- 多显示器：窗口坐标基于当前屏幕尺寸计算，如跨屏使用可根据实际需求调整中心点。

### 打包分发（可选）
使用 PyInstaller 生成单文件 EXE：

```bash
pip install pyinstaller
pyinstaller -F -w demo.py
```

生成结果在 `dist/` 目录，双击可运行。

### 许可
本示例用于学习与演示，你可以自由修改与分发。如用于商业场景，请自行评估并加上适当的版权与第三方依赖声明。*** End Patch```}>>();

