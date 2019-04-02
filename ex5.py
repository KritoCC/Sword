# 习题五

# 之前的练习中使用了 print() 打印出的字符串内容是固定的，
# 而格式化字符串可以将变量插入到字符串中打印出来，随着变量的改变打印出的内容也在改变。
name = 'Zed A. Shaw'
age = 35  # not a lie
height = 74  # 英寸
weight = 180  # 磅
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")

# 试用 %r 格式化字符，它的含义是“不管什么都打印出来”
print("Let's talk about %r." % name)
print("He's %r inches tall." % height)
print("He's %r pounds heavy." % weight)
print("Actually that's not too heavy.")
print("He's got %r eyes and %r hair." % (eyes, hair))
print("His teeth are usually %r depending on the coffee." % teeth)

# this line is tricky, try to get it exactly right
total = age + height + weight
print("If I add %r, %r, and %r I get %r." % (age, height, weight, total))

# 单位换算
print("Zed A. Shaw 高 %.2f 厘米" % (height * 2.54))
print("Zed A. Shaw 重 %.2f 千克" % (weight * 0.45))


# python 常用的格式化字符及其效果
#
# 占位符	                  作用	                 示例              	    结果
#   %s	                格式化为字符串	          '%s' % -666.66	           '-666'
#   %r	               格式化为原始数据	          '%r' % ' abc 	             " 'abc' "
#   %d	            格式化为 10 进制整数	        '%d' % 666	               '666'
#   	     整数：将数字转换成其unicode对应的值，
#   %c          10进制范围为0 <= i <= 1114111    '% c % c' % (97, 'b')	     'a b'
#                 (py27则只支持0-255);
#                字符：将字符添加到指定位置
#   %o	             格式化为 8 进制整数	        '% o' % 8	               '10'
#   %x	            格式化为 16 进制整数	        '% x' % 16	               '10'
#   %X	                 16 进制大写	           '% X' % 15	               'F'
#   	                 10进制浮点数
#   %f             可以用m.n控制最小长度（m)   '% f; % 6.2f' % (15, 10)  	'15.000000    10.00'
#                       和最小小数位（n）	                           '10.00'的前面有个空格占位共6位
#   % e	           使用科学计数法表示浮点数	       '% e' % 0.00001	         '1.000000e-05'
#   % E	               同 % e e为大写	          '% .2E' % 0.0004	         '4.00E-04'
#   % g 	以 10 进制或科学计数法表示浮点数	      '% g' % 1.001	              '1.001'
#   %G                   / (大写)                 '%g' % 0.00004              '4e-05'


# %f 浮点型用法
# %a.bf，a表示浮点数的打印长度，b表示浮点数小数点后面的精度  
# 只是%f时表示原值，默认是小数点后5位数    
pi = 3.141592653
print("PI = %f" % pi)  #  output: PI=3.141593    

# 只是 % 9f时，表示打印长度9位数，小数点也占一位，不够左侧补空格    
print("PI = %9f" % pi)  # output: PI=_3.141593    

# 只有.没有后面的数字时，表示去掉小数输出整数，03表示不够3位数左侧补0    
print("PI = %03.f" % pi)  #  output: PI=003    

# %6.3f表示小数点后面精确到3位，总长度6位数，包括小数点，不够左侧补空格    
print("PI = %6.3f" % pi)  #  output: PI=_3.142    

# %-6.3f表示小数点后面精确到3位，总长度6位数，包括小数点，不够右侧补空格    
print("PI = %-6.3f" % pi)  #  output: PI=3.142_    

# 还可以用%*.*f来表示精度，两个*的值分别在后面小括号的前两位数值指定    
# 如下，不过这种方式06就失去补0的功能，只能补空格    
print("PI = %*.*f" % (6, 3, pi))  #  output: PI=_3.142    


# 在Python中单引号和双引号都可以用来表示一个字符串，比如
str1 = 'python'
str2 = "python"
# str1和str2是没有任何区别的。
# Python以其易用性而著名，所以刚开始看教程学习看到单引号和双引号都可以使用会以为这是Python为了方便程序员，随便用哪个就好，不用担心用错。其实，背后的原因不只是这么简单。
# 举个例子，想想I'm a big fans of Python.这个字符串应该怎么定义。
# 单引号版本：
str3 = 'I\'m a big fan of Python.'
# 可以注意到，原来的字符串中有一个'，而Python又允许使用单引号' '来表示字符串，所以字符串中间的'必须用转移字符\才可以。
# 字符串中间只有一个'，这样写看起来还好，但是如果是We all know that 'A' and 'B' are two capital letters.这个字符串呢？
str4 = 'We all know that \'A\' and \'B\' are two capital letters.'
# 怎么样，是不是看起来就很不好看，而且很容易出错了？这个时候就是双引号也可以表示字符串该体现作用的时候了。下面是str4的双引号版本：
str4_ = "We all know that 'A' and 'B' are two capital letters."
# 这样是不是看起来就人性化多了？没错，这就是Python支持双引号和单引号都能用来定义字符串的原因。
# 反之，如果字符串中有双引号，为了避免使用转义符，你可以使用单引号来定义这个字符串。比如：
str5 = 'The teacher said: "Practice makes perfect" is a very famous proverb.'
# 这就是Python易用性和人性化的一个极致体现，当你用单引号' '定义字符串的时候，它就会认为你字符串里面的双引号" "是普通字符，从而不需要转义。
# 反之当你用双引号定义字符串的时候，就会认为你字符串里面的单引号是普通字符无需转义。
#
# 3个单引号及3个双引号
#
# 实际上3个单引号和3个双引号不经常用，但是在某些特殊格式的字符串下却有大用处。
# 通常情况下我们用单引号或者双引号定义一个字符串的时候只能把字符串连在一起写成一行，如果非要写成多行，就得在每一行后面加一个\表示连字符，比如：
str1 = "List of name:\
    Hua Li\
    Chao Deng"
# 而且即使你这样写也不能得到期望的输出：
# List of name:
# Hua Li
# Chao Deng
# 实际上输出是下面这样的：
str1 = "List of name:\
    Hua Li\
    Chao Deng"
print(str1)
#
# List of name:        Hua Li        Chao Deng
#
# 那么该如何得到我们期望的一行一个名字的输出格式呢？这就是3个引号的作用了：
str1 = """List of name:
Hua Li
Chao Deng
"""
print(str1)
#
# List of name:
# Hua Li
# Chao Deng
#
# 虽然我们也可以通过给字符串加上\n实现：
str1 = "List of name:\nHua Li\nChao Deng"
print(str1)
#
# List of name:
# Hua Li
# Chao Deng
#
# 但是这样在输入的时候看起来就乱了很多不是么？所以这种情况下尽量使用3个引号，至于3个单引号还是双引号都是一样的，
# 只需要注意如果字符串中包含有单引号就要使用双引号来定义就好了。
#
# 而且使用3个引号还有一个特别棒的作用就是：加注释！
#
str1 = """
List of name:
Hua Li # LiHua
Chao Deng # DengChao
"""
print(str1)
#
# List of name:
# Hua Li  # LiHua
# Chao Deng  # DengChao
# 如果要实现这种输出效果，仅仅使用单引号或者双引号还能实现吗？
