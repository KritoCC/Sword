# 习题二十四

# 据说我们来到 24 题就已经距离第一部分的结束不远了。
# 我们学习了如何打印 print 还能够同时运用格式化字符 % 和转义字符 \ ，
# 我们也已经能够写一些函数 def ，并且知道如何把写好的脚本引入当前脚本 import ……
# Zed 认为我们还需要练习来巩固学过的知识，我想不会有人觉得更多的练习不好，
# 那么本题将是一个比较长的练习，据说下一题也是。

# 开场问候一下
print("Let's practice everthing.")

# 转义字符练习，这里还有一个英文口语知识点=.= 'bout == about
print('You\'d need to know \'bout escapes with \\ that do \nnewlines and \t tabs.')

# 用不熟悉的知识点么,有记得不太清楚的可以看一下习题二十二
poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""


print("---------------")
print(poem)
# 分割线我喜欢这么用
print("-" * 15)

# 变量
five = 10 - 2 + 3 - 6
# 格式化字符
print("This should be five: %s" % five)


# 函数来了，还悄悄告诉我们如何return多个值
def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


# 函数的调用与解包
start_point = 10000
beans, jars, crates = secret_formula(start_point)

print("With a starting point of: %d" % start_point)
print("We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates))

# 使用变量进行运算，改变变量的值，然后...
start_point = start_point / 10
print("We can also do that this way:")

# 更厉害了，直接在格式化字符的时候使用调用函数并把返回的值解包各格式化字符
print("We'd have %d beans, %d jars, and %d crates." %
      secret_formula(start_point))
