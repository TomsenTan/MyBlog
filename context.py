# -*- coding:UTF-8 -*-
'''
@ Date: 2019-03-19
@ Author: Thomson
'''

from multiprocessing import Lock,RLock
from threading import Lock,RLock,Thread
import printlog

class MLock:
    def __init__(self):
        self.lock = Lock()
        self.rlock = RLock()

    def _acquire(self):    # 需要添加对锁获取次数的判断
        self.lock.acquire()

    def _release(self):
        self.lock.release()

    def _rlacquire(self):
        try:
            self.rlock.acquire()
        except Exception as e:
            printlog.err(e)
        finally:
            pass

    def _rlrelase(self):
        try:
            self.rlock.release()
        except Exception as e:
            printlog.err(e)
        finally:
            pass


class Context:
    def __init__(self):
        self.lock = MLock()

    def __enter__(self):
        self.lock._acquire()
        pass

    def __exit__(self):
        self.lock._release()
        pass


