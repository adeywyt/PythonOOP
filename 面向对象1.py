# 对象=属性+方法
class e:  # 命名e类型
    def hello(self):  # self是实例化对象本身
        print("I am Python")  # 输出I am Python


E = e()  # E是e的实例化
E.hello()


# ==============================================================
# 继承
class A:
    x = 520

    def he(self):
        print("我是A")


class B(A):  # 这里继承了类A的使用属性
    pass  # 占位符


b = B()  # b是B的实例化
print(b.x)  # 输出x的数值(520)
b.he()  # 调用he()


class B(A):
    x = 888

    def he(self):
        print("我是B")


b = B()
print(b.x)  # 这里覆盖了x=520变成了x=888
b.he()  # 这里覆盖了我是A变成了我是B
