# 重写
# __init__是构造函数
class C:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y

    def mul(self):
        return self.x * self.y


c = C(2, 3)


class D(C):
    def __init__(self, x, y, z):
        C.__init__(self, x, y)  # 相当于self.x=x self.y=y
        self.z = z

    def add(self):
        return C.add(self) + self.z  # return self.x + self.y +self.z

    def mul(self):
        return C.mul(self) * self.z  # return self.x * self.y * self.z


d = D(2, 3, 4)
print(d.add())
print(d.mul())
