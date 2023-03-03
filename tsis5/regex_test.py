import re


def read_file(fpath: str):
    with open(fpath, mode='r', encoding='utf8') as file:
        return file.read()


file = read_file("row.txt")
pattern = "^аб*$"
print(re.findall(pattern, file))
