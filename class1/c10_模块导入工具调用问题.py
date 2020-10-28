from class1.c10_module import num
from class1.c10_module import func
from class1.c10_module import Test

# 调用
print('*模块内调用*' * 4)
print(num)
func()
xm = Test('小明')
print(xm.name)
xm.eat()
print('*模块内调用*' * 4)

# 注意
# 如果将文件作为模块导入后，调用其内部的工具，
# 那么，在模块中的调试用的代码也会被执行
