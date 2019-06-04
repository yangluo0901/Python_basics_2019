class MySingleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "instance"):
            cls.instance = super().__new__(cls, *args, **kwargs)
        return cls.instance

    def __init__(self):
        print("initializing subSingleton ...")
        self.x = 100


class SubSingleton(MySingleton):
    def __init__(self):
        print("initializing subSingleton ...")
        self.x = 101


a = SubSingleton()
# b = MySingleton()
print(a.x)
# b.x = 10
# print(a.x)
