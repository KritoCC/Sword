# 习题三
print("I will now count my chickens:")  # 我现在数一数我的鸡：

print("Hens", 25 + 30 / 6)  # 母鸡 30.0
print("Roosters", 100 - 25 * 3 % 4)  # 雄鸡 97    其中'%'表示取余，即返回除法的余数

print("Now I will count the eggs:")  # 现在我要数鸡蛋：

print(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)  # 6.75

print("Is it true that 3 + 2 < 5 - 7?")  # 3 + 2 < 5 - 7是真的吗？

print(3 + 2 < 5 - 7)  # 对3 + 2和5 - 7的结果进行比较

print("What is 3 + 2?", 3 + 2)  # 3 + 2的结果是什么
print("What is 5 - 7?", 5 - 7)  # 5 + 7的结果是什么
print("Oh, that's why it's False.")  # 哦，这就是为什么它是假的。

print("How about some more.")  # 还有一些呢。

print("Is it qreater?", 5 > -2)  # 是大于吗?
print("Is it qreater or equal?", 5 >= -2)  # 是大于等于吗？
print("Is it less or equal?", 5 <= -2)  # 是小于等于吗？


# 7的意志
print(777777 * 77777 + 7777 - 777 / 77 % 7)


# 使用浮点数再计算一遍
# 和数学运算不同的地方是，Python的整数运算结果仍然是整数，浮点数运算结果仍然是浮点数
# 但是整数和浮点数混合运算的结果就变成浮点数了
# round(x, k) x为要处理的浮点数，k指要保留的位数

print("I will now count my chickens:")  # 我现在数一数我的鸡：

print("Hens", round(25 + 30 / 6, 3))  # 母鸡 30.0
# 雄鸡 97    其中'%'表示取余，即返回除法的余数
print("Roosters", round(100 - 25 * 3 % 4, 3))

print("Now I will count the eggs:")  # 现在我要数鸡蛋：

print(round(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6, 3))  # 6.75


# tip:转换为：
# 3*0.1 = 0.30000000000000004
# 为啥捏？
#
# 0.3 转换为二进制：
# 0.3 * 2 = 0.6 -> 0
# 0.6 * 2 = 1.2 -> 1
# 0.2 * 2 = 0.4 -> 0
# 0.4 * 0.2 = 0.8 -> 0
# 0.8 * 2 = 1.6 -> 1
# 0.6 * 2 = 1.2 -> 1
# 如此循环
#
# 所以 0.3 对应的二进制数为 0.01001100110011001 ……无限循环下去。
#
# 而电脑会把这个无限循环的东西截断为：0.0100110011001100110011001100110011001100110011001101
#
# 这个截断以后的二进制再转换回十进制，就变成了 0.30000000000000004