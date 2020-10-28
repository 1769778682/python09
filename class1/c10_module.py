num = 10  # 全局变量


def func():  # 函数
    print('函数实现')


class Test(object):  # 类
    """测试类"""

    def __init__(self, name):
        self.name = name

    @staticmethod
    def eat():
        print('测试类->吃东西方法')


# 调用
# print('*模块内调用*' * 4)
# print(num)
# func()
# xm = Test('小明')
# print(xm.name)
# xm.eat()
# print('*模块内调用*' * 4)

# __name__:系统内置的属性，负责记录一个字符串，
# 字符串的内容会根据当前文件的运行方式进行切换
# print(__name__)
# 当前文件内运行，字符串为:__main__
# 当被当做模块调用执行时，字符串为：模块名（文件名）
# 将字符串的值为__main__作为判断条件，表示是以当前文件内运行的
if __name__ == "__main__":  # 本条件快速输入方法，直接输入 main + enter 即可
    # 注意：该条件能够保证，只要不是当前文件内执行，条件代码都不会被执行
    # 在用当前文件调用方法进行调试操作时，调试代码调用一律放置于该条件之下！
    print('*模块内调用*' * 4)
    print(num)
    func()
    xm = Test('小明')
    print(xm.name)
    xm.eat()
    print('*模块内调用*' * 4)
