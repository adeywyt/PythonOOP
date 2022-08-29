# 类的组合
class Turtle:
    def say(self):
        print("我是Turtle")


class Cat:
    def say(self):
        print("我是Cat")


class Dog:
    def say(self):
        print("我是Dog")


class Garden:
    t = Turtle() # t是Turtle的实例化
    c = Cat()    # c是Cat的实例化
    d = Dog()    # d是Dog的实例化

    def say(self):
        self.t.say()  # 这里实例对象和类进行绑定
        self.c.say()  # 这里实例对象和类进行绑定
        self.d.say()  # 这里实例对象和类进行绑定


g = Garden()
g.say()

