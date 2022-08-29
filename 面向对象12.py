class CapStr(str):
    def __new__(cls, string):
        string = string.upper()
        return super().__new__(cls, string)


"""
在实例化对象创建之前进行拦截，
然后呢我们才去调用super().__new__()去创建真正的实例
"""

cs = CapStr("adeylinux")
print(cs)


# 对象被销毁的时候有个魔法方法：__del__(self)
class C:
    def __init__(self):
        print("我来了.")

    def __del__(self):
        print("我走了.")


c = C()
del c


# ====================================================================
# 对象被销毁的时候会调用：__del__(self)

# 对象的重生:
class E:
    def __init__(self, name, func):
        self.name = name
        self.func = func

    def __del__(self):
        self.func(self)


def outter():
    x = 0

    def inner(y=None):
        nonlocal x
        if y:
            x = y
        else:
            return x

    return inner


f = outter()
e = E("wyt", f)
print(e.name)
del e
g = f()
print(g.name)
