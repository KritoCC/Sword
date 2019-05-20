# 习题二十三

# 本习题需要一个叫languages.txt，
# 下载地址是：https://learnpythonthehardway.org/python3/languages.txt
# 编码格式：UTF-8。

# 调用sys模块中的argv功能（获取当前正在执行的命令行参数），形式与之前使用的有所不同
import sys
script, encoding, error = sys.argv


# 定义函数main，内有三个形参
def main(language_file, encoding, errors):
    line = language_file.readline()
    # 读取文件中的一行文本，并赋值给line，注意language_file是main主函数的实参
    # 实参是一个实实在在存在的参数，是实际占用内存地址的，
    # 而形参只是意义上的一种参数，在定义的时候是不占内存地址的
    '''
    if语句，用来检测line中是否为真值，
    如果为真，则执行下面2行代码，如果为假，则跳过不执行；
    所以如果readline()返回包含东西，则继续执行下面2行，
    如果返回为null，则不执行，这是为了防止死循环；
    '''
    if line:
        # 在主函数main中调用另外一个函数print_line
        print_line(line, encoding, errors)
        # 这个return是让我们在主函数main内再调用一次main，实际上就是跳到main顶端再运行一次
        return main(language_file, encoding, errors)


# 定义print_line函数，内有3个形参，这个函数的作用就是对language.txt中的每一行进行编码
def print_line(line, encoding, errors):
    # .strip()的作用：删掉每行结尾的\n
    # .strip()方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。
    next_lang = line.strip()
    # .encode()的作用：把每一行字符串编码成字节串bytes
    # .encode()方法以 encoding 指定的编码格式编码字符串。
    # errors -- 设置不同错误的处理方案。
    # 默认为 'strict',意为编码错误引起一个UnicodeError。
    # 其他可能的值有 'ignore', 'replace', 'xmlcharrefreplace', 'backslashreplace'
    # 以及通过 codecs.register_error() 注册的任何值。
    raw_bytes = next_lang.encode(encoding, errors=errors)
    # .decode()的作用：把每一行字节串解码成字符串string
    # .decode()方法以 encoding 指定的编码格式解码字符串，默认编码为字符串编码。
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    # 打印：“字节串 <===> 字符串”
    print(raw_bytes, "<===>", cooked_string)
    print(type(raw_bytes), type(cooked_string))


# 把languages.txt文件以utf-8的编码方式打开
languages = open("languages.txt", encoding="utf-8")

'''
上面都是定义函数，现在开始调用函数，main函数的执行顺序：
1.传入三个参数，languages， encoding, error, language是第52行的变量，后2个是第9行的变量；
2.第14行：读取languages的一行文本，赋值给line
3.第24行：做个判定，判定第26行的函数返回的结果，如果为真，执行第26、28行代码，如果为假，则不执行
4.第26行：调用print_line函数，这个函数删除了第14行读取的一行文本后面的\n，
然后把这行文本编码成字节串，赋值给raw_bytes变量待用，
又把raw_bytes变量解码成字符串，赋值给cooked_string变量待用，最后按照格式打印出来；
5.执行第28行再次调用main函数，重复上面的顺序，最后结果就是把languages.txt文件的每一行读取出来进行编码、解码、打印。
6.然后当所有的内容都读取完后，再次调用main函数，则第13行的if此时会发现返回结果为null，
然后就会停止执行return，循环结束，整段代码执行完毕。
'''
main(languages, encoding, error)


# 运行结果：
# PS C:\Users\12409\AppData\Roaming\Atom\file> python ex23.py utf-8 strict
# b'Afrikaans' <===> Afrikaans
# b'\xe1\x8a\xa0\xe1\x88\x9b\xe1\x88\xad\xe1\x8a\x9b' <===> አማርኛ
# b'\xd0\x90\xd2\xa7\xd1\x81\xd1\x88\xd3\x99\xd0\xb0' <===> Аҧсшәа
# b'\xd8\xa7\xd9\x84\xd8\xb9\xd8\xb1\xd8\xa8\xd9\x8a\xd8\xa9' <===> العربية
# b'Aragon\xc3\xa9s' <===> Aragonés
# b'Arpetan' <===> Arpetan
# b'Az\xc9\x99rbaycanca' <===> Azərbaycanca
# b'Bamanankan' <===> Bamanankan
# b'\xe0\xa6\xac\xe0\xa6\xbe\xe0\xa6\x82\xe0\xa6\xb2\xe0\xa6\xbe' <===> বাংলা
# b'B\xc3\xa2n-l\xc3\xa2m-g\xc3\xba' <===> Bân-lâm-gú
# b'\xd0\x91\xd0\xb5\xd0\xbb\xd0\xb0\xd1\x80\xd1\x83\xd1\x81\xd0\xba\xd0\xb0\xd1\x8f' <===> Беларуская
# b'\xd0\x91\xd1\x8a\xd0\xbb\xd0\xb3\xd0\xb0\xd1\x80\xd1\x81\xd0\xba\xd0\xb8' <===> Български
# b'Boarisch' <===> Boarisch
# b'Bosanski' <===> Bosanski
# b'\xd0\x91\xd1\x83\xd1\x80\xd1\x8f\xd0\xb0\xd0\xb4' <===> Буряад
# b'Catal\xc3\xa0' <===> Català
# b'\xd0\xa7\xd3\x91\xd0\xb2\xd0\xb0\xd1\x88\xd0\xbb\xd0\xb0' <===> Чӑвашла
# b'\xc4\x8ce\xc5\xa1tina' <===> Čeština
# b'Cymraeg' <===> Cymraeg
# b'Dansk' <===> Dansk
# b'Deutsch' <===> Deutsch
# b'Eesti' <===> Eesti
# b'\xce\x95\xce\xbb\xce\xbb\xce\xb7\xce\xbd\xce\xb9\xce\xba\xce\xac' <===> Ελληνικά
# b'Espa\xc3\xb1ol' <===> Español
# b'Esperanto' <===> Esperanto
# b'\xd9\x81\xd8\xa7\xd8\xb1\xd8\xb3\xdb\x8c' <===> فارسی
# b'Fran\xc3\xa7ais' <===> Français
# b'Frysk' <===> Frysk
# b'Gaelg' <===> Gaelg
# b'G\xc3\xa0idhlig' <===> Gàidhlig
# b'Galego' <===> Galego
# b'\xed\x95\x9c\xea\xb5\xad\xec\x96\xb4' <===> 한국어
# b'\xd5\x80\xd5\xa1\xd5\xb5\xd5\xa5\xd6\x80\xd5\xa5\xd5\xb6' <===> Հայերեն
# b'\xe0\xa4\xb9\xe0\xa4\xbf\xe0\xa4\xa8\xe0\xa5\x8d\xe0\xa4\xa6\xe0\xa5\x80' <===> हिन्दी
# b'Hrvatski' <===> Hrvatski
# b'Ido' <===> Ido
# b'Interlingua' <===> Interlingua
# b'Italiano' <===> Italiano
# b'\xd7\xa2\xd7\x91\xd7\xa8\xd7\x99\xd7\xaa' <===> עברית
# b'\xe0\xb2\x95\xe0\xb2\xa8\xe0\xb3\x8d\xe0\xb2\xa8\xe0\xb2\xa1' <===> ಕನ್ನಡ
# b'Kapampangan' <===> Kapampangan
# b'\xe1\x83\xa5\xe1\x83\x90\xe1\x83\xa0\xe1\x83\x97\xe1\x83\xa3\xe1\x83\x9a\xe1\x83\x98' <===> ქართული
# b'\xd2\x9a\xd0\xb0\xd0\xb7\xd0\xb0\xd2\x9b\xd1\x88\xd0\xb0' <===> Қазақша
# b'Krey\xc3\xb2l ayisyen' <===> Kreyòl ayisyen
# b'Latga\xc4\xbcu' <===> Latgaļu
# b'Latina' <===> Latina
# b'Latvie\xc5\xa1u' <===> Latviešu
# b'L\xc3\xabtzebuergesch' <===> Lëtzebuergesch
# b'Lietuvi\xc5\xb3' <===> Lietuvių
# b'Magyar' <===> Magyar
# b'\xd0\x9c\xd0\xb0\xd0\xba\xd0\xb5\xd0\xb4\xd0\xbe\xd0\xbd\xd1\x81\xd0\xba\xd0\xb8' <===> Македонски
# b'Malti' <===> Malti
# b'\xe0\xa4\xae\xe0\xa4\xb0\xe0\xa4\xbe\xe0\xa4\xa0\xe0\xa5\x80' <===> मराठी
# b'\xe1\x83\x9b\xe1\x83\x90\xe1\x83\xa0\xe1\x83\x92\xe1\x83\x90\xe1\x83\x9a\xe1\x83\xa3\xe1\x83\xa0\xe1\x83\x98' <===> მარგალური
# b'\xd9\x85\xd8\xa7\xd8\xb2\xd9\x90\xd8\xb1\xd9\x88\xd9\x86\xdb\x8c' <===> مازِرونی
# b'Bahasa Melayu' <===> Bahasa Melayu
# b'\xd0\x9c\xd0\xbe\xd0\xbd\xd0\xb3\xd0\xbe\xd0\xbb' <===> Монгол
# b'Nederlands' <===> Nederlands
# b'\xe0\xa4\xa8\xe0\xa5\x87\xe0\xa4\xaa\xe0\xa4\xbe\xe0\xa4\xb2 \xe0\xa4\xad\xe0\xa4\xbe\xe0\xa4\xb7\xe0\xa4\xbe' <===> नेपाल भाषा
# b'\xe6\x97\xa5\xe6\x9c\xac\xe8\xaa\x9e' <===> 日本語
# b'Norsk bokm\xc3\xa5l' <===> Norsk bokmål
# b'Nouormand' <===> Nouormand
# b'Occitan' <===> Occitan
# b'O\xca\xbbzbekcha/\xd1\x9e\xd0\xb7\xd0\xb1\xd0\xb5\xd0\xba\xd1\x87\xd0\xb0' <===> Oʻzbekcha/ўзбекча
# b'\xe0\xa8\xaa\xe0\xa9\xb0\xe0\xa8\x9c\xe0\xa8\xbe\xe0\xa8\xac\xe0\xa9\x80' <===> ਪੰਜਾਬੀ
# b'\xd9\xbe\xd9\x86\xd8\xac\xd8\xa7\xd8\xa8\xdb\x8c' <===> پنجابی
# b'\xd9\xbe\xda\x9a\xd8\xaa\xd9\x88' <===> پښتو
# b'Plattd\xc3\xbc\xc3\xbctsch' <===> Plattdüütsch
# b'Polski' <===> Polski
# b'Portugu\xc3\xaas' <===> Português
# b'Rom\xc3\xa2n\xc4\x83' <===> Română
# b'Romani' <===> Romani
# b'\xd0\xa0\xd1\x83\xd1\x81\xd1\x81\xd0\xba\xd0\xb8\xd0\xb9' <===> Русский
# b'Seeltersk' <===> Seeltersk
# b'Shqip' <===> Shqip
# b'Simple English' <===> Simple English
# b'Sloven\xc4\x8dina' <===> Slovenčina
# b'\xda\xa9\xd9\x88\xd8\xb1\xd8\xaf\xdb\x8c\xdb\x8c \xd9\x86\xd8\xa7\xd9\x88\xdb\x95\xd9\x86\xd8\xaf\xdb\x8c' <===> کوردیی ناوەندی
# b'\xd0\xa1\xd1\x80\xd0\xbf\xd1\x81\xd0\xba\xd0\xb8 / srpski' <===> Српски / srpski
# b'Suomi' <===> Suomi
# b'Svenska' <===> Svenska
# b'Tagalog' <===> Tagalog
# b'\xe0\xae\xa4\xe0\xae\xae\xe0\xae\xbf\xe0\xae\xb4\xe0\xaf\x8d' <===> தமிழ்
# b'\xe0\xb8\xa0\xe0\xb8\xb2\xe0\xb8\xa9\xe0\xb8\xb2\xe0\xb9\x84\xe0\xb8\x97\xe0\xb8\xa2' <===> ภาษาไทย
# b'Taqbaylit' <===> Taqbaylit
# b'\xd0\xa2\xd0\xb0\xd1\x82\xd0\xb0\xd1\x80\xd1\x87\xd0\xb0/tatar\xc3\xa7a' <===> Татарча/tatarça
# b'\xe0\xb0\xa4\xe0\xb1\x86\xe0\xb0\xb2\xe0\xb1\x81\xe0\xb0\x97\xe0\xb1\x81' <===> తెలుగు
# b'\xd0\xa2\xd0\xbe\xd2\xb7\xd0\xb8\xd0\xba\xd3\xa3' <===> Тоҷикӣ
# b'T\xc3\xbcrk\xc3\xa7e' <===> Türkçe
# b'\xd0\xa3\xd0\xba\xd1\x80\xd0\xb0\xd1\x97\xd0\xbd\xd1\x81\xd1\x8c\xd0\xba\xd0\xb0' <===> Українська
# b'\xd8\xa7\xd8\xb1\xd8\xaf\xd9\x88' <===> اردو
# b'Ti\xe1\xba\xbfng Vi\xe1\xbb\x87t' <===> Tiếng Việt
# b'V\xc3\xb5ro' <===> Võro
# b'\xe6\x96\x87\xe8\xa8\x80' <===> 文言
# b'\xe5\x90\xb4\xe8\xaf\xad' <===> 吴语
# b'\xd7\x99\xd7\x99\xd6\xb4\xd7\x93\xd7\x99\xd7\xa9' <===> ייִדיש
# b'\xe4\xb8\xad\xe6\x96\x87' <===> 中文

# "<===>"左边显示的都是bytes，右边显示的是string
# 在powershell里面右边有些会显示为框框，这是因为powershell没法显示的utf-8


# if语句知识补充：
# Python条件语句是通过一条或多条语句的执行结果（True或者False）来决定执行的代码块。
# Python程序语言指定任何非0和非空（null）值为true，0 或者 null为false。
# Python 编程中 if 语句用于控制程序的执行，基本形式为：

# if 判断条件：
#     执行语句……
# else：
#     执行语句……
# 其中"判断条件"成立时（非零），则执行后面的语句，而执行内容可以多行，以缩进来区分表示同一范围。
# else 为可选语句，当需要在条件不成立时执行内容则可以执行相关语句。

# 下面是if的基本用法实例
flag = False
name = 'Stark'
if name == 'Stark':
    flag = True
    print("Welcome Boss")
else:
    print(name)


# 我们知道，计算机是以二进制为单位的，也就是说计算机只识别0和1,
# 也就是我们平时在电脑上看到的文字，只有先变成0和1，计算机才会识别它的意思。
# 这种数据和二进制的转换规则就是编码。计算机的发展中，有ASCII码，GBK，Unicode，utf-8编码。
# 我们先从编码的发展史了解一下编码的进化过程。
# 编码发展史
# · 美国人发明了计算机，用八位0和1的组合，一一对应英文中的字符，整出了一个表格，ASCII表。
#   ASCII标准把数字和字母互相对应，我们可以在Python中试一下：
0b1011010
ord('Z')
chr(90)
# · 计算机传入中国，中国地大物博，繁体字和简体字多，8位字节最多表示256个字符，满足不了，于是对ASCII扩展，新表叫GB2312
# · 后来发现GB2312还不够用，扩充之后形成GB18030。
# · 每个国家都像中国一样，把自己的语言编码，于是出现了各种各样的编码，如果你不安装相应的编码，就无法解释相应编码想表达的内容。
# · 各自编码无法国际交流。
#   一个国际组织一起创造了一种编码 UNICODE（Universal Multiple-Octet Coded Character Set）
#   规定所有字符用两个字节表示，就是固定的，所有的字符就两个字节，计算机容易识别。
#   2的16次方可以表示所有的字符了。
# · UNICODE虽然解决了各自为战的问题，但是美国人不愿意了，
#   因为美国原来的ASCII只需要一个字节就可以了。
#   UNICODE编码却让他们的语言多了一个字节，白白浪费一个字节的存储空间。
#   经过协商，出现了一种新的转换格式，被称为通用转换格式，
#   也就是UTF(unicode transformation format) 常见的有utf-8,utf-16。
#   utf-8规定，先分类，美国字符一个字节，欧洲两个字符，东南亚三个字符。

# encode()和decode()
# decode英文意思是 解码，encode英文原意 编码
# 字符串在Python内部的表示是unicode编码，因此，在做编码转换时，通常需要以unicode作为中间编码，
# ***Py3 自动把文件编码转为unicode,所以虽然languages.txt的编码格式是utf-8，到了Py3中就转为unicode格式***
# 即先将其他编码的字符串解码（decode）成unicode，再从unicode编码（encode）成另一种编码。
# decode的作用是将其他编码的字符串转换成unicode编码，
# 如str1.decode('gb2312')，表示将gb2312编码的字符串str1转换成unicode编码。
# encode的作用是将unicode编码转换成其他编码的字符串，
# 如str2.encode('gb2312')，表示将unicode编码的字符串str2转换成gb2312编码。
# 总得意思:想要将其他的编码转换成utf-8必须先将其解码成unicode然后重新编码成utf-8,
# 它是以unicode为转换媒介的 如：s='中文' 如果是在utf8的文件中，该字符串就是utf8编码，
# 如果是在gb2312的文件中，则其编码为gb2312。这种情况下，要进行编码转换，
# 都需要先用 decode方法将其转换成unicode编码，再使用encode方法将其转换成其他编码。
# 通常，在没有指定特定的编码方式时，都是使用的系统默认编码创建的代码文件
# 在python3.x中，encode()函数只能用于字符串类型，而decode()函数只能用于字节数据类型。

#        decode         encode
# bytes ---------> str ---------> bytes
# 举例说明：

a = '编码'                       # a是unicode类型
b = a.encode('utf-8')      # b是utf-8类型
c = a.encode('gbk')        # c是gbk类型
d = b.decode('utf-8')      # d是unicode类型
e = c.decode('gbk')        # e是unicode类型
print(a, b, c, d, e)
print(type(a), type(b), type(c), type(d), type(e))
# python3默认是unicode类型

# Python3的执行过程
#        1.解释器找到代码文件，把代码字符串按文件头定义的编码加载到内存，转成unicode

#        2.把代码字符串按照语法规则进行解释，

#        3.所有的变量字符都会以unicode编码声明
