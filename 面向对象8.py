class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say(self):
        print(f"我是{self.name},今年{self.age}岁.")


class FlyMixin():
    def fly(self):
        print("我会飞.")


class Pig(FlyMixin, Animal):
    def special(self):
        print("我的技能是吃饭.")


p = Pig("猪", 5)
p.say()  # 这里调用say(),输出我是猪,今年5岁.
p.special()  # 这里调用special(),输出我的技能是吃饭.
p.fly()  # 这里调用fly(),输出我会飞.
