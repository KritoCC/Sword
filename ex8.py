# 习题八

formatter = "%r %r %r %r"

print(formatter % (1, 2, 3, 4))
print(formatter % ("one", "two", "three", "four"))
print(formatter % (True, False, False, True))
print(formatter % (formatter, formatter, formatter, formatter))
print(formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
))

# 结果中"But it didn't sing"是双引号，原因在于 %r 格式化字符后是显示字符的原始数据。
# 而字符串的原始数据包含引号，所以我们看到其他字符串被格式化后显示单引号。
# 而这条双引号的字符串是因为原始字符串中有了单引号，为避免字符意外截断，
# python 自动为这段字符串添加了双引号。
