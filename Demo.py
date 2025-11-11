import time
import math
import random
import tkinter as tk
from tkinter import ttk

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
desired_points = 50  # 心形点数


def generate_heart_points(num_points, screen_w, screen_h, window_w, window_h):
    points = []
    center_x = screen_w // 2
    center_y = screen_h // 2
    for i in range(num_points):
        t = i / num_points * 2 * math.pi
        # 心形参数方程
        x = 16 * (math.sin(t) ** 3)
        y = 13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t)
        y = -y  # 翻转 Y 轴，使心形正立

        # 缩放和平移
        scale = min(screen_w // 40, screen_h // 40)
        x = center_x + x * scale
        y = center_y + y * scale

        # 确保窗口不会超出屏幕边界
        x = max(window_w // 2, min(x, screen_w - window_w // 2))
        y = max(window_h // 2, min(y, screen_h - window_h // 2))

        points.append((int(x), int(y)))
    return points


def show_warn_tip(x, y, w, h):
    root = tk.Toplevel()
    root.overrideredirect(True)
    root.geometry(f"{w}x{h}+{x - w // 2}+{y - h // 2}")
    root.attributes("-topmost", True)

    # 随机浅色背景
    r = random.randint(200, 255)
    g = random.randint(200, 255)
    b = random.randint(200, 255)
    r = random.randint(200, 255)
    g = random.randint(200, 255)
    b = random.randint(200, 255)
    color = f"#{r:02x}{g:02x}{b:02x}"
    root.configure(bg=color)

    # 随机提示语
    tips = [
        "前程似锦，祝你，也祝我",
        "保持好心情",
        "天天开心奥",
        "保持微笑",
        "天 天 都 要 元 气 满 满 ",
        "注意身体，少 熬 夜 ",
        "记得吃水果",
        "好好吃饭",
        "多喝水",
        "别太累",
        "天冷了，加衣服",
        "每天都要元气满满噢！",
        "照顾好自己"
    ]
    tip = random.choice(tips)
    label = ttk.Label(root, text=tip, font=("微软雅黑", 10), background=color)
    label.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

    # 10秒后自动关闭
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
    root.configure(bg="#FFF9C4")  # 改为浅黄色

    main_label = tk.Label(
        root,
        text="生日快乐",
        font=("宋体", 40, "bold"),
        bg="#FFF9C4",  # ← 这里也要改！
        fg="#C2185B",
        justify=tk.CENTER
    )
    main_label.pack(expand=True, pady=30)

    decoration_label = tk.Label(
        root,
        text="❤ ❤ ❤",
        font=("Arial", 20),
        bg="#FFF9C4",  # ← 这里也要改！
        fg="#E91E63"
    )
    decoration_label.pack(pady=10)


    root.mainloop()


def main():
    points = generate_heart_points(desired_points, SCREEN_W, SCREEN_H, WINDOW_W, WINDOW_H)

    # 创建一个隐藏的主 Tk 实例（用于管理 Toplevel）
    master = tk.Tk()
    master.withdraw()  # 隐藏主窗口

    # 逐个弹出提示窗口，用 after 延迟
    delay_ms = 90  # 每个窗口间隔 90ms
    hold_seconds = 6  # 所有小窗显示完后保持 6 秒

    for i, (x, y) in enumerate(points):
        master.after(i * delay_ms, show_warn_tip, x, y, WINDOW_W, WINDOW_H)

    # 在所有小窗显示完毕后 + hold_seconds，再显示最终祝福
    total_time = len(points) * delay_ms + hold_seconds * 1000
    master.after(total_time, lambda: [master.destroy(), show_final_blessing()])

    master.mainloop()


if __name__ == "__main__":
    main()