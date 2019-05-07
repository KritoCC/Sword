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

# 有关列表、字典、元组、集合的定义与具体用法在https://blog.51cto.com/12970189/2337202有详述
# 这里只是简单提一下：

# 列表的特点：列表是有序的，列表可以有重复的值
# 列表在python里是有序集合对象类型。
# 列表里的对象可以是任何对象：数字，字符串，列表或者字典，元组。与字符串不同，列表是可变对象，支持原处修改的操作
# python的列表是：
# 任意对象的有序集合
# 通过偏移读取
# 可变长度、异构以及任意嵌套
# 属于可变序列的分组
# 对象引用数组

# 字典在python里是无序集合对象类型。
# 字典的值都有独立的唯一的键，用相应的键来取值。
# python字典主要特性如下：
# 通过键而不是偏移量来读取
# 任意对象的无序组合
# 可变长，异构，任意嵌套
# 属于可映射类型
# 对象引用表
# 字典用法注意事项：
# 序列运算无效——串联，分片不能使用
# 对新索引（键）赋值会添加项
# 键不一定是字符串——只要是不可变的对象（列表字典除外）

# 元组与列表非常类似，只是不能在原处更改，元祖在python里的特点：
# 任意对象的有序组合
# 通过偏移取数据
# 属于不可变序列类型
# 固定长度，异构，任意嵌套
# 对象引用的数组

# 集合是一个无序且不重复的元素集合
# 集合对象是一组无序排列的可哈希的值，集合成员可以做字典中的键。
# 集合也支持用in 和not in操作符检查成员，由于集合本身是无序的，不可以为集合创建索引或执行切片操作，也没有键可用来获取集合中元素的值。
# 集合特点
# 集合中的元素和字典中的键一样不重复
# 集合中的元素为不可变对象


# 我们已经了解了Python支持布尔类型的数据，布尔类型只有True和False两种值，但是布尔类型有以下几种运算：
# 与运算：只有两个布尔值都为 True 时，计算结果才为 True。
# True and True   # ==> True
# True and False   # ==> False
# False and True   # ==> False
# False and False   # ==> False
# 或运算：只要有一个布尔值为 True，计算结果就是 True。
# True or True   # ==> True
# True or False   # ==> True
# False or True   # ==> True
# False or False   # ==> False
# 非运算：把True变为False，或者把False变为True：
# not True   # ==> False
# not False   # ==> True
# 布尔运算在计算机中用来做条件判断，根据计算结果为True或者False，计算机可以自动执行不同的后续代码。

# 在Python中，布尔类型还可以与其他数据类型做 and、or和not运算，请看下面的代码：
# a = True
# print a and 'a=T' or 'a=F'
# 计算结果不是布尔类型，而是字符串 'a=T'，这是为什么呢？
# 因为Python把0、空字符串''和None看成 False，其他数值和非空字符串都看成 True，所以：
# True and 'a=T' 计算结果是 'a=T'
# 继续计算 'a=T' or 'a=F' 计算结果还是 'a=T'
# 要解释上述结果，又涉及到 and 和 or 运算的一条重要法则：短路计算。
# 1. 在计算 a and b 时，如果 a 是 False，则根据与运算法则，整个结果必定为 False，因此返回 a；
#    如果 a 是 True，则整个计算结果必定取决与 b，因此返回 b。
# 2. 在计算 a or b 时，如果 a 是 True，则根据或运算法则，整个计算结果必定为 True，因此返回 a；
#    如果 a 是 False，则整个计算结果必定取决于 b，因此返回 b。
# 所以Python解释器在做布尔运算时，只要能提前确定计算结果，它就不会往后算了，直接返回结果。
