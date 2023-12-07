# from ast import Bytes
# from struct import Struct
# from construct import *

# # 定义结构
# MyFormat = Struct(
#     "magic" / Int32ul,       # magic number
#     "header" / Struct(
#         "version" / Int8ul,   # file version
#         "data_size" / Int32ul # size of data section in bytes
#     ),
#     "data" / Bytes(this.header.data_size) # data section
# )

# # 构建数据
# data = {
#     "magic": 12345678,
#     "header": {
#         "version": 1,
#         "data_size": 10
#     },
#     "data": b"\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09"
# }

# # 将数据打包成二进制文件
# binary_data = MyFormat.build(data)

# # 将二进制数据写入文件
# with open("my_file.bin", "wb") as f:
#     f.write(binary_data)

import construct
import yaml

# 读取您的.ksy文件，获取文件格式的规则
with open("my_format.ksy", "r") as f:
    format = yaml.safe_load(f)

# 根据您的.ksy文件的定义，构建一个与您的数据结构相对应的构造器对象
format = construct.Struct (
    "magic" / construct.Int32ub,
    "header" / construct.Struct (
        "version" / construct.Int8ub,
        "data_size" / construct.Int32ub,
    ),
    "data" / construct.Bytes (construct.this.header.data_size),
)

# 使用构造器对象的build方法，传入一个包含您想要的数据的字典，生成一个二进制数据
data = format.build (dict (
    magic = 0x12345678,
    header = dict (
        version = 0x01,
        data_size = 0x00000010,
    ),
    data = b"John Doe 123456",
))

# 将数据打包成二进制文件
binary_data = format.build(data)

# 将二进制数据写入文件
with open("my_file.bin", "wb") as f:
    f.write(binary_data)
