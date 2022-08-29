# slice函数
s = "I love Wyt"
print(s[2:6])
print(s[slice(2, 6)])
print(s[7:])
print(s[slice(7, None)])
print(s[::4])
print(s[slice(None, None, 4)])
print("*" * 12)


class D:
    def __init__(self, data):
        self.data = data

    def __getitem__(self, index):
        return self.data[index]

    def __setitem__(self, index, value):
        self.data[index] = value


d = D([1, 2, 3, 4, 5])
print(d[:])
print(d[1])
d[1] = 5
print(d[1])
d[2:4] = [2, 3]
print(d[:])

# ====================================================================
print("====================================")


class D:
    def __init__(self, data):
        self.data = data

    def __getitem__(self, index):
        return self.data[index] * 2


d = D([1, 2, 3, 4, 5])
for i in d:
    print(i, end=" ")
# ====================================================================
print("\n====================================")
