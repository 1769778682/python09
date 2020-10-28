def demo1():
    num = int(input('请输入一个整数:'))
    num1 = 3 / num
    return num1


def demo2():
    return demo1()


try:
    demo2()
except ValueError:
    print('数据类型转换错误')

except Exception as e:
    print(f'未知错误{e}')