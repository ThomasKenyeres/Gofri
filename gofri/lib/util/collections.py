class WrappedDictionary(object):
    def __init__(self):
        self.__dict = {}

    def __getattr__(self, item):
        return self.__dict[item]

    def __setattr__(self, key, value):
        object.__setattr__(self, key, value)
        self.__dict[key] = value

    def __repr__(self):
        return str(self.__dict)

    def __add__(self, other):
        if isinstance(other, (dict, WrappedDictionary)):
            self.__dict.update(other)
        else:
            raise TypeError("Cannot add type '{}'".format(type(other)))