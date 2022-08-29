# 钻石继承（A被调用了两次）
# A重复调用
# 钻石继承有弊端
class A:
    def __init__(self):
        print("我是A")


class B1(A):
    def __init__(self):
        A.__init__(self)  # 这里调用A,则会输出我是A
        print("我是B1")


class B2(A):
    def __init__(self):
        A.__init__(self)  # 这里调用A,则会输出我是A
        print("我是B2")


class C(B1, B2):
    def __init__(self):
        B1.__init__(self)  # 这里调用B1,则会输出我是B1
        B2.__init__(self)  # 这里调用B2,则会输出我是B2
        print("我是C")


c = C()

print("-"*20)
# ====================================================================
# 使用super：super会自动寻找父类.避免重复调用
# super函数使用
# super依赖于MRO顺序
class A:
    def __init__(self):
        print("我是A")


class B1(A):
    def __init__(self):
        super().__init__()
        print("我是B1")


class B2(A):
    def __init__(self):
        super().__init__()
        print("我是B2")


class C(B1, B2):
    def __init__(self):
        super().__init__()
        print("我是C")


b = C()

# 查看MRO（Python的MRO即Method Resolution Order（方法解析顺序））
print(C.mro())
print(B1.mro())
print(B2.__mro__)
print(A.__mro__)
