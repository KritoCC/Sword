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

# 算法优化，试着用一个target.write()将line1、line2和line3打印出来，
# 替换掉原来的6行代码
n1 = "\n"
target.write(line1 + n1 + line2 + n1 + line3 + n1)

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


# open 为什么多了一个 w 参数
# open() 的默认参数是 open(file, 'rt') 也就是读取文本的模式，
# 默认参数可以不用填写。
# 而本题练习是写入文件，因此不适应使用 r 参数，
# 需要指定写入模式，因此需要增加 w 参数。


# 如果在'w'模式打开文件，那么我们还需不需要 target.truncate()?
# truncate()的作用是将文件截断指定 size 字节
# 本习题中没有指定truncate()的大小，所以实际上是清空了文件的内容
# 'w'打开一个文件只用于写入。
# 如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
# 所以不需要target.truncate()也可以


# 在文件模式中可以使用那些修饰符？
# 当前最重要的一个是+修饰符，你可以用它来实现'w+'、'r+'、'a+'。
# 这样可以把文件同时读写的方法打开，并根据使用的字符，
# 以不一样的方式实现文件的定位。
# r+	打开一个文件用于读写。文件指针将会放在文件的开头。
# rb+	以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。
# w+	打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
# wb+	以二进制格式打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
# a+	打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。
#       文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
# ab+	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。
#       如果该文件不存在，创建新文件用于读写。


# seek()函数是Python中操作文件游标移动操作的函数
# 用法如下:
# seek(offset,whence=0)
# offset：开始的偏移量，也就是代表需要移动偏移的字节数
# whence：给offset参数一个定义，表示要从哪个位置开始偏移；
# 0代表从文件开头开始算起，1代表从当前位置开始算起，2代表从文件末尾算起。

# 在使用seek（）函数时，有时候会报错为
# “io.UnsupportedOperation: can't do nonzero cur-relative seeks”
# 代码如下：

# >>> f=open("ex16_test.txt","r+")    #以读写的格式打开文件ex16_test.txt
# >>> f.read()    #读取文件内容
# ' To all the people out there.
# I say I don't like my hair.
# I need to shave it off.
# To all the people out there.
# I say I don't like my hair.
# I need to shave it off.'
# >>> f.seek(3,0)       #从开头开始偏移三个单位（偏移到“n”）
# 3
# >>> f.seek(5,1)     #想要从上一次偏移到的位置（即“n”）再偏移5个单位
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# io.UnsupportedOperation: can't do nonzero cur-relative seeks

# 照理说，按照seek()方法的格式file.seek(offset,whence)，后面的1代表从当前位置开始算起进行偏移，那又为什么报错呢？
# 这是因为，在文本文件中，没有使用b模式选项打开的文件，只允许从文件头开始计算相对位置，从文件尾计算时就会引发异常。
# 将  f=open("ex16_test.txt","r+")  改成 f = open("ex16_test.txt","rb")   就可以了.
# 改正后的代码如下：
# >>> f = open("ex16_test.txt","rb")
# >>> f.seek(3,0)
# 3
# >>> f.seek(5,1)
# 8
