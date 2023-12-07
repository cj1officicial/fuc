data = b'\x48\x65\x6c\x6c\x6f\x20\x57\x6f\x72\x6c\x64'  # 二进制数据

# 打开文件以二进制模式写入数据
with open('binary_file.bin', 'wb') as file:
    file.write(data)

print("二进制文件创建成功！")