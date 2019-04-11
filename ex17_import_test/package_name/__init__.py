# 不建议在__init__中写python模块，可以在包中在创建另外的模块来写，尽量保证__init__.py简单
# __init__.py文件导入"package_name"中的"hello"模块

# from . import hello

print("This is package_name.__init__.py")

# 错误总结1
# 不能写成from package_name import hello
# 因为__init__.py就在package_name这个包里，导入的时候会出现找不到package_name包的情况
# 会把package_name看成是模块来导入，而找不到package_name模块就会报错

# 错误总结2
# 不能写成import hello
# 因为__init__.py就在package_name这个包里，所以在导入hello模块的时候
# 系统能直接找到hello模块的位置，从而能顺利运行；但当__init__.py模块被其他程序导入时，
# 就会因为找不到hello模块的位置，导致出错。

# 错误总结3
# 不能写成from . import hello
# 因为不能在包的内部直接执行
# 我们可以在package_name包同级目录下module_test03.py测试看看效果
# from package_name import hello
# 可以达到效果
# from . import,  "."  代表使用相对路径导入，即从当前项目中寻找需要导入的包或函数
