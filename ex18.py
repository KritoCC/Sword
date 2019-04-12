# 习题十八

# 新知识：
# 函数是一段可以重复运行的代码片段，使用函数可以提高一段代码的重复利用性，
# 减少代码量，并且提高效率。
# python 中定义函数有特定个格式，总是以 def 开头，
# 后跟一个空格后是函数的名字，紧跟名字的是一对括号和冒号，
# 如果这个函数有参数的话需要写在括号内，多个函数用逗号隔开。
# 然后，在另起一行，和 def 起始位置相距 4 个空格 （缩进 4 个空格）的地方开始写函数的功能，
# 取消 4 个空格则表示函数定义结束。

# 例如一个把任意数字加一后打印的函数看起来可能像这样：


# 定义函数
def plus_one(number):
    new_number = number + 1
    print(new_number)


# 使用函数
plus_one(5)

# 结果将会是：6

# 函数可以做三样事情：

# 1. 它们给代码片段命名，就像“变量”给字符串和数字命名一样。
# 2. 它们可以接受参数，就跟你的脚本接受 argv 一样。
# 3. 通过使用 1 和 2，它们可以让你创建“迷你脚本”或者“小命令”


# 这就和我们的脚本使用argv一样
def print_two(*args):
    arg1, arg2 = args
    print("arg1: %r, arg2: %r" % (arg1, arg2))


# 实际上参数*args是没什么意义的，但我们实际可以这样写
def print_two_again(arg1, arg2):
    print("arg1: %r, arg2: %r" % (arg1, arg2))


# 这个是一个参数的
def print_one(arg1):
    print("arg1: %r")


# 这是没有参数的
def print_none():
    print("I got nothin'.")


# 下面是调用函数的演示
# 不去使用函数的话，它们是不会打印任何东西出来的。
print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()
