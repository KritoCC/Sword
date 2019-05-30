# 习题二十六修改版

# 据说我们的练习至此恰好是过半的位置，所以 Zed 大人给我们安排了期中考试，
# 要求是修改其中的各种错误。题目来自 24、25 题的脚本，而这其中特意调整了顺序并增加了不少错误，
# 这里也有很多程序员常犯的错误（例如拼写错误），所以也是一个负面教材的学习了。
# Zed 给了我们两个建议：
# 1. 不要寻求帮助，即使花费了大量时间也要自己独立完成。
# 2. 不要钻牛角尖，想不出的时候试着休息一下。
# 题目脚本下载(ex26_original.py就是该脚本):
# https://learnpythonthehardway.org/book/exercise26.txt

import ex25


def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words


def sort_words(words):
    """Sorts the words."""
    return sorted(words)


def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print(word)


def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print(word)


def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)


def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)


def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)


print("Let's practice everything.")
print('You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.')

poem = """
\tThe lovely word
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""


print('---------------')
print(poem)
print('---------------')

five = 10 - 2 + 3 - 5
print("This should be five: %d" % five)


def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point)

print("With a starting point of: %d" % start_point)
print("We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates))

start_point = start_point / 10

print("We can also do that this way:")
print("We'd have %d beans, %d jars, and %d crabapples." %
      secret_formula(start_point))

sentence = "All good things come to those who wait."

words = ex25.break_words(sentence)
sorted_words = ex25.sort_words(words)

print_first_word(words)
print_last_word(words)
print_first_word(sorted_words)
print_last_word(sorted_words)
sorted_words = ex25.sort_sentence(sentence)
print(sorted_words)

print_first_and_last(sentence)
print_first_and_last_sorted(sentence)
