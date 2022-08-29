class C:
    def __init__(self):
        self._x = 250  # 变量隐藏起来内部使用

    def getx(self):
        return self._x

    def setx(self, value):
        self._x = value

    def delx(self):
        del self._x

    x = property(getx, setx, delx)


c = C()
print(c.x)
print(c.__dict__)
c.x=520
print(c.x)
print(c.__dict__)
del c.x
print(c.__dict__)

