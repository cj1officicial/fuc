# 导入struct模块
import struct

# 打开二进制文件，模式为只读
with open("binary_file.bin", "rb") as file:
    # 读取文件的前4个字节，作为一个整数
    num = struct.unpack("i", file.read(4))[0]
    # 打印整数的值
    print(num)
    # 读取文件的后4个字节，作为一个浮点数
    flt = struct.unpack("f", file.read(4))[0]
    # 打印浮点数的值
    print(flt)
