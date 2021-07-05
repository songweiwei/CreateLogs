# -*- coding: utf-8 -*-
# author: songwei
# place: Shenzhen Guangdong
# time: 2020/6/22 14:55
import os, re, json, traceback
import logging
import time

def logger_fn(name,input_file,level=logging.INFO):
    '''
    传入日志名、日志文件以及日志的等级，记录日志
    :param name: 日志的名称
    :param input_file: 日志的文件
    :param level: 日志的等级
    :return:
    '''
    tf_logger=logging.getLogger(name)
    tf_logger.setLevel(level)
    log_dir=os.path.dirname(input_file)
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    fh=logging.FileHandler(input_file,mode="w",encoding="utf-8")
    date_format="%y/%m/%d %H:%M:%S %p"
    formatter=logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(message)s',datefmt=date_format)
    fh.setFormatter(formatter)
    tf_logger.addHandler(fh)
    return tf_logger


if __name__ == '__main__':
    now = time.strftime('%Y-%m-%d %H%M%S', time.localtime())
    logger_result=logger_fn("result","logs/result/test-{}.log".format(now))
    logger_result.info("结果为1")

    logger_info=logger_fn("info","logs/info/info-{}".format(now))
    logger_info.info("其他信息")

    logger_info.info("修改了master远程")

    logger_info.info("增加了dev")





















































