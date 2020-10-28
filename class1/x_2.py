# print(__file__)
# C:/Users/sandysong/Desktop/就业班/python/day 09/class1/x_2.py

# 需求：获取当前文件所在的文件夹的绝对路径
# 1.导入系统的OS模块
import os

print(os.path.abspath(__file__))  # abspath(): 返回文件的绝对路径
print(os.path.dirname(__file__))  # 返回当前文件的上一层目录的绝对路径
# 需求实现
print(os.path.dirname(os.path.abspath(__file__)))