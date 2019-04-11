# 习题十五

# 本题本题开始涉及文件的操作，文件操作是一件危险的事情，
# 需要仔细细心否则可能导致重要的文件损坏。

# 本题除了 ex15.py 这个脚本以外，还需要一个用来读取的文件 ex15_sample.txt
# 其内容如下：
# This is stuff I typed into a file.
# It is really cool stuff.
# Lots and lots of fun to have in here.

# 我们需要用 python 脚本打开文件并打印出来，
# 不过我们不能把 ex15_sample.txt 写死在脚本中，
# 如果我们遇到其他文件要处理，写死的文件名会给我们带来麻烦
# 要利用之前练习过的 argv 和 input 从用户那里得知要处理的文件名。

# 载入sys.argv模块，以获得脚本运行参数
from sys import argv

# 将argv解包，并将脚本名赋值给变量script；将参数赋值给变量filename。
script, filename = argv

# 将名为"filename"的文件打开，并将打开的内容赋值给变量txt
txt = open(filename)

# 打印文件名，并在读取文件内容后打印
print("Here's your file %r:" % filename)
print(txt.read())

# ---------上面是通过argv获取文件名

# 以input方式让用户在脚本运行后输入文件名
print("Type the filename again:")
file_again = input("> ")

# 打开用户输入的文件
txt_again = open(file_again)

# 读取后打印用户输入文件的内容
print(txt_again.read())


# 运行结果：
# PS C:\Users\12409\AppData\Local\atom\file> python ex15.py ex15_sample.txt
# Here's your file 'ex15_sample.txt':
# This is stuff I type into a file.
# It id really cool stuff.
# Lots and lots of fun to have in here.
# Type the filename again:
# > ex15_sample.txt
# This is stuff I type into a file.
# It id really cool stuff.
# Lots and lots of fun to have in here.

# 解析：
# 17-22行使用argv我们相对比较熟悉了。
# 我们把open打开的文件赋值给变量txt
# 接着我们在打印了一句话后，在28行我们在txt这个被open打开的file（“文件”类型）类型的
# 变量上使用英文句号.调用了一个命令read，并且没有在括号中传递任何参数
# 句点A.B是python常用的调用函数的方法，其意义相当于调用A下拥有的B方法。
# 所以在本题中的意思大概就是说“嘿，txt! 你有一个‘方法’是read吧？执行它，不需要任何参数”。


# 补充1
# 文件对象提供了三个“读”方法： .read()、.readline() 和 .readlines()。
# 每种方法可以接受一个变量以限制每次读取的数据量，但它们通常不使用变量。
# .read() 每次读取整个文件，它通常用于将文件内容放到一个字符串变量中。
# 然而 .read() 生成文件内容最直接的字符串表示，
# 但对于连续的面向行的处理，它却是不必要的，并且如果文件大于可用内存，则不可能实现这种处理。
# .readline() 和 .readlines() 非常相似。它们都在类似于以下的结构中使用：
#         fh = open('c:\\autoexec.bat')
#          for  line in  fh.readlines():
#          print  line
# .readline() 和 .readlines() 之间的差异是后者一次读取整个文件，象 .read() 一样。
# .readlines() 自动将文件内容分析成一个行的列表，该列表可以由 Python 的 for ... in ... 结构进行处理。
# 另一方面，.readline() 每次只读取一行，通常比 .readlines() 慢得多。
# 仅当没有足够内存可以一次读取整个文件时，才应该使用 .readline()。


# 补充2
# Python 的 for ... in ... 结构，我在ex15_1.py里补充了


# 补充3
# open是一个新东西，我们可以通过pydoc open查看它的说明，补充如下：
# open(file, mode=’r’, buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
# (在使用该函数的时候，除了file参数必填外，其他参数可以选用。在本代码中对其他参数使用了默认值。)
# 在使用 open() 的时候，如果文件不存在，那么将会返回 IOError。
# 参数说明：
# file：文件名称；

# mode:制定了文件打开的方式，函数提供了如下方式，其中，'rt'为默认方式。
# 'r'       只读，默认方式
# 'w'       写入，会覆盖源文件内容
# 'x'       创建新文件，并写入内容，如果文件已存在，将会报错：FileExistsError
# 'a'       写入，如果文件有内容，则在末尾追加写入
# 'b'       二进制模式
# 't'       文本模式
# '+'       更新磁盘文件，读写
# 'U'       universal newline mode (deprecated)——在paython3中已经弃用

# buffering：用于设置缓存策略
# 在二进制模式下，使用0来切换缓冲；在文本模式下，通过1表示行缓冲（固定大小的缓冲区）。
# 在不给参数的时候，二进制文件的缓冲区大小由底层设备决定，
# 可以通过io.DEFAULT_BUFFER_SIZE获取，通常为4096或8192字节
# 文本文件则采用行缓冲。

# encoding：编码或者解码方式。
# 默认编码方式依赖平台，如果需要特殊设置，可以参考codecs模块，获取编码列表。

# errors：可选，并且不能用于二进制模式，
# 指定了编码错误的处理方式，可以通过codecs.Codec获得编码错误字符串

# newline：换行控制，参数有：None，'\n'，'\r'，'\r\n'。
# 输入时，如果参数为None，那么行结束的标志可以是：'\n'，'\r'，'\r\n'任意一个，
# 并且三个控制符都首先会被转化为：'\n'，然后才会被调用；
# 如果参数为''，所有的通用的换行结束标志都可以用，
# 但是行结束标识符返回调用不会被编码。
# 输出时，如果参数为None，
# 那么行结束的标志可以是：'\n'被转换为系统默认的分隔符；
# 如果是''，'\n'则不会被编码。

# closefd：false：文件关闭时，底层文件描述符仍然为打开状态，这是不被允许的，
# 所以，需要设置为ture

# opener：可以通过调用*opener*方式，使用自定义的开启器。
# 底层文件描述符是通过调用*opener*或者*file*, *flags*获得的。
# *opener*必须返回一个打开的文件描述。
# 将os.open作为*opener*的结果，在功能上，类似于通过None。
