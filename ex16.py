# 习题十六

# 上一题的加分练习中有让我们查看file的帮助文档
# 虽然python3已经没有file这个东西了
# 不过我们通过 help() 知道了被 open 打开后的这个东西是什么以及它的帮助文档，
# 如果大家有大概看过应该有见过下面的几个方法（函数），请记住它们：
# close —— 关闭文件。如同编辑器中 文件 -> 保存 的作用。
# read —— 读取文件内容。可以把结果赋值给一个变量。
# readline —— 读取文本文件中的一行内容。
# truncate(size) —— 将文件截断指定 size 字节，size 后的内容将删除请小心使用。
#                   如果没有指定 size，则从当前位置起截断；截断之后 size 后面的所有字符被删除。
# write(something) —— 把 something 写入文件。
# seek(0) —— 将读写位置移动到文件开头
# 本题将练习写入文件 writer 的使用。

from sys import argv

# 通过解包argv获取脚本名和将要保存的文件名
script, filename = argv

# 询问是否继续编辑文件filename
print("We're going to erase %r" % filename)
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")
# 等待用户输入是否继续编辑
input("?")

# 如果用户未输入ctrl-c则会继续执行
print("Opening the file...")
# 打开文件对象
target = open(filename, 'w')
# 没有指定truncate()的大小，所以实际上删除了文件的内容
print("Truncating the file. Goodbye!")
target.truncate()

# 获取三个input变量的内容
print("I'm going to write there to the file.")

line1 = input("line1: ")
line2 = input("line2: ")
line3 = input("line3: ")

# 将内容写入文件（只在内存中，并未写入硬盘）
print("I'm going to write there to the file.")
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

# 关闭文件，将文件写入硬盘
print("And finally, we close it.")
target.close()


# 运行结果：
# PS C:\Users\12409\AppData\Local\atom\file> python ex16.py ex16_test.txt
# We're going to erase 'ex16_test.txt'
# If you don't want that, hit CTRL-C (^C).
# If you do want that, hit RETURN.
# ?
# Opening the file...
# Truncating the file. Goodbye!
# I'm going to write there to the file.
# line1: To all the people out there.
# line2: I say I don't like my hair.
# line3: I need to shave it off.
# I'm going to write there to the file.
# And finally, we close it.
