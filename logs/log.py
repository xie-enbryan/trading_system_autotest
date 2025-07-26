# ！ /usr/bin/python3
# coding=utf-8
# @Time: 2025/7/26 22:49
# @Author: Enbryan Xie

import  logging
import os.path
import time

from common.tools import get_project_path, sep

def get_log(logger_name):
    # 创建一个logger
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)

    # 设置日志存放路径，日志文件名
    # 获取本地时间
    rq = time.strftime("%Y%m%d%H%M", time.localtime(time.time()))

    # 设置日志存放路径
    all_log_path = get_project_path() + sep(["logs","all_logs"], add_sep_before=True,add_sep_after=True)
    # 如果日志目录不存在， 就自动创建
    if not os.path.exists(all_log_path):
        os.mkdir(all_log_path)
    # 设置日志的文件名
    all_log_name = all_log_path + rq + ".log"

    # 创建handler
    # 创建handler写入所有日志
    fh = logging.FileHandler(all_log_name)
    fh.setLevel(logging.INFO)

    # 定义日志输出模式
    all_log_formatter = logging.Formatter("%(asctime)s - %(filename)s - %(module)s - %(funcName)s - %(lineno)d - %(levelname)s - %(message)s",
                                          datefmt="%Y-%m-%d %H:%M:%S")
    # 将定义好的输出形式添加到handler
    fh.setFormatter(all_log_formatter)

    # 给logger 添加handler
    logger.addHandler(fh)
    return logger

log = get_log("自动化测试")


if __name__ == '__main__':
    # get_log("自动化测试")
    log.debug("i am a debug message")
    log.info(" i am a info message")
    log.warning("i am a warning message")
    log.error("i am a error message")
    log.critical("i am a critical message")
