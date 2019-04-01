# 习题六

# 在变量中使用格式化字符
types_of_people = 10
x = "There are %d types of people" % types_of_people
# 这里10是数字，不是字符串。如果是'10'就是字符串包含字符串了

# 在变量中使用格式化字符，并且格式化其他变量
binary = "binary"
do_not = "dont't"
y = "Those who know %s and those who %s" % (binary, do_not)  # 第一处和第二处字符串包含字符串

print(x)
print(y)
# 利用%r格式化字符显示原始字符的引号
# 打印字符串和格式化的变量
print("I said: %r." % x)  # 第三处字符串包含字符串
print("I also said: '%s'." % y)  # 第四处字符串包含字符串

# 格式化一个布尔型变量False
hilarious = "False"
joke_evaluation = "Isn't that joke so funny?! {}"
# 如同在注释中所写，这里是hilarious是布尔型变量，而非字符串

print(joke_evaluation.format(hilarious))

# 下面演示字符串的拼接打印
w = "This is the left side of..."
e = "a string with a right side."

print(w + e)

# python 的加分运算符 + 会尝试把两边的东西加在一起，即便不是数字。
# 如果两边是字符串，则做拼接也就是 ‘a’ + ‘b’ 等于 'ab'
# 如果是布尔型，则 False = 0 True = 1 进行运算
# 列表、元祖则同样做拼接变成一个列表或元祖
# 但是字典、集合不能用 + 拼接或相加
