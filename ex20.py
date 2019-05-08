# 习题二十

# 本练习通过脚本的参数获取被打印的文件名
# 因此需要argv获取脚本参数
from sys import argv


# 第一个函数，打印整个文档。
def print_all(f):
    print(f.read())


# 第二个函数，用来重置指针（相当于光标）到文件开头的位置
def rewind(f):
    f.seek(0)


# 函数：打印一个数字代表行号后，打印一行文件
def print_a_line(line_count, f):
    print(line_count, f.readline())


# 运用以上函数把脚本参数中的文件打印一遍

# 获取脚本参数
script, input_file = argv

# 从函数可以看出其中对参数f使用的方法都是
# Py2的file对象（在习题十五中得知在Py3中是TextIOWrapper）
# 它们都是被open后才出现的，所以我们需要打开文件以被函数调用
current_file = open(input_file)

# 首先打印全文
print("First let's print the whole file: \n")
print_all(current_file)

# 打印全文之后指针已经移动到了文档的末尾，想要做其他打印需要复位一下。
# Zed比喻这个过程像倒带一样
print("Now let's rewind, kind of like a tape.")
rewind(current_file)

# 然后指针已经回到起始位置了（0的位置）
# 逐行打印
print("Let's print three lines:")
# 设置一个代表行号的变量，打印第一行
current_line = 1
print_a_line(current_line, current_file)

# 变更行号，打印第二行（这里设置行号并不会改变
# f.readline的行，这个被打印的行号只是给人看的，写100也行
# 打印过一行之后，指针其实已经在第二行开头等着了）
current_line += 1   # 运用了赋值运算符，下面会介绍
print_a_line(current_line, current_file)

# 重复上一步再打印一行
current_line += 1
print_a_line(current_line, current_file)

# 运行结果：
# PS C:\Users\12409\AppData\Roaming\Atom\file> python ex20.py ex20_test.txt
# First let's print the whole file:

# This is line 1
# This is line 2
# This is line 3

# Now let's rewind, kind of like a tape.
# Let's print three lines:
# 1 This is line 1

# 2 This is line 2

# 3 This is line 3

# current_line 是怎么变成line_count的
# 其实line_count要叫做位置参数，之所以调用时的参数current_line成为了函数定义时的line_count
# 是因为它们在定义与被调用时所处的位置是一样的。如果我们把函数定义时两个参数的位置对调，并保持调用的顺序不变
# 或者，函数定义时不变，调用时对调。都会因为行号这个整数（int）没有readline()这个方法而导致错误发生


# seek的作用
# seek 是用来设置被 open 打开的文件对象指针。这个指针我爱想象它是打字的光标，
# read() 的时候光标会从当前位置逐字移动到末尾，每移动一个字就打印这个字
# （ open的打开方式 'r' 'w' 'r+' 'w+' 等影响光标默认位置）。
# 而 readline() 的时候则从当前位置移动到行末至下一行起始位置。

# 另外 seek 还有一个可选参数 whence
# 它一个可能有三种值 0,1,2
# 默认时是 0 ，表示从文件开始位置计算指针移动多少个 cookie 字节。
# 1，表示以当前为开始移动。
# 2，表示从末尾开始移动。


# += 操作符(赋值运算符）
# += 这个符号其实和 = 一类，一般都叫做赋值运算符，它还有几个兄弟姐妹。
# 其意义是：左边已存在的变量，与右边的值进行运算后，重新赋值给左边的变量。
# 假设已经有一个变量 a = 6 和一个 b = 2
# 运算符        描述            等价于         打印结果 print(a)
# a = b	       赋值            a = b               2
# a += b    相加后赋值        a = a + b            8
# a -= b    相减后赋值        a = a - b            4
# a *= b    相乘后赋值        a = a * b            12
# a /= b    相除后赋值        a = a / b            3.0
# a %= b    取模后赋值        a = a % b            0
# a **= b  幂运算后赋值       a = a ** b           36
# a //= b   整除后赋值        a = a // b	          3
