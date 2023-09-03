import os
import time
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
from logtool import INFO, ensure_path_sep
import easyocr


def tool(cmd):
    _count_result = 0
    for i in cmd:
        time.sleep(1)
        # os.system() 返回 0 表示执行成功
        result = os.system(i)
        _count_result += result
    if _count_result == 0:
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
        'adb shell input tap 820 1700'
    ]
    tool(_unlock)


# 打开阿里钉 并打卡
def check_in():
    # 打开 阿里钉 adb 命令
    _check_in = [
        'adb shell input tap 660 1760'
    ]
    tool(_check_in)


def easycorrun(filepath):
    reader = easyocr.Reader(['ch_sim', 'en'])
    _text = reader.readtext(filepath)
    return _text


def img_word(text, word_content):
    for i in text:
        if word_content in i:
            # print(True)
            # print(type(i))
            return True, i
    return False, None


# 通过计数 返回 文字所在坐标 数据
def coord(tuple_data):
    coord_data01 = tuple_data[0][0]
    coord_data02 = tuple_data[0][2]
    # coord_data = [int((coord_data01[0] + coord_data02[0])/2), int(((coord_data01[1] + coord_data02[1])/2))]
    coord_data = str((coord_data01[0] + coord_data02[0])//2) + ' ' + str(((coord_data01[1] + coord_data02[1])//2)) # // 取整除 - 返回商的整数部分
    return coord_data


# 截取当前 屏幕，并输出 图片保存路径
def screenshot():
    now_time_day = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
    _path = ensure_path_sep(f'/imgs/{now_time_day}.png')
    _command = 'adb exec-out screencap -p > ' + _path
    _result = os.system(_command)
    return _path


def run():
    cron_task()
    # 下方加个 判断 页面中是否有 阿里钉文字 判断，有者执行进入阿里钉
    _file_path = screenshot()
    time.sleep(1)
    check_in_run = True
    possible = ['取消', '阿里钉']
    text01 = easycorrun(_file_path)
    for i in possible:
        result, tuple_data = img_word(text01, i)
        if i == '取消' and result:
            # 这里执行 相关adb命令
            _coord = coord(tuple_data)
            os.system(f'adb shell input tap {_coord}')
            break
        elif i == '阿里钉' and result:
            check_in()
            check_in_run = False
        else:
            INFO.logg.info('页面进入异常检查代码')
    if check_in_run:
        check_in()
    # 下方 加个 截图 并判断是否打卡成功
    _file_path = screenshot()
    result, tuple_data = img_word(easycorrun(_file_path), '打卡成功')
    if result:
        INFO.logg.info('打卡成功')
    else:
        INFO.logg.info('打卡失败')



if __name__ == '__main__':
    # a=coord(([[487, 2173], [591, 2173], [591, 2233], [487, 2233]], '取消', 0.9918431518684246))
    # print(a)
    # print(screenshot())
    run()
    # scheduler = BlockingScheduler()
    # # scheduler.add_job(my_clock, "interval", seconds=3)
    # scheduler.add_job(run, "cron", hour=18, minute=47)
    # scheduler.start()



