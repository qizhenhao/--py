import tkinter as tk
from tkinter import messagebox
import time
from threading import Thread
import os
import sys

def show_popup(is_up_ban : bool):
    """
    打卡提醒弹窗

    :param is_up_ban: 上班提醒为True, 下班提醒为False ，布尔类型。
    :return: True
    """
    def slide_in():
        # 初始位置设置在屏幕外面
        start_x = root.winfo_screenwidth()  # 屏幕宽度
        start_y = root.winfo_screenheight()  # 屏幕高度

        # 目标位置
        target_x = start_x - 900  # 300 是窗口宽度
        target_y = start_y - 223  # 150 是窗口高度

        # 滑动动画
        for i in range(0, 320, 10):  # 从0到200，增加10
            x = start_x - i
            
            root.geometry(f"300x150+{x}+{target_y}")  # 更新窗口的位置
            root.update()
            time.sleep(0.02)  # 控制滑动速度

    root = tk.Tk()
    root.title("打卡提示")  # 设置窗口标题

    # 设置窗口的样式
    root.configure(bg='#f0f0f0')  # 设置背景颜色

    # 创建消息框
    frame = tk.Frame(root, bg='#ffffff', padx=20, pady=20, borderwidth=2, relief="groove")
    frame.pack(fill="both", expand=True)
    label = tk.Label(frame, text="请记得打卡。", bg='#ffffff', font=("Helvetica", 14))
    if is_up_ban:
        label = tk.Label(frame, text="上班了！请记得打卡。", bg='#ffffff', font=("Helvetica", 14))
    else:
        label = tk.Label(frame, text="下班了！请记得打卡。", bg='#ffffff', font=("Helvetica", 14))
    label.pack(pady=10)
    
    button = tk.Button(frame, text="确认", command=root.destroy, bg='#4CAF50', fg='white', font=("Helvetica", 12))
    button.pack()

    root.update_idletasks()
    
    # 设置初始位置在右下角之外
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.geometry(f"300x150+{screen_width}+{screen_height}")  # 初始位置在右下角之外
    
    # 使用滑动动画使窗口从右下角滑入
    slide_in()

    root.attributes('-topmost', True)  # 确保窗口总是最上层
    root.mainloop()

    return True

# show_popup(True)
# show_popup(False)
