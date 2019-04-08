# 习题十四巩固练习二

from sys import argv

script, user_name, call = argv  # 加一个参量试试
prompt = "%s>" % user_name  # 改成这样试试

print("Hi %s, I'm the %r script." % (user_name, script))
print("Emmmm, you want me call you %s" % call)  # call在这里
print("I'd like to ask you a few question.")
print("Do you like me %s?" % call)
likes = input(call + " " + prompt)

print("Where do you live %s？" % call)
lives = input(call + " " + prompt)

print("What kind of computer do you have?")
computer = input(call + " " + prompt)

print("""
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer))

# 运行结果
# PS C:\Users\12409\AppData\Local\atom\file> python ex14_2.py Krito Master
# Hi Krito, I'm the 'ex14_2.py' script.
# Emmmm, you want me call you Master
# I'd like to ask you a few question.
# Do you like me Master?
# Master Krito>Yes!
# Where do you live Master？
# Master Krito>Sword Art Online
# What kind of computer do you have?
# Master Krito>Apple

# Alright, so you said 'Yes!' about liking me.
# You live in 'Sword Art Online'. Not sure where that is.
# And you have a 'Apple' computer. Nice.
