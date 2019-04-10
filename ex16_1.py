# 习题十六巩固练习一

# 要求用 argv 方式
from sys import argv

# 解包
script, filename = argv

print("脚本%r正在读取文件：%s..." % (script, filename))

# 打开文件
file_open = open(filename)

# 用print打印出读取的内容
print(file_open.read())


# 运行结果：
# PS C:\Users\12409\AppData\Local\atom\file> python ex16_1.py ex16_test.txt
# 脚本'ex16_1.py'正在读取文件：ex16_test.txt...
# To all the people out there.
# I say I don't like my hair.
# I need to shave it off.
