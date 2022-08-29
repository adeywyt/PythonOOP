class D:
    def __bool__(self):
        print("Bool")
        return True


d = D()
print(bool(d))

# ====================================================================
print("====================================")


class D:
    def __init__(self, data):
        self.data = data

    def __len__(self):
        print("len")
        return len(self.data)


d = D("Python")
print(bool(d))

# ====================================================================
print("====================================")


# 比较运算符的魔法方法：
class S(str):
    def __lt__(self, other):
        return len(self) < len(other)

    def __gt__(self, other):
        return len(self) > len(other)

    def __eq__(self, other):
        return len(self) == len(other)


s1 = S("google")
s2 = S("google pixel3")
print(s1 < s2)  # (6 < 13)
print(s1 == s2)  # (6 ==13)
print(s1 > s2)  # (6 > 13)
print(s1 <= s2)  # (6 <= 13)
print(s1 >= s2)  # (6 >= 13)
print(s1 != s2)
# ====================================================================
print("====================================")


# 不想要某个魔法方法实现
class S(str):
    def __lt__(self, other):
        return len(self) < len(other)

    def __gt__(self, other):
        return len(self) > len(other)

    def __eq__(self, other):
        return len(self) == len(other)

    __le__ = None  # 不想要__le__魔法方法实现
    __ge__ = None  # 不需要__ge__魔法方法实现
    __ne__ = None  # 不需要__ne__魔法方法实现


s1 = S("Google")
s2 = S("google")
# print(s1 != s2)  # 这里会报错,因为__ne__的魔法方法不可以实现
"""
<    __lt__(self,other)
<=   __le__(self,other)
>    __gt__(self,other)
>=   __ge__(self,other)
==   __eq__(self,other)
!=   __ne__(self,other)
"""


# ====================================================================


# 如果没有找到contains魔法方法则会去找iter,next魔法方法.
# 如果没有contains和iter,next则会去寻找getitem魔法方法.
class C:
    def __init__(self, data):
        self.data = data  # [1, 2, 3, 4, 5, 6]

    def __iter__(self):  # 本身就是迭代器
        print("Iter", end=" -> ")
        self.i = 0  # i=0 随着+1变化
        return self  # 返回本身 #本身就是迭代器

    def __next__(self):
        print("Next", end=" -> ")
        if self.i == len(self.data):  # 判断self是否等于列表的个数.等于否会返回False
            raise StopIteration  # 一旦执行了raise语句,raise后面的语句将不能执行.
        item = self.data[self.i]
        self.i += 1  # 0+1 1+1 2+1 3+1 4+1 5+1 ....(不存在)
        return item  # 1 2 3 4 5

    __contains__ = None  # 在这里明确的表示__contains__魔法方法,不希望关系判断这种方法出现.


c = C([1, 2, 3, 4, 5, 6])
# print(3 in c)  这里会报错，因为__contains__魔法方法赋值为：None,所以实现不了
# print(3 not in c) 这里会报错，因为__contains__魔法方法赋值为：None,所以实现不了
