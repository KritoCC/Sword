# 习题十三

# 在本题中将了解另一种将变量传递给脚本的方法（脚本就是你编写的 *.py 程序）。
# 运行一个 python 脚本我们可以用命令行输入 python ex13.py
# 其中 python 是要运行的程序，而 ex13.py 就是参数了。
from sys import argv
# read thr WYSS section for how to run This
script, first, second, third = argv

print("This script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

# 第6行:
# import语句的作用是引用我们（python自带的、其他人写的）已经写好的程序、“功能”，
# 能使这些“功能”可以在当前脚本中使用
# sys就是本次引入的“功能”，我们一般叫它们“模块”或“库”。
# 它提供了一系列有关python运行环境的变量和函数。

# import有两种用法
# *引入全部模块：import sys
# *引入部分模块：from sys import argv

# 这次用的就是第二种方法，从sys模块中引入了argv具体的“功能”（获取当前正在执行的命令行参数）

# 第8行
# 这一行是将argv进行解包。解包是个编程专用的名词
# 作用是将argv中包含的多个值依次赋值给左边的几个变量
# script，first，second，third

# 第10——13行：
# 我们将被赋值后的几个变量打印出来

# 这个脚本保存后需要在命令行中单独运行：（必须有 3 个参数）
# python ex13.py first 2nd 3rd
# 我们尝试几个不同的参数：

# PS C:\Users\12409> cd C:\Users\12409\AppData\Local\atom\file
# PS C:\Users\12409\AppData\Local\atom\file> python ex13.py first 2nd 3rd
# This script is called: ex13.py
# Your first variable is: first
# Your second variable is: 2nd
# Your third variable is: 3rd

# PS C:\Users\12409\AppData\Local\atom\file> python ex13.py cheese apples bread
# This script is called: ex13.py
# Your first variable is: cheese
# Your second variable is: apples
# Your third variable is: bread

# PS C:\Users\12409\AppData\Local\atom\file> python ex13.py Zed A. Shaw
# This script is called: ex13.py
# Your first variable is: Zed
# Your second variable is: A.
# Your third variable is: Shaw

# PS C:\Users\12409\AppData\Local\atom\file> python ex13.py 中文 行不行 ?
# This script is called: ex13.py
# Your first variable is: 中文
# Your second variable is: 行不行
# Your third variable is: ?

# 使用不同数量的参数会怎样？
# 两个参数
# PS C:\Users\12409\AppData\Local\atom\file> python ex13.py 两个 参数
# Traceback (most recent call last):
#   File "ex13.py", line 8, in <module>
#     script, first, second, third = argv
# ValueError: not enough values to unpack (expected 4, got 3)
# 解释：
# 当我使用两个参数的时候出错了
# 首先程序指出我们脚本第 8 行写的是 script, first, second, third = argv
# 这是刚刚解包的位置。
# python 提示 ValueError 值出错了，
# 具体错误是 not enough values to unpack (expected 4, got 3) 没有足够的值解包。
# 通对观察对比第 8 行的代码可以看出一些问题：
# argv 解包的第一个值，对应变量 script 永远都是我们运行的脚本的名字。
# 命令行中最后三个参数分别对应了 first, second, third 三个变量。
# 错误的问题就在于 third 没有办法取得参数了，因为我们只输入了两个参数。

# 四个参数
# PS C:\Users\12409\AppData\Local\atom\file> python ex13.py 四个 参数 行不行 ?
# Traceback (most recent call last):
#   File "ex13.py", line 8, in <module>
#     script, first, second, third = argv
# ValueError: too many values to unpack (expected 4)
# 解释：
# 和上面的情况相反，这次错误信息告诉我们参数太多了。
# 可以看出 python 的程序非常严谨，多一个不行少一个也不行。

# 将 input 和 argv 一起用，使脚本可以从用户得到更多输入。
length = int(input("What is the length of the rectangle?"))
width = int(input("What is the width of the rectangle?"))
print("The area of the rectangle is %d" % (width * length))
