# 注意：在Python中异常的类型很多，如下举例
# 数据类型转换
# num = int('你好')  # 错误类型：ValueError

# 0 不能做除数
# num1 = 1/0  # 错误类型：ZeroDivisionError

# 文件操作，打开文件
# open('./text.txt')  # 错误类型：FileNotFoundError
# try:
#     int('你好')  # 模拟类型装换报错
# # 当对特定异常类型进行处理时，
# # 能够保证只捕获设定好的异常类型，其它异常不做处理
# except ZeroDivisionError:
#     print('xxx')

# 针对特定异常类型执行捕获操作（多种）
# try:
#     print(int('你好'))
# except (ValueError, FileNotFoundError):
#     print('xxx')

# 3.针对特定异常类型执行捕获操作（具体异常类型不明）
# try:
#     int('你好')
#     # open('./text.txt')
#     # num1 = 1 / 0
# except Exception as e:
#     print('xxx')
#     print(e)


# 1. 针对特定异常类型执行捕获操作(一种)
# try:
#     int('你好')  # 模拟类型转换报错, 异常类型: ValueError
# # 注意: 当对特定异常类型进行处理时, 能够保证只捕获设定好的异常类型, 其他异常不做处理
# except ZeroDivisionError:
#     print('xxx')

# 2. 针对特定异常类型执行捕获操作(多种)
# try:
#     # int('你好')  # 模拟类型转换报错, 异常类型: ValueError
#     # num = 1 / 0
#     open('./test.txt')
# # 注意: 如果想要同时捕获多种类型, 可以使用以下语法: (异常类型1, 异常类型2 ...)
# except (ZeroDivisionError, FileNotFoundError):
#     print('捕获异常后的操作')

# 3. 针对特定异常类型执行捕获操作(具体异常类型不明)
try:
    # 异常的模拟
    int('你好')
    # num = 1/0
    # open('./test.txt')
# 注意: 如果不清楚具体要捕获的异常类型名, 可以使用 Exception (所有异常类型), 由于异常类型范围过大, 不建议使用
# except Exception:
# 注意: 有些时候, 需要捕获异常后, 再提取异常信息, 那么此时就一定需要有一个异常类型名
# e : 只是变量名, 可以任意命名, 只是 Exception 首字母是 e, 因此习惯用法
except Exception as e:
    print('捕获异常后的处理')
    print(e)