# 习题二十二

# 本次习题没有任何代码，只能算作是一个大的巩固练习
# 请完成一个表格，回顾到目前为止你已经学到的所有内容
# 回到每一个习题的脚本里，把你遇到的每一个词和每一个符号写下来，并加以解释

# 习题一、习题二
"""
'#' 这两节习题中最重要的就是就是这个井号，它也是我们以后会一直用到的，作用就是注释代码
"""

# 习题三
"""
本节主要讲python中常用的运算符
+：    加号
-：    减号
/：    除法
%：    取余
//：   整除
*：    乘法
**：   幂运算
<：    小于
>：    大于
<=：   小于等于
>=：   大于等于
"""

# 习题四
"""
记住 = 的作用是为数据取名。
记住 == 的作用是检查左右两边的值是否相等
记住 _ 是下划线字符
"""

# 习题五
"""
f"Hello {somevar}" 这种f、引号和{ }的组合相当于告诉Python：“嘿， 这是一个格式化字符串，把这些变量放在那几个位置。”

还学习了Python常用的格式化字符
%s   格式化为字符串
%r   格式化为原始数据
%d   格式化为十进制整数
%c   将数字转换成其unicode对应的值，10进制范围为0 <= i <= 1114111
     Unicode（统一码、万国码、单一码）是计算机科学领域里的一项业界标准，包括字符集、编码方案等。
     Unicode 是为了解决传统的字符编码方案的局限而产生的，它为每种语言中的每个字符设定了统一并且唯一的二进制编码,
     以满足跨语言、跨平台进行文本转换、处理的要求。
%o   格式化为八进制整数
%x   格式化为十六进制整数
%X   格式化为十六进制整数（大写）
%f   格式化为浮点数，可以用m.n控制最小长度(m)和最小小数位(n)
%e   使用科学计数法表示浮点数
%E   同 %e 但e为大写
%g   以十进制或科学计数法表示浮点数
%G   同 %g 但e为大写
"""

# 习题六
"""
在python中""和''都可以用来表示一个字符串
但是有很多注意事项
原来的字符串中有一个'，而Python又允许使用单引号' '来表示字符串，所以字符串中间的'必须结合转移字符使用才可以
故字符串中的'应写为\'才可以
当你用单引号' '定义字符串的时候，它就会认为你字符串里面的双引号" "是普通字符，从而不需要转义
反之当你用双引号定义字符串的时候，就会认为你字符串里面的单引号是普通字符无需转义

记住"""  """和''' '''用于使字符串一行一行依次输出

本节还讲了 + 在python中会尝试把两边的东西加在一起，即便不是数字
不论是字符串、布尔型(False和True)、列表、元祖都能被拼接拼接起来，当然应该是同种类型的
但是字典、集合不能用 + 拼接或相加

格式化方式，目前我自己已知的三种：
1.f-string类型，形式为： f"Some stuff here {avariable}"
2.运用格式化字符，形式为： "Some stuff here %s" % avariable
3.str.format()方法，形式为： "Some stuff here {}".format(avariable)
"""

# 习题十
"""
学习了Python常用的转义字符：
"""
# \n	     ASCII 换行符
# \\	     反斜杠（ \ )
# \' 和 \"   表示引号（ ' 和 "）
# \（在行末） 不换行
# \t	     ASCII 横向制表符
# \v	     ASCII 纵向制表符
# \a	     ASCII 响铃
# \b	     ASCII 退格(将后面的字符前移)
# \e	     转义 官网上没有这个东西，不知道众网友都哪来的
# \000	     空（但不是空格）
# \r	     ASCII 回车（效果类似 \b 但是看起是光标退掉整行内容，移动到了本行开头位置后输出后面的内容）
# \f	     换页(据说在有些终端会清空屏幕）
# \ooo	     八进字符，ooo代表的字符的值，例如：\044是美元符$
# \xhh	     十六进制字符，hh代表的字符的值，例如：\x44是大写D

# 习题十一
"""
input()函数接受任意输入，但是默认都作为字符串处理
int(input())强制将输入的内容转换为整数形式
eval(input())将去掉输入内容的两个引号，来获取用户输入的数字

end=''作为print()BIF的一个参数，会使该函数关闭“在输出中自动包含换行”的默认行为。
其原理是：为end传递一个空字符串，这样print函数不会在字符串末尾添加一个换行符，而是添加一个空字符串。
这个只有Python3有用，Python2不支持。
"""

# 习题十二
"""
前一题用 print() 打印问题，用input() 回答问题有点麻烦不是么？
input() 就是要用户输入内容的，何不把提示功能加进去，从而省去写 print() 语句的麻烦。

pydoc 是 python 的一个文档帮助系统，
可以在命令行界面和浏览器中读取并呈现模块、类、函数、方法中的 __doc__ 属性中保存的文档。
在命令行输入pydoc input即可进行查找
"""

# 习题十三
"""
import语句的作用是引用我们（python自带的、其他人写的）已经写好的程序、“功能”，
能使这些“功能”可以在当前脚本中使用。

import有两种用法
*引入全部模块：import sys
*引入部分模块：from sys import argv
"""

# 习题十五
"""
句点A.B是python常用的调用函数的方法，其意义相当于调用A下拥有的B方法

open(file, mode=’r’, buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
(在使用该函数的时候，除了file参数必填外，其他参数可以选用。)
mode:制定了文件打开的方式，函数提供了如下方式，其中，'rt'为默认方式。
'r'       只读，默认方式
'w'       写入，会覆盖源文件内容
'x'       创建新文件，并写入内容，如果文件已存在，将会报错：FileExistsError
'a'       写入，如果文件有内容，则在末尾追加写入
'b'       二进制模式
't'       文本模式
'+'       更新磁盘文件，读写

.read() 每次读取整个文件，它通常用于将文件内容放到一个字符串变量中
.readline() 和 .readlines() 之间的差异是后者一次读取整个文件，象 .read() 一样。
.readline() 每次只读取一行，通常比 .readlines() 慢得多，仅当没有足够内存可以一次读取整个文件时，才应该使用 .readline()。
.readlines() 自动将文件内容分析成一个行的列表，该列表可以由 Python 的 for ... in ... 结构进行处理。

for...in..循环结构
说明：也是循环结构的一种，经常用于遍历字符串、列表，元组，字典等
格式：
for x in y:
    循环体

执行流程：x依次表示y中的一个元素，遍历完所有元素循环结束
"""

# 习题十六
"""
.truncate()的作用是将文件截断指定 size 字节,
本习题中没有指定truncate()的大小，所以实际上是清空了文件的内容

.write()将内容写入文件

.close()关闭文件。如同编辑器中 文件 -> 保存 的作用。

.seek(0)将读写位置移动到文件开头
"""
print("Type the filename again:")
file_again = input("> ")

# 打开用户输入的文件
txt_again = open(file_again)

# 读取后打印用户输入文件的内容
txt_again.seek(1, 1)
print(txt_again.tell())
print(txt_again.read())
