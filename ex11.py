# 习题十一

# 本次练习还是和打印有关，不过要练习一个新东西 input() 这个函数让我们可以给 python 输入一些内容参与到程序的运行当中。

# 在每行print后面加上end=' '，告诉print不要用换行符结束这一行跑到下一行去
print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
height = input()
print("How much do you weight?", end=' ')
weight = input()

print("So, you're %r old, %r tall and %r heavy." % (age, height, weight))


# 如何读取用户输入的数并进行数学计算
print("输入第一个数：", end='')
first = int(input())
print("输入第二个数：", end='')
second = int(input())
ans = first + second

print("%d + %d = %d" % (first, second, ans))


# 在我们使用input的时候，会从标准输入中读取一个string，即字符串（请注意，这里很重要，下面我们会继续说），
# 对于用户输入的换行是不会读入的，因为我们都知道input是以换行作为输入结束的标志的

# 例一
# input从标准输入中为我们拿到的值是一个字符串，那么也就是说，无论我们的初衷是得到一个整数、小数或者其他的值，
# input都会在我们的输入的值的左右两边加上一个引号 " "
a = input("请输入：")
type_a = type(a)
print("a = %r" % a, type_a)

# 例二
# 我们来得到一个整数，很简单，只需要使用强制类型转换就可以了：
b = int(input("请输入："))
type_b = type(b)
print("b = %r" % b, type_b)

# 例三
# 刚刚在例一中说到了对于我们的输入，无论我们的初衷是什么，都会被加上一对引号，
# 所以我们如果把引号去掉了，这样的话我们是不是就会得到原来的东西了呢？
# 本例子中，我们想得到的是一个整数，这个时候你用eval除去input“添加”的引号是完全正确的。
# 其实，当我们输入的时候，eval帮我们去除了引号后，就相当于执行了c = □□（□□代表任意数），显然这是整数赋值。
# 而如果没有加eval，只是单纯的c = input("请输入:")，显然，我们得到的是c = "□□"。
c = eval(input("请输入："))
type_c = type(c)
print("c = %r" % c, type_c)

# 例四
# 看到这个例子，我想先让大家回忆一下我们,使用过的赋值语句：d, e = □□, □□。（□□代表任意数）
# 对于这个语句，大家在类比到本例中的eval的输入，在输入的时候，我输入的是“□□, □□”，
# 那么，在eval会去除input“强加”的引号的时候，是不是等价于“d, e = □□, □□”这个赋值语句！
# 所以，在这里我想通过这两个例子展现一下eval的本质，那就是"单纯"的替我们去出引号，
# 大家可以当做eval执行后将引号里面的内容原原本本地写回了代码的原来位置，那么这一切是不是就可以看得很明白了。
d, e = eval(input("请输入两个数(以英文逗号隔开)："))
print("d = %r" % d, "\ne = %r" % e)

# 关于eval的文章可以参考https://blog.csdn.net/qq_29883591/article/details/53443062
