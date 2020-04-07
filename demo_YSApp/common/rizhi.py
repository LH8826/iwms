import logging
import time


def getlog():
    '''
        指定保存日志的文件路径，日志级别，以及调用文件
        将日志存入到指定的文件中
    '''

    # 创建一个logger
    logger = logging.getLogger()
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        # 创建一个handler，用于写入日志文件
        log_time = time.strftime("%Y_%m_%d_")
        log_path = "D://HDiWMS//report_of_day//"
        log_name = log_path + log_time + 'YSApplog.txt'

        # 创建一个handler，用于输出到文件
        fh = logging.FileHandler(log_name, 'a', encoding='utf-8')
        fh.setLevel(logging.INFO)

        # 再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        # 定义handler的输出格式
        formatter = logging.Formatter(
            '[%(asctime)s] %(filename)s->%(funcName)s line:%(lineno)d [%(levelname)s]%(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给logger添加handler
        logger.addHandler(fh)
        logger.addHandler(ch)

        # 关闭打开的文件
        fh.close()
        ch.close()
    return logger


