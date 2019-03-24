# -*- coding:UTF-8 -*-
import mongoengine
import printlog


class MongoEngine(object):
    def __init__(self, Metaclass):
        self.Object = Metaclass.objects()
        super(MongoEngine, self).__init__()

    def __getAll(self):
        return self.Object.all()

    def __get(self, id):
        return self.Object.filter(id)

    def __mget(self):
        pass

    def __save(self):
        pass

    def __msave(self):
        pass

    def __update(self, key1, key2,  action, value=None, upvalue=None):
        '''
        :param key1:  用于查询文档的key
               注意：若key1是id,则必须用 _id 形式，因数据库存储形式为 _id
        :param key2:  更新的key
        :param action:  更新操作
               --incr  增加
               --set   设置新值
        :param value:   用于查询文档的key对应的值
        :param upvalue: 更新字段的值
        :return:
        '''
        try:
            if action == 'incr':
                upaction = 'inc__' + key2
                self.Object(__raw__={key1: value}).update(**{upaction: upvalue})
            elif action == 'set':
                upaction = 'set__' + key2
                self.Object(__raw__={key1: value}).update(**{upaction: upvalue})
            else:
                pass
        except Exception as e:
            printlog.err(e)

    def __updateList(self, id):
        pass

    def __del(self, id):
        pass

    def __order(self, name, des=-1):
        if des == -1:
            name = '-' + name
            return self.Object.order_by(name)
        else:
            return self.Object.order_by(name)

    def __average(self, name):
        return self.Object.average(name)

    def GET(self, id):
        return self.__get(id)

    def GETAll(self):
        return self.__getAll()

    def MGET(self):
        return self.__mget()

    def SAVE(self):
        return self.__save()

    def MSAVE(self):
        return self.__msave()

    def UPDATE(self, key1, key2,  action, kvalue=None, upvalue=None):
        self.__update(key1, key2,  action, value=kvalue, upvalue=upvalue)

    def UPDATELIST(self, id):
        return self.__updateList(id)

    def DELETE(self, id):
        return self.__del(id)

    def ORDER(self, name, des=-1):
        return self.__order(name, des)

    def AVERAGE(self, name):
        return self.__average(name)

    def __call__(self):
        return self
