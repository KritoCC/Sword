# 习题二十五

# 本题虽然叫做练习，不过通过以下函数和变量的练习，还是有不少新的东西要见面的。
# 而我们要做的和之前差不多还是写程序，逐行研究，弄懂它。
# 不过也有不同，我们本次不会直接运行所写的程序，而是要将它导入到 python 里通过执行函数的方式运行。

# 新知识
# 本题会遇到几个新的的函数、方法，我估计有可能后续题目会讲解，先说一下基本功能吧。
# 本题的 3 个新函数除一个 sorted 是python 的内置函数，用起来和 print 类似，直接在括号中加合法的参数就能使用外。
# 另外两个都要只对特定的对象起作用，它们使用的时候类似 open 打开的文件，是用“点分”格式调用的：

# split：它是字符串的一个方法，作用是把字符串拆成一个一个的单词，放在中括号中（叫做列表 【list】，
#         后续介绍 ）并以逗号分隔。至于以什么标准来拆则在参数中定义。
# 例如以逗号分割字符串：
s = '111,sss,bbb'
s.split(',')
# 结果是 ['111', 'sss', 'bbb']


# sorted: 把参数中的内容按照升序排列，并且生成一个新的列表（list）
sorted(s)
# 结果为 [',', ',', '1', '1', '1', 'b', 'b', 'b', 's', 's', 's']
s = sorted(s.split(','))
# 结果为：['111', 'bbb', 'sss']


# pop(整数): 它是列表(list)的一个方法，会从列表中指定位置（默认是末尾）拿出一个元素并返回。
#            不过我们可以在参数中指定从什么位数拿东西出来。我们也可以先思考一下练习中的
#            pop(-1)和pop(0)代表的究竟是什么位置？（提示，计算机不是从1开始数的）
s.pop(-1)
# 结果为：'sss'
# 详细讲解见本习题最后


def break_words(stuff):
    """
    This function will break up words for us.
    这个函数会为我们拆分出单词
    """
    words = stuff.split(' ')
    return words


def sort_words(words):
    """
    Sorts the words.
    对单词进行排序
    """
    return sorted(words)


def print_first_word(words):
    """
    Prints the first word after popping it off.
    抛出第一个单词并打印
    """
    word = words.pop(0)
    print(word)


def print_last_word(words):
    """
    Prints the last word after popping it off.
    抛出最后一个单词并打印
    """
    word = words.pop(-1)
    print(word)


def sort_sentence(sentence):
    """
    Takes in a full sentence and returns the sorts words.
    输入完整的句子，并返回排序后的单词
    """
    words = break_words(sentence)
    return sort_words(words)


def print_first_and_last(sentence):
    """
    Prints the first and last words of the sentence.
    打印句子的第一个和最后一个单词
    """
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)


def print_first_and_last_sorted(sentence):
    """
    Sorts the words then prints the first and last one.
    打印排序后的句子的第一个和最后一个单词
    """
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)


# 运行结果（这里使用了 ipython 这个增强型的 python 命令行）：
# PS C:\Users\12409\AppData\Roaming\Atom\file> ipython
# Python 3.6.6 (v3.6.6:4cf1f54eb7, Jun 27 2018, 03:37:03) [MSC v.1900 64 bit (AMD64)]
# Type 'copyright', 'credits' or 'license' for more information
# IPython 7.4.0 -- An enhanced Interactive Python. Type '?' for help.

# In [1]: import ex25
# ['This', 'is', 'string', 'example....wow!!!']
# ['Th', 's is string example....wow!!!']
# ['Th', 's ', 's str', 'ng example....wow!!!']
# ['This is string example....', 'o', '!!!']
# [1, 2, 3, 4, 5]
# [7, 6, 5, 4, 3, 2, 1, 0]
# [('a', 2, 1), ('b', 3, 3), ('c', 5, 4), ('d', 1, 5), ('e', 4, 2)]
# [('c', 5, 4), ('e', 4, 2), ('b', 3, 3), ('a', 2, 1), ('d', 1, 5)]
# [('a', 2, 1), ('e', 4, 2), ('b', 3, 3), ('c', 5, 4), ('d', 1, 5)]
# 列表删除的项为： Taobao
# 列表现在为： ['Google', 'Runoob']

# In [2]: sentence = "All good things come to those who wait."

# In [3]: words = ex25.break_words(sentence)

# In [4]: words
# Out[4]: ['All', 'good', 'things', 'come', 'to', 'those', 'who', 'wait.']

# In [5]: sorted_words = ex25.sort_words(words)

# In [6]: sorted_words
# Out[6]: ['All', 'come', 'good', 'things', 'those', 'to', 'wait.', 'who']

# In [7]: ex25.print_first_word(words)
# All

# In [8]: ex25.print_last_word(words)
# wait.

# In [9]: words
# Out[9]: ['good', 'things', 'come', 'to', 'those', 'who']

# In [10]: ex25.print_first_word(sorted_words)
# All

# In [11]: ex25.print_last_word(sorted_words)
# who

# In [12]: sorted_words
# Out[12]: ['come', 'good', 'things', 'those', 'to', 'wait.']

# In [13]: sorted_words = ex25.sort_sentence(sentence)

# In [14]: sorted_words
# Out[14]: ['All', 'come', 'good', 'things', 'those', 'to', 'wait.', 'who']

# In [15]: ex25.print_first_and_last(sentence)
# All
# wait.

# In [16]: ex25.print_first_and_last_sorted(sentence)
# All
# who

# In [17]: quit()

# 分析：
# 下面说的行以 ipython 的行号为准，输入输出使用一个行号。
# 第 1 行：import ex25 这里把我们刚刚写的脚本进行了引入，这和我们之前练习中引入库（模组、模块）的时候一样，
#         你也一定注意到了，我们引入的时候并不需要写后缀名 .py（后面跟的输出量是新知识点演示实例的输出结果）
# 第 2 行：我们把一句话装入了变量 sentence
# 第 3 行：调用了函数 ex25.break_words 。
#         其中 . 符号告诉 python ：“嗨，我要运行 ex25 里的那个叫做 break_words 的函数。
# 第 4 行：我们输出了 words 变量的内容（这个方法只在命令行模式有用）。
#         而在它的输出中我们看到的中括号 [] 的部分叫做列表（list)，我们在后面的练习会正式认识到它。
# 第 5-6 行：使用了 ex25.sort_words 得到了一个单词被排序后的句子sorted_words。
# 第 7-8 行：使用了ex25.print_first_word 和 ex25.print_last_word 将第一个和最后一个词打印出来。
# 第 9 行：再次输出 words 的内容，可以发现之前的首尾的单词都不见了（详见下文）
# 第 10-11 行 把排序句子的首尾单词打印出来
# 第 12 行：和第 9 行类似，打印出来发现首尾单词后它们也消失了
# 第 13-14 行 我们用了另一个方法 ex25.sort_sentence ，使用一个函数重新获取了排序句子。
# 第 15-16行：一样是一个函数，我们就分别得到了两种排序的首位单词。
# 第 17 行：quit()是在命令行中退出ipython的命令


# 新知识详细讲解
# split() 通过指定分隔符对字符串进行切片，如果参数 num 有指定值，则分隔 num+1 个子字符串
# split() 方法语法：

# str.split(str="", num=string.count(str))
# 参数说明：
# str -- 分隔符，默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等。
# num -- 分割次数。默认为 -1, 即分隔所有。
# 返回值：
# 返回分割后的字符串列表。
# 实例：
str = "This is string example....wow!!!"
print(str.split())  # 以空格为分隔符
print(str.split('i', 1))  # 以 i 为分隔符，返回两个参数列表
print(str.split('i'))  # 以 i 为分隔符
print(str.split('w'))  # 以 w 为分隔符

# 输出结果：
# ['This', 'is', 'string', 'example....wow!!!']
# ['Th', 's is string example....wow!!!']
# ['Th', 's ', 's str', 'ng example....wow!!!']
# ['This is string example....', 'o', '!!!']


# sorted() 函数对所有可迭代的对象进行排序操作。
# sort 与 sorted 区别：
# sort 是应用在 list 上的方法，sorted 可以对所有可迭代的对象进行排序操作。
# list 的 sort 方法返回的是对已经存在的列表进行操作，无返回值，
# 而内建函数 sorted 方法返回的是一个新的 list，而不是在原来的基础上进行的操作。
# sorted 语法：

# sorted(iterable, key=None, reverse=False)
# 参数说明：
# iterable -- 可迭代对象。
# key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，
#        指定可迭代对象中的一个元素来进行排序。
# reverse -- 排序规则，reverse = True 降序 ， reverse = False 升序（默认）。
# 返回值：
# 返回重新排序的列表。
# 实例：
# 先来展示一下sorted的最简单的使用方法
sorted([5, 2, 3, 1, 4])
# 结果：[1, 2, 3, 4, 5]
# 你也可以使用 list 的 list.sort() 方法。这个方法会修改原始的 list（返回值为None）。通常这个方法不如sorted()方便
# 但是如果你不需要原始的 list，list.sort()方法效率会稍微高一些。
a = [5, 2, 3, 1, 4]
a.sort()
print(a)
# 结果：[1, 2, 3, 4, 5]
# 另一个区别在于list.sort()方法只为list定义。而sorted()函数可以接收任何的iterable
sorted({1: 'D', 2: 'B', 3: 'B', 4: 'E', 5: 'A'})
# 结果为：[1, 2, 3, 4, 5]
# 利用key进行倒序排列
example_list = [5, 0, 6, 1, 2, 7, 3, 4]
result_list = sorted(example_list, key=lambda x: x * -1)
print(result_list)
# 结果为：[7, 6, 5, 4, 3, 2, 1, 0]
# 要进行反向排序，也通过传入第三个参数reverse=True：
example_list = [5, 0, 6, 1, 2, 7, 3, 4]
sorted(example_list, reverse=True)
# 结果为：[7, 6, 5, 4, 3, 2, 1, 0]


C = [('e', 4, 2), ('a', 2, 1), ('c', 5, 4), ('b', 3, 3), ('d', 1, 5)]
print(sorted(C, key=lambda y: y[0]))
print(sorted(C, key=lambda x: x[1] * -1))
print(sorted(C, key=lambda x: x[2]))
# 结果为：
# [('a', 2, 1), ('b', 3, 3), ('c', 5, 4), ('d', 1, 5), ('e', 4, 2)]
# [('c', 5, 4), ('e', 4, 2), ('b', 3, 3), ('a', 2, 1), ('d', 1, 5)]
# [('a', 2, 1), ('e', 4, 2), ('b', 3, 3), ('c', 5, 4), ('d', 1, 5)]
# 解析：
# C是一个由元组构成的列表，这时候就麻烦了，我们需要用到参数key，也就是关键词，看下面这句命令，
# key=lambda x: x[2])
# lambda是一个隐函数，是固定写法，不要写成别的单词；
# x表示列表中的一个元素，在这里，表示一个元组，x只是临时起的一个名字，你可以使用任意的名字；
# x[0]表示元组里的第一个元素，当然第二个元素就是x[1]，第三个元素就是x[2]；所以这句命令的意思就是按照列表中第三个元素排序
# x:x[]字母可以随意修改，排序方式按照中括号[]里面的维度进行排序，后面 *-1来实现倒序排列,但似乎对字母不起作用^-^


# pop() 函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值。
# pop()方法语法：

# list.pop([index=-1])
# 参数说明：
# index -- 可选参数，要移除列表元素的索引值，不能超过列表总长度，默认为 index=-1，删除最后一个列表值。
# 返回值
# 该方法返回从列表中移除的元素对象。
# 实例：
list1 = ['Google', 'Runoob', 'Taobao']
list_pop = list1.pop()
print("列表删除的项为：", list_pop)
print("列表现在为：", list1)
