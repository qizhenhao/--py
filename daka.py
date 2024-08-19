import tkinter as tk
from tkinter import messagebox
import time
from threading import Thread
import os
import sys
from windows_api import show_popup

determine = [False, False]

# 定义检查时间并弹出提示框的函数
def check_time():
    while True:
        current_time = time.localtime()
        hour = current_time.tm_hour
        minute = current_time.tm_min
        # 检查是否在指定时间段内
        if (8 <= hour < 9 and minute < 30) and not determine[0]:
            determine[0] = show_popup(True)
            time.sleep(60)  # 每分钟检查一次

        if (18 <= hour < 19) and not determine[1]:
            determine[1] = show_popup(False)
            time.sleep(60)
        
        if hour >= 0 and hour < 5:
            determine[0] = determine[1] = False  # 重置状态

        time.sleep(30)

# 使用线程来运行时间检查函数
def start_checking_time():
    time_thread = Thread(target=check_time, daemon=False)
    time_thread.start()

if __name__ == "__main__":
    start_checking_time()
    # 确保主进程退出
    sys.exit()
