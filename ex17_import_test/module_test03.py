# 导入包

# 包的本质就是一个包含__init__.py文件的目录。

# 这个语句只会执行package_name目录下的__init__.py文件，而不会导入任何模块:
import package_name

# from package_name import hello
print("This is module_test03.py")

# "import package_name"导入包的本质就是执行该包下的__init__.py文件，
# 在执行文件后，会在"package_name"目录下生成一个"__pycache__ / __init__.cpython-35.pyc" 文件。
