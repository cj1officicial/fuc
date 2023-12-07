import gif

# 读取 GIF 文件
with open("R.gif", "rb") as f:
    data = f.read()

# 解析数据
parser = gif.Gif.from_bytes(data)
header = parser.header
logical_screen = parser.logical_screen

# 获取解析结果
magic = header.magic
version = header.version
image_width = logical_screen.image_width
image_height = logical_screen.image_height
flags = logical_screen.flags
bg_color_index = logical_screen.bg_color_index
pixel_aspect_ratio = logical_screen.pixel_aspect_ratio

# 打印解析结果
print(f"Magic: {magic}")
print(f"Version: {version}")
print(f"Image Width: {image_width}")
print(f"Image Height: {image_height}")
print(f"Flags: {flags}")
print(f"Background Color Index: {bg_color_index}")
print(f"Pixel Aspect Ratio: {pixel_aspect_ratio}")