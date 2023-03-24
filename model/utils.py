import os

#把数据添加到已有文件下一行
def append_to_file(filename, line):
    with open(filename, "a") as f:
        f.write(line + "\n")

#创建一个新的文件，并写一行数据
def write_to_file(filename, line):
    with open(filename, "w") as f:
        f.write(line + "\n")

#判断文件是否存在
def is_exist_file(filename):
    return os.path.exists(filename)


