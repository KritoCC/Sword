# 习题二十七

# 你以为期中考试过后会有一个小假期轻松一下？那就在想想错了！
# Zed 大神为我们安排了一个为期一周的作业题目——背熟本题即将介绍的一系列的逻辑表格。

# 要点：
# · 不可擅自缩短本题完成时间。
# · 不可擅自缩短本题完成时间。
# · 不可擅自缩短本题完成时间。
# · 一定熟记这些逻辑关系，做到如同条件反射一般看到问题就知道它的答案。
# · 少吃多餐，分多次记忆，一次一点，重点反复记忆弱点项目。

# 我们在中学的时候应该都学过一些逻辑意义（与或非），在各种编程语言中也会在某些地方进行逻辑判断，
# 以确定一段字符、变量或者它们的组合所表达的结果是“真” （True） 的意思还是”假” （False）的意思。
# Python 会用到下面的这些术语或叫逻辑操作符来表达这些意思。

"""
逻辑操作符     意义               例子        结果
True        表示 “真”         1 + 2 > 1      True
False       表示 “假”         1 + 1 < 1      False
==          表示 “等于”       1 + 1 == 2     True
!=          表示 “不等于”     1 + 1 != 2     False
>=          表示 “大于等于”   1 + 1 >= 0     True
<=          表示 “小于等于”   1 + 1 <= 5     True
and         表示 “与”       True and False   False
or          表示 “或”       True or False    True
not         表示 “非”         not False      True
in          表示 “包含其中”   '1' in 'a1'     True
"""


"""
真值表

   NOT                True?
not False	          True
not True              False

    OR                True?
True or True          True
True or False         True
False or True         True
False or False        False

    AND               True?
True and True         True
True and False        False
False and True        False
False and False       False

    NOT OR            True?
not (True or True)    False
not (True or False)   False
not (False or True)   False
not (False or False)  True

    NOT AND           True?
not (True and True)   False
not (True and False)  True
not (False and True)  True
not (False and False) True

  !=                  True?
1 != 1                False
1 != 0                True
0 != 1                True
0 != 0                False

  ==                  True?
1 == 1                True
1 == 0                False
0 == 1                False
0 == 0                True
"""
