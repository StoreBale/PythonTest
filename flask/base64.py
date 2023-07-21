import base64

def file_to_base64(filename):
    with open(filename, 'rb') as file:
        binary_data = file.read()
        base64_data = base64.b64encode(binary_data)
    return base64_data

# 使用示例：
file_path = 'path/to/your/file.ext'
base64_data = file_to_base64(file_path)
print(base64_data)
