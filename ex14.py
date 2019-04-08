# 习题十四

from sys import argv

script, user_name = argv
prompt = "> "
# 我们将用户提示符设置为变量prompt，这样就不需要在每次用到input时反复输入提示用户的字符了。
# 而且，如果要将提示符修改成别的字符串，只要改一个位置就可以了。

print("Hi %s, I'm the %s script" % (user_name, script))
print("I'd like to ask you a few question.")
print("Do you like me %s？" % user_name)
likes = input(prompt)

print("Where do you live %s？" % user_name)
lives = input(prompt)

print("Where kind of computer do you have?")
computer = input(prompt)

print("""
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer))

# 运行结果
# PS C:\Users\12409> cd C:\Users\12409\AppData\Local\atom\file
# PS C:\Users\12409\AppData\Local\atom\file> python ex14.py Krito
# Hi Krito, I'm the ex14.py script
# I'd like to ask you a few question.
# Do you like me Krito
# > Yes
# Where do you live Krito
# > Sword Art Online
# Where kind of computer do you have?
# > Apple

# Alright, so you said 'Yes' about likeing me.
# You live in 'Sword Art Online'. Not sure where that is.
# And you have a 'Apple' computer. Nice.
