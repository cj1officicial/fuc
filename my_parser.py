import json
import struct
import yaml

def parse_file(data, file_format):
    # 初始化一个字典，用于存放解析结果
    result = {}
    # 初始化一个变量，用于记录当前读取的位置
    offset = 0
    # 遍历文件格式的顺序部分（seq）
    for field in file_format["seq"]:
        # 获取字段的名称（id）、类型（type）和大小（size）
        name = field["id"]
        type = field["type"]
        size = field.get("size")
        # 如果类型是一个内置的数据类型，如u1、u4等，使用struct模块来解码
        if isinstance(type, str) and type.startswith("u"):
            # 根据类型的后缀，确定字节数
            num_bytes = int(type[1:])
            # 检查是否有足够的字节可供解码
            if offset + num_bytes <= len(data):
                # 从数据中截取相应的字节
                bytes = data[offset:offset+num_bytes]
                # 将每个字节转换为整数并存入字典中
                result[name] = int.from_bytes(bytes, byteorder='big')
                # 更新当前读取的位置
                offset += num_bytes
            else:
                print(f"Error: Not enough bytes to unpack for field {name}.")
        # 如果类型是一个自定义的类型，如header等，使用递归的方式来解析
        elif isinstance(type, str) and type in file_format["types"]:
            # 获取自定义类型的定义
            sub_format = file_format["types"][type]
            # 检查是否有足够的字节可供递归解析
            if offset < len(data):
                # 调用parse_file函数，传入数据和自定义类型的定义，得到解析结果
                value = parse_file(data[offset:], sub_format)
                # 将解析结果存入字典中
                result[name] = value
                # 更新当前读取的位置
                offset += value["_size"]
            else:
                print(f"Error: Not enough bytes to parse for field {name}.")
        # 如果大小是一个已知的值，如header.data_size等，直接截取相应的字节
        elif isinstance(size, int):  # Modified to check for int type
            # 获取大小的值
            num_bytes = size
            # 检查是否有足够的字节可供截取
            if offset + num_bytes <= len(data):
                # 从数据中截取相应的字节
                bytes = data[offset:offset+num_bytes]
                # 将字节存入字典中
                result[name] = bytes
                # 更新当前读取的位置
                offset += num_bytes
            else:
                print(f"Error: Not enough bytes to slice for field {name}.")
        # 其他情况，暂不处理
        else:
            pass
    # 在字典中添加一个特殊的键，表示当前类型的总大小
    result["_size"] = offset
    # 返回解析结果
    return result

if __name__ == "__main__":
    # 读取yaml文件，获取文件格式的规则
    with open("./my_format.yaml", "r") as f:
        file_format = yaml.safe_load(f)

    # 读取二进制文件，获取文件内容
    with open("./my_file.bin", "rb") as f:
        file_data = f.read()

    # 调用parse_file函数，传入二进制数据和文件格式的规则，打印解析结果
    result = parse_file(file_data, file_format)
    result_str = json.dumps(result, indent=4, ensure_ascii=False)
    print(result_str)


