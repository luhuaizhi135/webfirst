# -*- coding: utf-8 -*-
import logging
import os
logging.debug('debug message')  
logging.info('info message')  
logging.warning('warning message')  
logging.error('error message')  
logging.critical('critical message') 

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.getLogger().setLevel(logging.ERROR)
logging.basicConfig(filename='d:/myfirstweb.log', level=logging.ERROR, format=LOG_FORMAT,filemode='w')
logging.error("dddddddddddddddddddddddddddddd")
print("end")


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_DIR)
print(os.path.abspath(__file__))
print(os.path.dirname(os.path.abspath(__file__)))
