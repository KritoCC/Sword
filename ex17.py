# 习题十七

# 我们将编写一个Python脚本，将一个文件中的内容复制另一个文件中
# 并使用os.path.exists在拷贝前判断被拷贝的文件是否已经存在，
# 之后由用户判断是否继续完成拷贝

# 引入库
from sys import argv
from os.path import exists

# 解包参量
script, from_file, to_file = argv

# 打印任务目标
print("Copy from %r to % r" % (from_file, to_file))

# we could do these two on one line too, how?
# 如何把这两行写到一行
in_file = open(from_file)
indata = in_file.read()

# 打印文件字符长度。
print("The input file is %r bytes long" % len(indata))

# 打印目标文件是否已经存在
print("Does the output file exist? %r" % exists(to_file))
# 用户决定是否完成复制
print("Ready, hit RETURN to coutinue, CTRL-C to about")
input()

# 以写入模式打开目标文件
out_file = open(to_file, 'w')
# 写入复制的内容
out_file.write(indata)

# 打印操作完成（实际打印这段话的时候根本没完成）
print("Alright, all done.")

# 关闭文件（真保存至磁盘）
out_file.close()
in_file.close()


# 运行结果：
# PS C:\Users\12409> cd C:\Users\12409\AppData\Local\atom\file
# PS C:\Users\12409\AppData\Local\atom\file> python ex17.py ex16_test.txt ex17_copy.txt
# Copy from 'ex16_test.txt' to 'ex17_copy.txt'
# The input file is 162 bytes long
# Does the output file exist? False
# Ready, hit RETURN to coutinue, CTRL-C to about

# Alright, all done.


# 新知识
# 1.os.path.exists 是一个本题的新知识点。
#   和 sys 一样，os 也是 python 自带的基本库中的一员，主要提供和操作系统有关的功能。
#   其中 path 正如其名提供了和路径操作有关的功能。
#   在 path 模块中拥有 exists 这个方法，它的作用是判断所提供的文件名是否已经存在于磁盘中，
#   如果已经存在则返回 False ，反之则返回 True
# 2.len()用来返回其中项目的数量，例如
#   返回字符串的长度
print("\n %r" % len("hahaha"))


#  在powershell里输入echo能创建一个文件
#  echo "This is a txt file.">test.txt
#  输出cat能显示文件的内容
#  cat test.txt


# 在代码中写out_file.close()的原因
# 原因在于如果不写，则新复制的文件中是不会保存任何内容的。
# 也就是没有保存（如同在 16 题 Zed 介绍的一样）
# out_put = open(to_file, 'w') 执行时会创建 to_file 文件，但是没内容
# out_put.write(indata) 执行时，内容会写入到 to_file 的内存数据中，但仍未写入硬盘。
# 只有在执行 close 时 python 才指定文本的各种操作已经结束了，
# 不会再有任何变化，这个时候在写入硬盘可以尽可能地减少硬盘读写操作，提高效率（特别在特大文件的时候）

# 那么为什么在 精简练习、极限精简练习 中不需要关闭呢？
# 我的理解：
# 关键点在于没有使用变量，也就是没有给打开的文件起名字。
# 这个时候，任何操作是一次性的，我们没办法在写入了一些东西后再说“喂，就你，你再写入这些内容”，
# python 不知道这句‘喂’说的是哪一个内存堆栈中的数据。
# 所有没有起名的代码都是一次性的，不会保存在内存中，
# 针对 open 来说，python 就自动关闭它了。


# import机制
# Python语言中import的使用很简单，直接使用import module_name语句导入即可
# import本质：路径搜索和搜索路径
# 模块（module）：用来从逻辑（实现一个功能）上组织Python代码（变量、函数、类），本质就是*.py文件。
#                文件是物理上组织方式"module_name.py"，模块是逻辑上组织方式"module_name"。
# 包（package）：定义了一个由模块和子包组成的Python应用程序执行环境，
#               本质就是一个有层次的文件目录结构（必须带有一个__init__.py文件）。
# 导入一个模块
# import model_name
# 导入多个模块
# import module_name1,module_name2
# 导入模块中的指定的属性、方法（不加括号）、类
# from moudule_name import moudule_element [as new_name]
