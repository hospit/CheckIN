"""
日志封装，可设置不同等级的日志颜色
"""
import logging
import logging.handlers
from typing import Text
import colorlog
import time
import os


class LogHandler:
    """ 日志打印封装"""
    # 日志级别关系映射
    level_relations = {
        'debug': logging.DEBUG,
        'info': logging.INFO,
        'warning': logging.WARNING,
        'error': logging.ERROR,
        'critical': logging.CRITICAL
    }

    def __init__(self,
            filename: Text,
            level: Text = "info",
            when: Text = "D",
            # "%(levelname)-8s%(asctime)s%(name)s:%(filename)s:%(lineno)d %(message)s"
            fmt: Text = "%(levelname)-8s%(asctime)s:%(filename)s:%(lineno)d %(message)s"):
        self.logg = logging.getLogger(filename)

        formatter = self.log_color()

        # 设置日志格式
        format_str = logging.Formatter(fmt)
        # 设置日志级别
        self.logg.setLevel(self.level_relations.get(level))
        # 往屏幕上输出
        screen_output = logging.StreamHandler()
        # 设置屏幕上显示的格式
        screen_output.setFormatter(formatter)
        # 往文件里写入#指定间隔时间自动生成文件的处理器
        time_rotating = logging.handlers.TimedRotatingFileHandler(
            filename=filename,
            when=when,
            backupCount=3,
            encoding='utf-8'
        )
        # 设置文件里写入的格式
        time_rotating.setFormatter(format_str)
        # 把对象加到logger里
        self.logg.addHandler(screen_output)
        self.logg.addHandler(time_rotating)

    @classmethod
    def log_color(cls):
        """ 设置日志颜色 """
        log_colors_config = {
            'DEBUG': 'cyan',
            'INFO': 'green',
            'WARNING': 'yellow',
            'ERROR': 'red',
            'CRITICAL': 'red',
        }

        formatter = colorlog.ColoredFormatter(
            '%(log_color)s[%(asctime)s] [%(levelname)s]: %(message)s',
            log_colors=log_colors_config
        )
        return formatter


def root_path():
    """ 获取项目根路径 """
    path = os.path.dirname(os.path.abspath(__file__))
    """
    os.path.abspath: 返回绝对路径
    __file__: 表示当前文件
    os.path.dirname：返回上一层文件夹绝对路径
    """
    return path


def ensure_path_sep(path) -> Text:
    """兼容 windows 和 linux 不同环境的操作系统路径 """
    if "/" in path:
        path = os.sep.join(path.split("/"))
    if "\\" in path:
        path = os.sep.join(path.split("\\"))
    """
    os.sep.join(): 函数传入的参数是一个列表，输出的结果是将列表中的元素用相应平台对应的路径分隔符链接起来的整体
    """
    return root_path() + path


now_time_day = time.strftime("%Y-%m-%d", time.localtime())
# DEBUG = LogHandler(ensure_path_sep(f'\\logs\\debug-{now_time_day}.log'), level='debug')
INFO = LogHandler(ensure_path_sep(f"\\logs\\info.log"), level='info')
# ERROR = LogHandler(ensure_path_sep(f"\\logs\\error-{now_time_day}.log"), level='error')
# WARNING = LogHandler(ensure_path_sep(f'\\logs\\warning-{now_time_day}.log'))
# ee = LogHandler(ensure_path_sep(f'\\logs\\warning-{now_time_day}.log'), level='debug')

if __name__ == '__main__':
    print(os.path.abspath('.'))
    # ee.logg.debug("测试")
    # DEBUG.logg.info("0000")
    # INFO.logg.info("cs")
    # try:
    #     open("s.txt", 'r')
    # except Exception:
        # INFO.logg.exception("Failed to open sklearn.txt from logger.exception")
