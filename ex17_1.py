# 习题十七巩固练习一

# 精简训练
# 之前写的脚本太烦人，没必要在做复制之前问你，也没必要在屏幕上输出那么多东西。
# 试着删除脚本的一些特性，让它用起来更加友好
from sys import argv

script, from_file, to_file = argv

# 一行读取源文件
indata = open(from_file).read()

# 一行写入
open(to_file, 'w').write(indata)
# 要友好么？就在完成的时候打印一句话吧
print("拷贝完成，共复制了%r个字" % len(indata))


# 这样一来只有读取和写入文件，其他提示都没有，如果文件存在则直接覆盖。
# 实际代码缩减到了5行，删除print的话只有4行


# 当你写了indata = open(from_file).read()，这意味着，在到达脚本结尾的时候，
# 你无须在运行in_file.close()或者from_file.close(),因为read()一旦运行，
# 文件就会被python关掉，想一下ex17.py里的from_file和to_filr文件也都没有close()
# 如果还要强行加上close()就会报错
