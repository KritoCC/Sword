# 习题十五补充

# 循环结构(for-in)
# 说明：也是循环结构的一种，经常用于遍历字符串、列表，元组，字典等
# 格式：

# for x in y:
#     循环体

# 执行流程：x依次表示y中的一个元素，遍历完所有元素循环结束

# 实例1：遍历字符串
Love = "I love you more than i can say"
for i in Love:
    print(i)

print("\n")
# 实例2：遍历列表
verse = ['鹅鹅鹅', '曲项向天歌', '锄禾日当午', '春种一粒粟']

for i in verse:
    print(i)

print("\n")
# 可以获取下表，enumerate每次循环可以得到下表及元素
for i, v in enumerate(verse):
    print(i, v)

print("\n")
# enumerate英文翻译为枚举的意思。
# 可以将一个可遍历的数据对象组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。

# 实例3：遍历字典
dictionary = {'a': 'apple', 'b': 'banana', 'c': 'car', 'd': 'desk'}

print("字典值 : %s" % dictionary.items())

for key in dictionary:
    # 遍历字典时遍历的是键
    print(key, dictionary.get(key))

# get()方法语法：
# dict.get(key, default=None)
# key -- 字典中要查找的键。
# default -- 如果指定键的值不存在时，返回该默认值。
# 返回值: 返回指定键的值，如果值不在字典中返回默认值None。

print("\n")
# for key, value in dictionary.items():
# 上下两种方式等价 dictionary.items() <=> dict.items(dictionary)
for key, value in dict.items(dictionary):
    print(key, value)

print("\n")
# items()方法语法：
# dict.items()
# 以列表返回可遍历的(键, 值) 元组数组。

# range，用法如下:
# 可以生成从0开始到10的连续整数的迭代对象
print(range(10))
print("\n")
print(range(0, 10))
print("\n")
# 可以遍历
for i in range(10):
    print(i)

print("\n")
# 强制转换为列表
print(list(range(1, 11)))
print("\n")
# 列表生成式：快速生成具有特定规律的列表
print([i for i in range(1, 11)])
print([i * 2 for i in range(1, 11)])
print([i * i for i in range(1, 11)])
print([str(i) for i in range(1, 11)])
print([i for i in range(1, 11) if i % 2 == 0])
