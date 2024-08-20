import tkinter as tk
from tkinter import messagebox
import time
from threading import Thread
import os
import sys
from windows_api import qizhenhao_style_up, qizhenhao_style_down

determine = [False, False]

# 定义检查时间并弹出提示框的函数
def check_time():
    while True:
        current_time = time.localtime()
        hour = current_time.tm_hour
        minute = current_time.tm_min
        # 检查是否在指定时间段内
        if (8 <= hour < 9 ) and not determine[0]:
            determine[0] = qizhenhao_style_up()
            if determine[0] == None:
                determine[0] = True
            else:
                time.sleep(int(determine[0]) * 60 - 30)
                determine[0] = False

        if (18 <= hour < 22) and not determine[1]:
            determine[1] = qizhenhao_style_down()
            if determine[1] == None:
                determine[1] = True
            else:
                time.sleep(determine[1] * 60 - 30)
                determine[1] = False
        
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
