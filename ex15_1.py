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

# 实例2：遍历列表
verse = ['鹅鹅鹅', '曲项向天歌', '锄禾日当午', '春种一粒粟']

for i in verse:
    print(i)

print("\n")
# 可以获取下表，enumerate每次循环可以得到下表及元素
for i, v in enumerate(verse):
    print(i, v)

# 实例3：
