# 习题六

# 在变量中使用格式化字符
types_of_people = 10
x = f"There are {types_of_people} types of people"
# 在变量中使用格式化字符，并且格式化其他变量
binary = "binary"
do_not = "dont't"
y = f"Those who know {binary} and those who {do_not}"

print(x)
print(y)
# 打印字符串和格式化的变量
print(f"I said: {x}")
print(f"I also said: '{y}'")

# 格式化一个布尔型变量False
hilarious = "False"
joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(hilarious))

# 下面演示字符串的拼接打印
w = "This is the left side of..."
e = "a string with a right side."

print(w + e)
