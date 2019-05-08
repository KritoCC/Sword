# 导入模块

import module_name

print("This is module_test01.py")
# python的type函数有两个用法，当只有一个参数的时候，返回对象的类型。
# 当有三个参数的时候返回一个类对象。
print(type(module_name))
print(module_name)

# 在导入模块的时候，模块所在文件夹会自动生成一个__pycache__\module_name.cpython-36.pyc文件。
# "import module_name" 的本质是将"module_name.py"中的全部代码加载到内存并赋值给与模块同名的变量写在当前文件中,
# 这个变量的类型是'module'；
# <module 'module_name' from 'C:\\Users\\12409\\AppData\\Local\\atom\\file\\ex17_import_test\\module_name.py'>
