# -*- coding:UTF-8 -*-
import mongoengine


class MongoEngine(object):
    def __init__(self, Metaclass):
        self.Object = Metaclass.objects
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

    def __update(self, id):
        pass

    def __updateList(self, id):
        pass

    def __del(self, id):
        pass

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

    def UPDATE(self, id):
        return self.__update(id)

    def UPDATELIST(self, id):
        return self.__updateList(id)

    def DELETE(self, id):
        return self.__del(id)

    def __call__(self):
        return self
