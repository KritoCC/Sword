# 习题十九巩固练习

# 简单改编一个程序，先写出原程序

from sys import argv  # 对应于法五
print("文件大小是1G，下载带宽是4M下水管，计算下载用几分钟：")
# 网络带宽一般以位为单位,4M位的话,速度要除以8,就是每秒500k字节的速度
# 1G=1024M=1048576K 除以500就是 时间
print(1024000 / ((4 * 1024) / 8) / 60)


# 用函数重写上述程序
def download_time(bandwidth, size):
    bandwidth_KByte = bandwidth * 1024
    download_bandwidth_KBs = bandwidth_KByte / 8
    need_time = (size * 1024 * 1024) / download_bandwidth_KBs / 60
    print("带宽%d Mbit, 下载%d GByte的文件需要用时约：%.2f分钟" % (
        bandwidth, size * 1024, need_time))


# 尝试用不同的方式运行该函数

# 计算22Mbit 带宽，下载10GByte文件所需时间
# 法一
download_time(22, 10)

# 法二
bandwidth_Mbit_1 = 22
size_GByte_1 = 10
download_time(bandwidth_Mbit_1, size_GByte_1)

# 法三
download_time(10 + 12, 5 + 5)

# 法四
bandwidth_Mbit_2 = int(input("带宽为："))
size_GByte_2 = int(input("文件大小为："))
download_time(bandwidth_Mbit_2, size_GByte_2)

# 法五
script, bandwidth_Mbit_3, size_GByte_3 = argv
download_time(int(bandwidth_Mbit_3), int(size_GByte_3))

# 上述方法进行结合可以产生更多运行方式
