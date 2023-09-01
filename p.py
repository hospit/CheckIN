from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
import os
import time

def my_clock():
    print("Hello! The time is:%s"%datetime.now())

# 解锁屏幕
unlock = [
    'adb shell input keyevent 224',
    'adb shell input swipe 500 2000 500 1000 300',
    'adb shell input text 84153',
    'adb shell input tap 820 1700',
    'adb shell input tap 660 1760'
]
check_in = [
    'adb shell input tap 660 1760'
]


def tool(cmd):
    for i in cmd:
        time.sleep(1)
        # os.system() 返回 0 表示执行成功
        result = os.system(i)
        print(result)
        str1 = '%Y-%m-%d %H:%M:%S'
        tuple1 = time.localtime()
        time.strftime(str1, tuple1)
        print(time.strftime(str1, tuple1))


def cron_task():
    print('23456')
    tool(unlock)

if __name__ == '__main__':
    scheduler = BlockingScheduler()
    # scheduler.add_job(my_clock, "interval", seconds=3)
    scheduler.add_job(my_clock, "cron", hour=00, minute=21 )
    scheduler.start()