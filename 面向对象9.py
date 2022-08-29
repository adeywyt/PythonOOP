class Displayer:
    def display(self, message):
        print(message)


class LoggerMixin:
    def log(self, message, filename="logfile.txt"):
        with open(filename, "a") as f:
            f.write(message)

    def display(self, message):
        super().display(message)  # 这个display的父类没有
        self.log(message)  # log方法
        # self是MySubClass本身.


class MySubClass(LoggerMixin, Displayer):
    def log(self, message):
        super().log(message, filename="subclasslog.txt")
        '''
        这个log方法是LoggerMixin类里面的方法
        这里的log调用LoggerMixin类的log
        '''


subclass = MySubClass()
subclass.display("This is a text.")
'''
subclass.display("This is a text.")调用display里面的display，
display里面的display在调用Displayer里面的display函数.

This is a text传递给isplay里面的display然后display里面的display再传递给
Displayer里面的display
'''
