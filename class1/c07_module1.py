# 全局变量
name = '小明'


# 函数
def demo():
    print('xxx')


class File(object):
    def __init__(self, weight):
        self.weight = weight

    @staticmethod
    def age(age):
        print(f'年龄是{age}')
