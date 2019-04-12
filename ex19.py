# 习题十九

# 对于之前么有接触过的人来说，函数这个概念也许觉得有点摸不到头脑，
# Zed 为我们准备了下面的第19个练习，
# 他强调：函数里边的变量和脚本里边的变量之间是没有连接的。
# 让我们试着体会一下。


# 定义我们的函数，我们给参数起个名字
# 不过我们将在后面的调用时看到，
# 这个名字和引入参数时引入的变量名没关系
# 我们可以在24行和25行脚本变量命名的时候试验一下
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print("You have %r cheese!" % cheese_count)
    print("You have %r boxes of crackers!" % boxes_of_crackers)
    print("Man that's enough for a party!")
    print("Get a blanket.\n")


# 直接为函数传入参数
print("We can just give the funcation numbers directly:")
cheese_and_crackers(20, 30)

# 以变量方式将参数传入函数
print("OR, we can use variables from our script:")
amount_of_cheese = 10  # cheese_count = 10
amount_of_crackers = 50  # boxes_of_crackers = 50
# 如果我们把脚本变量的命名与函数变量的命名保持一致
# 发现脚本能正常运行，互不影响

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


# 函数的的参数可以进行计算
# 实际上是运算后传入函数的
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)


# 变量进行运算后作为函数的参数
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
