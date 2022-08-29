class C:
    x = 100

    def he(self, v):
        x = v
        print(v)
        print(x)


c = C()
c.he(250)
print(c.x)  # 不会变化
C.x = 250
print(C.x)
print(c.x)
