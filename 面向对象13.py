class S(str):
    def __add__(self, other):
        return len(self) + len(other)


s1 = S("Python")
s2 = S("Javascript")
print(s1 + s2)  # 这里相当于s1.__add__(s2)
# self是自己,也就是+号左边的对象
# other参数指的是别人也就是+号右边的对象
print("Python" + s2)
print(s2 + "Python")

print("*" * 20)
# ====================================================================

class S1(str):
    def __add__(self, other):
        return NotImplemented
        # NotImplemented表示__add__未实现.则会运行__radd__魔法方法


class S2(str):
    def __radd__(self, other):
        return len(self) + len(other)


s1 = S1("Python")
s2 = S2("Java")
print(s1 + s2)  # 这里相当于s1.__radd__(s2)

print("*" * 20)
# ====================================================================

class S1(str):
    def __iadd__(self, other):
        return len(self) + len(other)


s1 = S1("apple")
s2 = S2("Java")
s1 += s2 # s1=s1+s2
print(s1, type(s1))
s2 += s2  # s2=s2+s2
print(s2,type(s2))
"""
s2+=s2
如果增强赋值运算符的左边对象没有实现相应的魔法方法
加等于的左边的这个对象没有实现__iadd__()方法,python
则会使用__add__和__radd__方法进行代替
"""
"""
调用__radd__()方法是需要条件的首先它们两个要是基于不同的类
因为S2和S2是相同的类，则不会调用__radd__()方法,则会去调用__add__() 
"""

