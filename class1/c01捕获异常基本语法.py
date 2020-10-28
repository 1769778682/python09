# 提示用户输入整数
try:
    num = int(input('请输入整数：'))
    print(num)
except:
    print('输入的数据有误！')