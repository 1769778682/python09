# 1.提示用户输入一个整数
# 2.使用8除以用户输入的整数并且输出


try:
    num = int(input('请输入一个整数:'))
    # print(num)
    result = 8 / num
    print(result)
except ValueError:
    print('值类型错误，转换类型失败')
except ZeroDivisionError:
    print('0不能做除数')
else:
    print('正常执行，没有任何异常')
finally:
    print('执行完成，但是不确定上方是否存在异常！')