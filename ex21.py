# 习题二十一


# 前面的函数练习中，我们给函数撰写了 print() 语句使函数可以把运行后的结果打印出来。
# 不过我们并不总是需要把结果打印出来，在实际编写程序的时候我们更多的是需要使用函数的结果做其他事情（而不是打印出来）。
# 这就是本题的一个重点 return 的使用。
# 先看个小例子，并且简单说明一下：
def my_add(a, b):
    """
    其实这里可以用三引号写函数的说明文档的。但是也要遵循缩进原则
    就像我们用help或者pydoc查看的内容一样。
    这个函数实现了两个数字相加的功能
    """
    return a + b


# 接下来调用看看
my_add(2, 3)

# 打印函数看看
print(my_add(2, 3))

# 删除三行注释之后这个函数只有两行内容，第一行我们比较熟悉了：定义了一个拥有两个参数的函数my_add。
# 我们来看第二行代码：
# 1.调用了函数的两个参数：a和b
# 2.然后让两个参数执行加法运算a + b
# 3.最后python会执行返回return， 把a + b的结果返回来
# python 在执行这个函数的时候会把合法的两个参数做相加，并把结果返回。
# 这里有个问题，返回到哪了？看一下两次调用的结果。
# 可以看到，我们明明调用了 my_add 两次，应该有两次 return ，但是屏幕上却只有一个结果被打印了。
# 事实上 return 的结果是在内存中的，如果没人使用这个返回的结果，
# 则这个结果将被 python 的垃圾回收机制清除掉来腾出可用内存。
# 所以通常情况下，我们会为结果赋值，用一个变量表示结果并等待被使用；
# 或者如本例直接使一个函数被另一个当作参数来用。


def add(a, b):
    print("ADDING %d + %d" % (a, b))
    return a + b


def subtract(a, b):
    print("SUBTRACT %d - %d" % (a, b))
    return a - b


def multiply(a, b):
    print("MULTIPLY %d * %d" % (a, b))
    return a * b


def divide(a, b):
    print("DIVIDE %d / %d" % (a, b))
    return a / b


print("Let's do some math with just functions!")

age = add(25, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print("Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq))

# A puzzle for the extra credit, type it in antway.
print("Here is puzzle.")

what = add(age, subtract(height, (multiply(weight, divide(iq, 2)))))

print("That becomes:", what, "Can you do it by hand?")

# 谜题：
# what = add(age, subtract(height, (multiply(weight, divide(iq, 2)))))
# 这个谜题其实只是一个多层嵌套引用函数的语句，
# 由一个函数的结果作为另一个函数的参数，而这个函数的结果又是其他函数的参考。
# 看起来比较乱，但拆开步骤的话和前面的没什么区别。
iq_1 = divide(iq, 2)
weight_1 = multiply(weight, iq_1)
height_1 = subtract(height, weight_1)
age_1 = add(age, height_1)
what_1 = age_1
print("That becomes:", what_1)

# 颠倒过来做一次
what_2 = divide(iq, multiply(weight, subtract(height, add(age, 5))))
print("That becomes:", what_2)

# 写一个简单的公式，一样使用函数来计算
# 24 + 34 / 100 - 1023
what_3 = subtract(add(24, divide(34, 100)), 1023)
print("The result is:", what_3)

# 输出结果为：
# DIVIDE 34 / 100
# ADDING 24 + 0  注意此处并不是0，而是0.34，因为我前面设置%d，打印为整数，但是运算的时候还是照0.34
# SUBTRACT 24 - 1023  将add函数里面的第二个数的输出格式改为%.3f就能够打印出小数了
# The result is: -998.66
