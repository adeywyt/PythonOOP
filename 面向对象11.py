# 面向对象的多态
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def intro(self):
        print(f"我是Cat,我叫{self.name},今年{self.age}岁.")

    def say(self):
        print("喵喵喵.")


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def intro(self):
        print(f"我是Dog,我叫{self.name},今年{self.age}岁.")

    def say(self):
        print("汪汪汪.")


class Pig:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def intro(self):
        print(f"我是Pig,我叫{self.name},今年{self.age}岁.")

    def say(self):
        print("呃呃呃.")


c = Cat("小白", 10)
d = Dog("小黑", 14)
p = Pig("小朱", 15)


def animal(x):
    x.intro()
    x.say()


animal(c)  # 这里调用了c的intro和say函数.c是Cat的实例化
animal(d)  # 这里调用了d的intro和say函数.c是Dog的实例化
animal(p)  # 这里调用了p的intro和say函数.c是Pig的实例化


class Bicycle:
    def intro(self):
        print("我跨过山和大海")

    def say(self):
        print("我有自行车环游世界")


b = Bicycle()
animal(b)
