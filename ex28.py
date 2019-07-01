# 习题二十八

# 上题我们学习了不少逻辑表达式，但是他们还有另一个更正式的名字——布尔逻辑表达式（boolean logic expression)。
# 它们无处不在非常重要，所以本题将要练习它们。
# 我们要做的是判断下列表达式的结果是 True 还是 False，并在 python 环境中验证结果：
# True and True
# False and True
# 1 == 1 and 2 == 1
# “test” == “test”
# 1 == 1 or 2 != 1
# True and 1 == 1
# False and 0 != 0
# True or 1 == 1
# “test” == “testing”
# 1 != 0 and 2 == 1
# “test” != “testing”
# “test” == 1
# not (True and False)
# not (1 == 1 and 0 != 1)
# not (10 == 1 or 1000 == 1000)
# not (1 != 10 or 3 == 4)
# not (“testing” == “testing” and “Zed” == “Cool Guy”)
# 1 == 1 and not (“testing” == 1 or 1 == 0)
# “chunky” == “bacon” and not (3 == 4 or 3 == 3)
# 3 == 3 and not (“testing” == “testing” or “Python” == “Fun”)


# 1. True and True
print('True and True' + '是真是假？我的答案是' + 'True')
print(True and True, "\n" * 2)

# 2. False and True
print('False and True' + '是真是假？我的答案是' + 'False')
print(False and True, "\n" * 2)

# 3. 1 == 1 and 2 == 1
print('1 == 1 and 2 == 1' + '是真是假？我的答案是' + 'False')
print(1 == 1 and 2 == 1, "\n" * 2)

# 4. "test" == "test"
print('"test" == "test"' + '是真是假？我的答案是' + 'True')
print("test" == "test", "\n" * 2)

# 5. 1 == 1 or 2 != 1
print('1 == 1 or 2 != 1' + '是真是假？我的答案是' + 'True')
print(1 == 1 or 2 != 1, "\n" * 2)

# 6. True and 1 == 1
print('True and 1 == 1' + '是真是假？我的答案是' + 'True')
print(True and 1 == 1, "\n" * 2)

# 7. False and 0 != 0
print('False and 0 != 0' + '是真是假？我的答案是' + 'False')
print(False and 0 != 0, "\n" * 2)

# 8. True or 1 == 1
print('True or 1 == 1' + '是真是假？我的答案是' + 'True')
print(True or 1 == 1, "\n" * 2)

# 9. "test" =="testing"
print('"test" == "testing"' + '是真是假？我的答案是' + 'False')
print("test" == "testing", "\n" * 2)

# 10. 1 != 0 and 2 == 1
print('1 != 0 and 2 == 1' + '是真是假？我的答案是' + 'False')
print(1 != 0 and 2 == 1, "\n" * 2)

# 11. "test" != "testing"
print('"test" != "testing"' + '是真是假？我的答案是' + 'True')
print("test" != "testing", "\n" * 2)

# 12. "test" == 1
print('"test" == 1' + '是真是假？我的答案是' + 'False')
print("test" == 1, "\n" * 2)

# 13. not (True and False)
print('not (True and False)' + '是真是假？我的答案是' + 'True')
print(not (True and False), "\n" * 2)

# 14. not (1 == 1 or 0 != 1)
print('not (1 == 1 or 0 != 1)' + '是真是假？我的答案是' + 'False')
print(not (1 == 1 or 0 != 1), "\n" * 2)

# 15. not (10 == 1 or 1000 == 1000)
print('not (10 == 1 or 1000 == 1000)' + '是真是假？我的答案是' + 'False')
print(not (10 == 1 or 1000 == 1000), "\n" * 2)

# 16. not (1 != 10 or 3 == 4)
print('not (1 != 10 or 3 == 4)' + '是真是假？我的答案是' + 'False')
print(not (1 != 10 or 3 == 4), "\n" * 2)

# 17. not ("testing" == "testing" and "Zed" == "Cool Guy")
print('not ("testing" == "testing" and "Zed" == "Cool Guy")' + '是真是假？我的答案是' + 'True')
print(not ("testing" == "testing" and "Zed" == "Cool Guy"), "\n" * 2)

# 18. 1 == 1 and not ("testing" == 1 or 1 == 0)
print('1 == 1 and not ("testing" == 1 or 1 == 0)' + '是真是假？我的答案是' + 'True')
print(1 == 1 and not ("testing" == 1 or 1 == 0), "\n" * 2)

# 19. "chunky" == "bacon" and not (3 == 4 or 3 == 3)
print('"chunky" == "bacon" and not (3 == 4 or 3 == 3)' + '是真是假？我的答案是' + 'False')
print("chunky" == "bacon" and not (3 == 4 or 3 == 3), "\n" * 2)

# 20. 3 == 3 and not ("testing" == "testing" or "Python" == "Fun")
print('3 == 3 and not ("testing" == "testing" or "Python" == "Fun")' + '是真是假？我的答案是' + 'False')
print(3 == 3 and not ("testing" == "testing" or "Python" == "Fun"), "\n" * 2)


# 比较运算符       名字
# ==              等于
# !=              不等于
# <               小于
# >               大于
# <=              小于等于
# >=              大于等于


# 例子
print(False and 1)
print(False and True)
print(True and 1)
print(True or 1)
print(False or 1)
print(True + True)
print('' or 5 or 0)
# 出现以上情况的原因是什么呢？
print(bool(''))  # False
print(bool(0))  # False
# 所有变量的位操作都是通过强制转换成bool(布尔类型)实现的，并且表达式的值是从左到右第一个能够确定表达式的值的变量。
# ('' or 5 or 0) == (False or True or False),
# 当遇到第一个True的时候，表达式的值等于True这个变量（5）的值，并且不会再去管后面是什么，所以返回5.
# 原则
# 1. 在纯and语句中，如果每一个表达式都不是假的话，那么返回最后一个，因为需要一直匹配直到最后一个。
#    如果有一个是假，那么返回假
# 2. 在纯or语句中，只要有一个表达式不是假的话，那么就返回这个表达式的值。只有所有都是假，才返回假
# 3. 在or和and语句比较难表达，总而言之，碰到and就往后匹配，碰到or如果or左边的为真，那么就返回or左边的那个值，
#    如果or左边为假，继续匹配or右边的参数。
# (False or 1)   输出1
# (1 or False)   输出1
# (True or 1)    输出前者
# (1 or True)    输出前者
# (True and 1)   输出后者
# (1 and True)   输出后者
# (False and 1)  输出False
# (1 and False)  输出False
# 对python而言
# 　　其一, 在不加括号时候, and优先级大于or
# 　　and运算有假则取假，如果没有假则取最后一个真（需要保证为真，则需要运算打最后一个真）
# 　　or运算会取从左到右的第一个真，如果没有就取假
# 　　其二, x or y 的值只可能是x或y. x为真就是x, x为假就是y
# 　　第三, x and y 的值只可能是x或y. x为真就是y, x为假就是x
# 显然,
# 　　对于, 1 or 5 and 4: 先算5 and 4, 5为真, 值为4. 再算1 or 4, 1 为真,值为1
# 　　对于, (1 or 5) and 4: 先算1 or 5, 1为真, 值为1. 再算1 and 4, 1为真,值为4
# 在Python中，空字符串为假，非空字符串为真。非零的数为真。
# 数字和字符串之间、字符串之间的逻辑操作规律是：
# 对于and操作符：
# 　　只要左边的表达式为真，整个表达式返回的值是右边表达式的值，否则，返回左边表达式的值
print(2 and 1)
print(2 and '')
print(1 and 2)
print(0 and 1)
# 对于or操作符：
# 　　只要两边的表达式为真，整个表达式的结果是左边表达式的值。
print(1 or 2)
print(True or 1)
# 　　如果是一真一假，返回真值表达式的值
print('' or 5)
print(5 or '')
print(0 or 5)
print(5 or 0)
# 　　如果两个都是假，比如空值和0，返回的是右边的值。（空值或0）
print('' or False)
print(False or '')
print('' or 0)
print(0 or '')
# 总结一句话就是：无论操作符是哪个，最后的结果一定是按照计算顺序能最快判断出结果的那个表达式决定的
