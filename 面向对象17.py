# x = [1, 2, 3, 4, 5, 6]
# _ = iter(x)
# while True:
#     try:
#         i = _.__next__()
#     except StopIteration:
#         break
#     print(i, end=" ")


class Double:
    def __init__(self, start, stop):
        self.value = start - 1  # valu=start-1   # 1-1  2-1 3-1
        self.stop = stop   # 5

    def __iter__(self):  # 本身是迭代器/有__iter__方法他就是一个可迭代对象
        return self  # 返回自己(本身是迭代器)

    def __next__(self):
        if self.value == self.stop: 
            raise StopIteration # 一旦执行了raise语句,raise后面的语句将不能执行.
        self.value += 1
        return self.value * 2


d = Double(1,5)
for i in d:
    print(i, end=" ")
"""当程序出现错误，python会自动引发异常，也可以通过raise显示地引发异常。
一旦执行了raise语句，raise后面的语句将不能执行。"""
