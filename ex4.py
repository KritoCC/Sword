# 习题四

# 变量 简单理解就是给一段代码或值起个名字，这个名字就是变量了，
# 在编写代码的时候可以用变量名代指被命名的代码或值。
# 本题在前面 print() 函数以及运算符的基础上将值命名成为变量后进行运算并打印

# 表示汽车数量的变量
cars = 100
# 表示车内空间的变量
space_in_a_car = 4.0
# 表示司机数量的变量
drivers = 30
# 表示乘客数量的变量
passengers = 90
# 表示无法行驶的汽车数量的变量
cars_not_driven = cars - drivers
# 表示能行驶的汽车数量的变量
cars_driven = drivers
# 表示拼车容量的变量
carpool_capacity = cars_driven * space_in_a_car
# 表示平均每辆车的乘客数的变量
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")


# Traceback (most recent call last):
#  File "ex4.py", line 8, in <module>    告诉我们错误发生的位置在“ex4.py”文件的第8行。
#   average_passengers_per_car = car_pool_capacity / passenger   列出了错误行的内容
# NameError: name 'car_pool_capacity' is not defined
# 告诉我们错误类型是 NameError 变量名 car_pool_capacity 未被定义
