# 习题十四巩固练习一

from sys import argv

script, user_name = argv
prompt = "%s>" % user_name  # 改成这样试试

print("Hi %s, I'm the %s script." % (user_name, script))
print("I'd like to ask you a few questions.")
print("Do you like me %s?" % user_name)
likes = input(prompt)

print("Where do you live %s？" % user_name)
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print("""
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer))

# 运行结果
# PS C:\Users\12409\AppData\Local\atom\file> python ex14_1.py Krito
# Hi Krito, I'm the ex14_1.py script.
# I'd like to ask you a few questions.
# Do you like me Krito?
# Krito>Yes!
# Where do you live Krito
# Krito>Sword Art Online
# What kind of computer do you have?
# Krito>Apple

# Alright, so you said 'Yes!' about liking me.
# You live in 'Sword Art Online'. Not sure where that is.
# And you have a 'Apple' computer. Nice.
