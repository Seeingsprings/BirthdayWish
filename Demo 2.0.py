# -*- coding: utf-8 -*-
import time
import math
import random
import tkinter as tk
from tkinter import ttk

# ===== 主题与样式常量 =====
THEME = {
    "font_primary": ("微软雅黑", 10),
    "font_title": ("微软雅黑", 40, "bold"),
    "bg_soft": "#FFF9C4",
    "bg_grad_top": "#FFF3E0",
    "bg_grad_bottom": "#E1F5FE",
    "tip_colors": [
        "#FFE0E0", "#E0F7FA", "#E8F5E9", "#FFF3E0", "#EDE7F6",
        "#F3E5F5", "#E1F5FE", "#FBE9E7", "#E8EAF6", "#FFFDE7"
    ],
    "accent": "#C2185B",
    "accent_light": "#E91E63",
    "transparent_key": "#FF00FF",  # 作为透明色键
    "corner_radius": 12
}

# 获取屏幕尺寸
try:
    temp_root = tk.Tk()
    temp_root.withdraw()
    SCREEN_W = temp_root.winfo_screenwidth()
    SCREEN_H = temp_root.winfo_screenheight()
    temp_root.destroy()
except Exception:
    SCREEN_W, SCREEN_H = 1920, 1080

# 窗口大小
WINDOW_W, WINDOW_H = 120, 60
desired_points = 50  # 爱心点数


def generate_heart_points(num_points, screen_w, screen_h, window_w, window_h):
    points = []
    center_x = screen_w // 2
    center_y = screen_h // 2
    for i in range(num_points):
        t = i / num_points * 2 * math.pi
        # 心形参数方程
        x = 16 * (math.sin(t) ** 3)
        y = 13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t)
        y = -y  # 翻转 Y 轴，使其正向向下

        # 缩放与平移
        scale = min(screen_w // 40, screen_h // 40)
        x = center_x + x * scale
        y = center_y + y * scale

        # 确保不会超出屏幕边界
        x = max(window_w // 2, min(x, screen_w - window_w // 2))
        y = max(window_h // 2, min(y, screen_h - window_h // 2))

        points.append((int(x), int(y)))
    return points


def _draw_rounded_rect(canvas, x1, y1, x2, y2, r, fill, outline=""):
    # 保留占位，祝福界面的圆角或后续扩展可能继续使用
    r = max(0, min(r, int(min(x2 - x1, y2 - y1) / 2)))
    canvas.create_rectangle(x1, y1, x2, y2, fill=fill, outline=outline)


def show_warn_tip(x, y, w, h):
    root = tk.Toplevel()
    root.overrideredirect(True)
    root.geometry(f"{w}x{h}+{x - w // 2}+{y - h // 2}")
    root.attributes("-topmost", True)

    # 随机淡色背景（简单版本）
    r = random.randint(200, 255)
    g = random.randint(200, 255)
    b = random.randint(200, 255)
    color = f"#{r:02x}{g:02x}{b:02x}"
    root.configure(bg=color)

    # 提示语（保持中文修复后的内容）
    tips = [
        "前路皆平安，所愿皆成真",
        "愿你好运常在",
        "愿你开心每一天",
        "保持微笑",
        "记得吃早饭",
        "注意休息，早点睡",
        "多喝热水",
        "好好吃饭",
        "多喝水",
        "别太累",
        "加油呀，向前走",
        "每天都要元气满满",
        "善待自己"
    ]
    tip = random.choice(tips)

    label = ttk.Label(root, text=tip, font=("微软雅黑", 10), background=color)
    label.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

    # 10 秒后自动关闭（不做 alpha 动画）
    root.after(10000, root.destroy)
    return root





def show_final_blessing():
    root = tk.Tk()
    root.title("祝福")
    root.attributes("-topmost", True)

    window_width, window_height = 1000, 500
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")
    root.configure(bg=THEME["bg_soft"])  # 基底色

    # 使用 Canvas 做粒子动画 + 文案
    canvas = tk.Canvas(root, width=window_width, height=window_height, bg=THEME["bg_soft"], highlightthickness=0)
    canvas.pack(fill=tk.BOTH, expand=True)

    # 渐变背景
    def hex_to_rgb(hx):
        hx = hx.lstrip("#")
        return tuple(int(hx[i:i+2], 16) for i in (0, 2, 4))

    def rgb_to_hex(rgb):
        return f"#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}"

    top = hex_to_rgb(THEME["bg_grad_top"])
    bottom = hex_to_rgb(THEME["bg_grad_bottom"])
    steps = max(1, window_height // 2)
    for i in range(steps):
        t = i / (steps - 1) if steps > 1 else 1.0
        r = int(top[0] + (bottom[0] - top[0]) * t)
        g = int(top[1] + (bottom[1] - top[1]) * t)
        b = int(top[2] + (bottom[2] - top[2]) * t)
        color = rgb_to_hex((r, g, b))
        y1 = int(i * (window_height / steps))
        y2 = int((i + 1) * (window_height / steps))
        canvas.create_rectangle(0, y1, window_width, y2, outline="", fill=color)

    title_id = canvas.create_text(
        window_width // 2, window_height // 2 - 40,
        text="祝你生日快乐",
        font=THEME["font_title"],
        fill=THEME["accent"]
    )

    sub_id = canvas.create_text(
        window_width // 2, window_height // 2 + 20,
        text="❤  ❤  ❤",
        font=("Arial", 22),
        fill=THEME["accent_light"]
    )

    # 心形粒子
    particles = []

    def heart_points(size=8):
        pts = []
        for i in range(0, 36):
            t = i / 36 * 2 * math.pi
            x = 16 * (math.sin(t) ** 3)
            y = 13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t)
            x, y = x * size / 16, -y * size / 16
            pts.append((x, y))
        return pts

    base_shape = heart_points(7)

    def spawn_particle():
        cx = random.randint(80, window_width - 80)
        cy = window_height - 40
        scale = random.uniform(0.8, 1.6)
        color = random.choice(["#F06292", "#EC407A", "#FF80AB", "#FF8A80", "#F48FB1"])
        dx = random.uniform(-0.4, 0.4)
        vy = random.uniform(-1.8, -1.0)
        lifetime = random.randint(1300, 2200)  # ms
        created = int(time.time() * 1000)
        # 预绘制为多边形
        coords = []
        for (px, py) in base_shape:
            coords.extend([cx + px * scale, cy + py * scale])
        pid = canvas.create_polygon(coords, fill=color, outline="", smooth=True)
        particles.append({
            "id": pid, "x": cx, "y": cy, "dx": dx, "vy": vy,
            "scale": scale, "color": color, "created": created, "life": lifetime, "rot": random.uniform(-0.02, 0.02)
        })

    def animate():
        now = int(time.time() * 1000)
        to_remove = []
        for p in particles:
            age = now - p["created"]
            if age > p["life"]:
                to_remove.append(p)
                continue
            # 轻微上升 + 左右漂移
            p["x"] += p["dx"]
            p["y"] += p["vy"]
            # 重新计算形状坐标（简单但直观）
            coords = []
            for (px, py) in base_shape:
                coords.extend([p["x"] + px * p["scale"], p["y"] + py * p["scale"]])
            canvas.coords(p["id"], *coords)
        for p in to_remove:
            canvas.delete(p["id"])
            particles.remove(p)

        # 周期性生成
        if random.random() < 0.25 and len(particles) < 40:
            spawn_particle()
        root.after(16, animate)

    animate()


    root.mainloop()


def main():
    points = generate_heart_points(desired_points, SCREEN_W, SCREEN_H, WINDOW_W, WINDOW_H)

    # 创建一个隐藏的 Tk 实例，用于管理 Toplevel
    master = tk.Tk()
    master.withdraw()  # 自身隐藏

    # 调度多个显示窗口，用 after 延迟（恢复最初版本）
    delay_ms = 90  # 每个窗口间隔 90ms
    hold_seconds = 6  # 小窗显示后保留 6 秒

    for i, (x, y) in enumerate(points):
        master.after(i * delay_ms, show_warn_tip, x, y, WINDOW_W, WINDOW_H)

    # 所有小窗显示完成后 + hold_seconds，再显示最终祝福
    total_time = len(points) * delay_ms + hold_seconds * 1000
    master.after(total_time, lambda: [master.destroy(), show_final_blessing()])

    master.mainloop()


if __name__ == "__main__":
    main()