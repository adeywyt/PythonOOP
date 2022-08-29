# 多重继承：
class A:
    x = 520

    def he(self):
        print("我是A")


class B:
    x = 880
    y = 250

    def he(self):
        print("我是B")


class C(A, B):
    pass


c = C()
print(c.x)  # python首先会去类里面找,找到了,则不会去B类里面去寻找
c.he()   # python首先会去类里面找,找到了,则不会去B类里面去寻找
# 访问顺序是从A-B（从左往右）
