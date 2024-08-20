import tkinter as tk
from tkinter import messagebox
import time

def show_popup(is_up_ban: bool, width: int = 430, height: int = 300, start_x: int = None, start_y: int = None, end_x: int = None, end_y: int = None):
    result = {"minutes": None}  # 用于存储返回的分钟数

    def slide_in(start_x, start_y, end_x, end_y):
        """滑动动画使窗口从指定位置滑入到目标位置"""
        # Customize the sliding effect
        distance_x = start_x - end_x
        distance_y = start_y - end_y
        steps = 32  # Number of steps for sliding animation
        for i in range(steps + 1):
            x = start_x - int(i * distance_x / steps)
            y = start_y - int(i * distance_y / steps)
            root.geometry(f"{width}x{height}+{x}+{y}")
            root.update()
            time.sleep(0.02)

    def confirm():
        """确认按钮点击事件，保存分钟数并关闭窗口"""
        try:
            delay_minutes = int(entry.get())
            result["minutes"] = delay_minutes
            root.destroy()
        except ValueError:
            messagebox.showerror("输入错误", "请输入有效的延迟时间（分钟）。")

    def cancel():
        """取消按钮点击事件，关闭窗口"""
        result["minutes"] = None
        root.destroy()

    # 创建主窗口
    root = tk.Tk()
    root.title("打卡提示")
    root.configure(bg='#ffffff')

    # 创建并配置框架
    frame = tk.Frame(root, bg='#ffffff', padx=20, pady=20, borderwidth=1, relief="flat")
    frame.pack(padx=20, pady=20, expand=True)

    # 设置消息标签
    message = "上班了！请记得打卡。" if is_up_ban else "下班了！请记得打卡。"
    label = tk.Label(frame, text=message, bg='#ffffff', font=("Roboto", 16), fg="#202124")
    label.grid(row=0, column=0, columnspan=2, pady=20, sticky="n")

    # 设置输入框标签
    entry_label = tk.Label(frame, text="延迟提醒/分钟:", bg='#ffffff', font=("Roboto", 14), fg="#5f6368")
    entry_label.grid(row=1, column=0, sticky="e", padx=10, pady=10)
    
    # 设置输入框
    entry = tk.Entry(frame, width=15, font=("Roboto", 14), bd=1, relief="solid")
    entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")
    
    # 设置确认按钮
    confirm_button = tk.Button(frame, text="确认", command=confirm, bg='#34a853', fg='white', font=("Roboto", 14), relief="raised")
    confirm_button.grid(row=2, column=0, pady=20, padx=10, sticky="e")
    confirm_button.bind("<Enter>", lambda e: confirm_button.config(bg='#2c6b43'))  # 鼠标悬停时改变颜色
    confirm_button.bind("<Leave>", lambda e: confirm_button.config(bg='#34a853'))  # 鼠标离开时恢复颜色

    # 设置取消按钮
    cancel_button = tk.Button(frame, text="取消", command=cancel, bg='#ea4335', fg='white', font=("Roboto", 14), relief="raised")
    cancel_button.grid(row=2, column=1, pady=20, padx=10, sticky="w")
    cancel_button.bind("<Enter>", lambda e: cancel_button.config(bg='#c1351d'))  # 鼠标悬停时改变颜色
    cancel_button.bind("<Leave>", lambda e: cancel_button.config(bg='#ea4335'))  # 鼠标离开时恢复颜色

    root.update_idletasks()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Initialize the position to be outside the visible screen area
    initial_x = start_x if start_x is not None else screen_width
    initial_y = start_y if start_y is not None else screen_height
    final_x = end_x if end_x is not None else screen_width - width
    final_y = end_y if end_y is not None else screen_height - height

    root.geometry(f"{width}x{height}+{initial_x}+{initial_y}")

    # 执行滑动动画
    slide_in(initial_x, initial_y, final_x, final_y)
    root.attributes('-topmost', True)
    root.mainloop()

    return result["minutes"]

# 示例调用
# delay_minutes = show_popup(True, width=430, height=300, start_x=0, start_y=0, end_x=100, end_y=100)
# print(f"返回的分钟数: {delay_minutes}")


def get_screen_bottom_right():
    root = tk.Tk()
    root.withdraw()  # 隐藏主窗口

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # 窗口右下角的坐标
    bottom_right_x = screen_width
    bottom_right_y = screen_height

    root.destroy()  # 销毁隐藏的窗口
    return bottom_right_x, bottom_right_y

# # 示例调用
# x, y = get_screen_bottom_right()
# print(f"屏幕右下角的坐标: x={x}, y={y}")

def qizhenhao_style_up():
    x, y = get_screen_bottom_right()
    return show_popup(True,width=430, height=273, start_x=x, start_y=y-340, end_x=x-440, end_y=y-340)

def qizhenhao_style_down():
    x, y = get_screen_bottom_right()
    return show_popup(False,width=430, height=273, start_x=x, start_y=y-340, end_x=x-440, end_y=y-340)