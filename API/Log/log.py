# encoding:utf-8
"""
@file = log
@author = zouju
@create_time = 2023-08-07- 13:52
"""
import logging

# 日志模块
logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)
handler = logging.FileHandler("log.txt")
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)