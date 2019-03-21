# -*- coding:UTF-8 -*-
'''
@ Date: 2019-03-19
@ Author: Thomson
'''

import contextlib
import printlog

class MYDatabase(object):
    def __init__(self):
        self.connected = False
        self.db = MYDatabase()
        super(MYDatabase, self).__init__()

    def _connect(self):
        self.db.connect()

    def _close(self):
        self.db.close()

def dbconn(fn):
    pass


@contextlib.contextmanager
def database():
    db = MYDatabase()
    try:
        if not db.connected:
            db._connect()
        yield db
    except Exception as e:
        printlog.err(e)
        db._close()

