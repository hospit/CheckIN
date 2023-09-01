import os
import time
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
from logtool import INFO

def tool(cmd):
    for i in cmd:
        time.sleep(1)
        # os.system() 返回 0 表示执行成功
        result = os.system(i)
        if result == 0:
            INFO.logg.info('adb执行成功')
        else:
            INFO.logg.info(str(result) + ' 没有连接手机or系统没有识别到设备')


# 解锁 进入首页
def cron_task():
    # 解锁屏幕 adb 命令集
    _unlock = [
        'adb shell input keyevent 224',
        'adb shell input swipe 500 2000 500 1000 300',
        'adb shell input text 84153',
        'adb shell input tap 820 1700',
        'adb shell input tap 660 1760'
    ]
    tool(_unlock)


def check_in():
    # 打开 阿里钉 adb 命令
    _check_in = [
        'adb shell input tap 660 1760'
    ]
    tool(_check_in)


def run():
    cron_task()
    # 下方加个 判断 页面中是否有 阿里钉文字 判断，有者执行进入阿里钉
    check_in()

if __name__ == '__main__':
    # run()
    scheduler = BlockingScheduler()
    # scheduler.add_job(my_clock, "interval", seconds=3)
    scheduler.add_job(run, "cron", hour=12, minute=46)
    scheduler.start()



