import os
# 1
pth = r"C:\Users\bigch\Desktop\alan\programming\tsis6"
print(os.listdir(pth))

# 2
path = r"C:\Users\bigch\Desktop\alan\programming\tsis6\dir-files\new_txt.txt"
if not os.path.exists(path):
    print(f"{path} does not exist.")
else:
    print(f"{path} exists.")

    if not os.access(path, os.R_OK):
        print(f"{path} is not readable.")
    else:
        print(f"{path} is readable.")

    if not os.access(path, os.W_OK):
        print(f"{path} is not writable.")
    else:
        print(f"{path} is writable.")

    if not os.access(path, os.X_OK):
        print(f"{path} is not executable.")
    else:
        print(f"{path} is executable.")

# 3
pth = r"C:\Users\bigch\Desktop\alan\programming\tsis6"
if os.path.isdir(pth):
    print("exist", os.path.basename(pth))
    print(pth.split("\\"))

else:
    print("not exist")

# 4
file = open("new_txt.txt")
cnt = 0
for i in file:
    cnt += 1
print(cnt)

# 5
newList = [1, 2, 3, 4, 5]
file = open("new_txt.txt", "a+")
file.write('\n')
file.write(str(newList) + '\n')
file.seek(0)
print(file.read())

# 6
cod = 65
while cod < 91:
    open(f"{chr(cod)}.txt", 'w')
    cod += 1
cod2 = 90
while cod2 > 64:
    d = fr"C:\Users\bigch\Desktop\alan\programming\tsis6\{chr(cod2)}.txt"
    os.remove(d)
    cod2 -= 1

# 7
a = open("new_txt.txt")
b = a.read()
c = open("to_copy.txt", "w")
c.write(b)


# 8
p = r"C:\Users\bigch\Desktop\alan\programming\tsis6\deleteme.txt"
if os.path.exists(p):
    os.remove(p)
else:
    print("not exist")
