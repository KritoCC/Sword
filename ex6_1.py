# 习题六中关于str.format() 方法的详解

# 本节仅讲解str.format() 方法简单字段名的部分，复杂字段名等到后面用到再讲解

# 术语说明
# str.format() 方法通过字符串中的花括号 {} 来识别替换字段，从而完成字符串的格式化。
# 替换字段 由字段名和转换字段以及格式说明符组成，即一般形式为 {字段名!转换字段:格式说明符}。
# 字段名分为简单字段名和复合字段名。
# 而转换字段和格式说明符都是可选的。

# 简单字段名的三种写法：
# · 省略不写         {}
# · 数字      {十进制非负整数}
# · 变量名   {合法的Python标识符}

# 1.省略字段名
# 花括号内省略字段名，传递位置参数。
# · 替换字段形式： {}
# · 注意：花括号个数可以少与位置参数的个数，反之不然

# 省略字段名传递位置参数
print("我叫{}，今年{}岁。".format('小明', '18'))
# 换成习题六中的形式为
name = '小明'
year = '18'
introduction = "我叫{}，今年{}岁。"
print(introduction.format(name, year))

# 花括号个数可以少于位置参数的个数
print("我爱吃{}和{}。".format('香蕉', '苹果', '大鸭梨'))

# 花括号个数多于位置参数的个数则会出错
# print("我还吃{}和{}。".format('西红柿'))
"""
IndexError: tuple index out of range
"""


# 2.数字形式的简单字段名
# 可以通过数字形式的简单字段名传递位置参数
# · 数字必须是大于等于0的整数
# · 带数字的替代字段可以重复使用
# · 数字形式的简单字段名相当于把format中的所有位置参数整体当作一个元组，通过字段名中的数字进行取值
# · 即{0}等价于tuple[0],所以花括号内的数字不能越界

# 通过数字形式的简单字段名传递位置参数
print("身高{0}，家住{1}。".format(1.8, '铜锣湾'))

# 数字形式的简单字段名可以重复使用。
print("我爱{0}。\n她今年{1}。\n{0}也爱我。".format('小黑', 18))

# 体会把所有位置参数整体当成元组来取值
print('小黑爱吃{1}、{3}和{0}。'.format(
     '榴莲', '臭豆腐', '皮蛋', '鲱鱼罐头', '螺狮粉'))

# 尝试一下越界错误
# print('{1}'.format('错误用法'))
"""
IndexError: tuple index out of range
"""


# 3.变量名形式的简单字段名
# 使用变量名形式的简单字段名传递关键字参数
# · 关键字参数的位置可以随意切换

# 使用变量名形式的简单字段名传递关键字参数
print("我大哥是{name}，今年{age}岁。".format(name='阿飞', age=20))
# 关键字参数的顺序可以随意调换
print("我大哥是{name}，今年{age}岁。".format(age=20, name='阿飞'))


# 4.简单字段名的混合使用
# · 混合使用数字形式和变量名形式的字段名，可以同时传递位置参数和关键词参数。
# · 关键字参数必须位于位置参数之后
# · 混合使用时可以省略数字
# · 省略字段名{}不能和数字形式的字段名{非负整数}同时使用

# 混合使用数字形式和变量形式的字段名
# 可以同时传递位置参数和关键词参数
print("这是一个关于{0}、{1}和{girl}的故事。".format(
    '小明', '阿飞', girl='小黑'))
# 但是关键词参数必须位于位置参数之后
# print("这是一个关于{0}、{1}和{girl}的故事。".format(
#      '小明', girl='小黑', '阿飞'))
"""
SyntaxError: positional argument follows keyword argument
"""

# 数字也可以省略
print("这是一个关于{}、{}和{girl}的故事。".format(
    '小明', '阿飞', girl='小黑'))

# 但是省略字段名不能和数字形式的字段名同时出现
# print("这是一个{}、{1}和{girl}的故事。".format(
#     '小明', '阿飞', girl='小黑'))
"""
ValueError:
cannot switch from automatic field numbering to manual field specification
"""


# 5.使用远足和字典传参
# str.format() 方法还可以使用 *元组 和 **字典 的形式传参，两者可以混合使用。
# 位置参数、关键字参数、*元组 和 **字典 也可以同时使用，
# 但是要注意，位置参数要在关键字参数前面，*元组 要在 **字典 前面。

# 使用元组传参
infos = '钢铁侠', 66, '小辣椒'
print("我是{}，身价{}亿, 我爱{}。".format(*infos))

print("我是{0}，身价{1}亿，我爱{2}。".format(*infos))

# 使用字典传参
venom = {'name': '毒液', 'weakness': '火'}
print("我是{name}，我怕{weakness}。".format(**venom))

# 同时使用元组和字典传参
hulk = '绿巨人', '拳头'
captain = {'name': '美国队长', 'weapon': '盾'}
print('我是{}， 我怕{weapon}。'.format(*hulk, **captain))
print('我是{name}， 我怕{1}'.format(*hulk, **captain))

# 同时使用位置参数、元组、关键词参数、字典传参
# 注意：
# 位置参数必须在关键词参数前面
# *元组必须在**字典前面
tup = '鹰眼', '黑寡妇'
dic = {'weapon': '箭'}
text = '我是{1}，我怕{weakness}，我要{0}，我用{weapon}'
text = text.format(
    *tup, weakness='男人', **dic)
print(text)