from abc import ABCMeta, abstractmethod


class Observable():
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self, **kwargs):
        for i in kwargs:
            self.__dict__[i] = kwargs[i]

    @abstractmethod
    def __str__(self):
        res = type(self).__name__ + '('
        for i in self.__dict__.keys():
            if i[0] != '_':
                res += str(i) + '=' + str(self.__dict__[i]) + ', '
        res = res[:-2]
        res += ')'
        return res

