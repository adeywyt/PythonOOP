class Power:
    def __init__(self, exp):
        self.exp = exp

    def __call__(self, base):
        return base ** self.exp


square = Power(2)  # 这里传递给了exp
print(square(2))  # 这里传递给了base
print(square(3))  # 这里传递给了base

# ================================================
print(repr("Google"))  # 这里的repr函数和str函数的功能差不多.
print(eval(repr("Google")))  # eval函数可以去除双引号

# ================================================
print("================================================")


class C:
    def __repr__(self):
        return "I Love Python"


c = C()
print(repr(c))
print(str(c))  # 这里没有定义str的魔法方法，它会自动的寻找repr的魔法方法进行传递
cs = [C(), C(), C()]
for i in cs:
    print(i)
print(cs)
# ================================================
print("================================================")


class C:
    def __str__(self):
        return "I Love PyCharm"


c = C()
print(str(c))
print(repr(c))  # 这里不会输出”I love PyCharm“否会输出c的内存地址
cs = [C(), C(), C()]
for i in cs:
    print(i)
print(cs)  # 这里输出会是C的内存地址不会输出"I Love PyCharm"

print("================================================")


# ================================================

class C:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return f"data={self.data}"

    def __repr__(self):
        return f"C(self.data)"

    def __add__(self, other):
        self.data += other


c = C(250)
print(c)
print(c + 250)  # 这里输出None
c + 250  # 这里不可以写print(c + 250)，否则会输出None
print(c)
"""
c         输出C(250)
print(c)  输出data=250
"""
