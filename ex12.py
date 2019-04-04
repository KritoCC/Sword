# 习题十二

# 前一题用 print() 打印问题，用input() 回答问题有点麻烦不是么？
# input() 就是要用户输入内容的，何不把提示功能加进去省去写 print() 语句的麻烦。
age = input("How old are you? ")
height = input("How tall are you? ")
weight = input("How much do you weight? ")

print("So, you're %s old, %s tall and %s heavy." % (age, height, weight))

# pydoc-文档生成工具
# 用途：
# 是python自带的一个文档生成工具，使用pydoc可以很方便的查看类和方法结构
# python中pydoc模块可以从python代码中获取docstring，然后生成帮助信息。
# 主要用于从python模块中自动生成文档，这些文档可以基于文本呈现的、
# 也可以生成WEB页面的，还可以在服务器上以浏览器的方式呈现！

# 方法：
# pydoc <name> ...
# 显示关于某事的文本文档。 <name>可以是a的名称 Python关键字，主题，功能，模块或包，
# 或点缀引用模块或模块中的类或函数包。
# 如果<name>包含'\\'，则将其用作a的路径 Python源文件到文档。
# 如果名称是'关键字'，'主题'，或“模块”，显示这些内容的列表。

# pydoc -k <keyword>
# 在所有可用模块的概要行中搜索关键字。

# pydoc -n <hostname>
# 使用给定的主机名启动HTTP服务器（默认值：localhost）。

# pydoc -p <port>
# 在本地计算机上的给定端口上启动HTTP服务器。港口
# 数字0可用于获取任意未使用的端口。

# pydoc -b
# 在任意未使用的端口上启动HTTP服务器并打开Web浏览器
# 以交互方式浏览文档。此选项可用于与-n和/或-p组合。

# pydoc -w <name> ...
# 将模块的HTML文档写入当前文件目录。如果<name>包含'\\'，则将其视为文件名;
# 如果它命名一个目录，为所有内容编写文档。

# 巩固练习
# 在命令行界面下运行你的程序，然后在命令行输入 python -m pydoc input
# 输入 q 退出 pydoc
# 使用 pydoc 看看 open、file 、 os 和 sys 的含义。
