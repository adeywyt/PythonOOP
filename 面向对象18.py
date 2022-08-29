class C:
    def __init__(self, data):
        self.data = data

    def __contains__(self, item):
        print("您好.")
        return item in self.data


c = C([1, 2, 3, 4, 5, 6])
print(3 in c)  # 这里的3传递到__contains__里面的item中(存在返回True,不存在返回False.)
print(666 in c)  # 这里的666传递到__contains__里面的item中(存在返回True,不存在返回False.)

# ====================================================================
print("====================================")


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


c = C([1, 2, 3, 4, 5, 6])
print(1 in c)  # 3存在返回True
print(2 in c)  # 55不存在返回False

# ====================================================================
print("====================================")


class C:
    def __init__(self, data):
        self.data = data

    def __getitem__(self, index):
        print("Getitme", end=" -> ")
        return self.data[index]


c = C([1, 2, 3, 4, 5, 6])
print(3 in c)
print(5 in c)
# ====================================================================
print("====================================")