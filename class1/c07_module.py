# 1.导入形式一: import 模块名
# 1.导包
#
# import class1.c07_module1
#
# print(class1.c07_module1.name)
# class1.c07_module1.demo()
# xm = class1.c07_module1.File(55)
#
# print(xm.weight)
# xm.age()


# 导入形式二: from 模块名 import 工具名
# 1.导包


from class1.c07_module1 import name
from class1.c07_module1 import demo
from class1.c07_module1 import File


print(name)
demo()
xm = File(45)
xm.age()
print(xm.weight)