# 属性访问：
class C:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # 私有变量


c = C("wyt", 16)
print(hasattr(c, "name"))  # 检测是否存在
print(getattr(c, "name"))  # 获取name的数值
print(getattr(c, "_C__age"))  # 获取私有变量
setattr(c, "_C__age", 18)  # 修改私有变量
print(getattr(c, "_C__age"))  # 获取__agr
delattr(c, "_C__age")  # 在这里删除了__age这个私有变量
print(hasattr(c, "_C__age"))  # 检测是否存在

print("*" * 15)


# ====================================================================
class C:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # 私有变量

    def __getattribute__(self, item):
        print("拦截操作")
        return super().__getattribute__(item)


c = C("wyt", 16)
getattr(c, "name")
getattr(c, "_C__age")
print("*" * 15)


# ====================================================================
class C:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # 私有变量

    def __getattribute__(self, attrname):
        print("拦截")
        return super().__getattribute__(attrname)

    def __getattr__(self, attrname):
        if attrname == "adey":
            print("I Love Python")
        else:
            return AttributeError(attrname)


c = C("adey", 15)
go = c.adey # 这里的adey传递给了attrname,然后传递给了__getattr__(self,attrname).
print("*" * 15)


# ====================================================================
class D:
    def __setattr__(self, name, value):
        self.__dict__[name] = value  # 字典存储


d = D()
d.name = "wyt"
print(d.name)


# =====================================================================================
class D:
    def __setattr__(self, name, value):
        self.__dict__["name"] = value

    def __delattr__(self, name):
        del self.__dict__["name"]


d = D()
d.name = "wyt"
print(d.__dict__)
del d.name
print(d.__dict__)
