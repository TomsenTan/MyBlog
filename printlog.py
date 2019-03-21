# -*-conding：utf98-*-
# Date:2018-12-19
# @Author:Thomson


import logging as log

def err(e, *args, **kwargs):
    print(e)
    return log.error

def verbose():
    pass

def info(INFO, *args, **kwargs):
    print(INFO)

def debug():
    pass


