# 需求
# 定义  input_password  函数，提示用户输入密码
# 如果用户输入长度 < 8，抛出异常
# 如果用户输入长度 >=8，返回输入的密码


# def input_password():
#     pwd = input('请输入密码:')
#     if len(pwd) >= 8:
#         return pwd
#     info = Exception('您输入的密码不足8位')
#     raise info
#
#
# try:
#     user_pwd = input_password()
#     print(f'用户密码为{user_pwd}')
# except Exception as e:
#     print(f'错误信息是：{e}')

# 需求
# 定义  input_password  函数，提示用户输入密码
# 如果用户输入长度 < 8，抛出异常
# 如果用户输入长度 >=8，返回输入的密码


def input_password():
    pwd1 = input('请输入密码：')

    if len(pwd1) < 8:
        raise Exception('密码小于8位')
    else:
        return pwd1


try:
    input_password()
    print('等待验证中...')
except Exception as e:
    print(f'错误类型为：{e}')
else:
    print('您的密码正确')