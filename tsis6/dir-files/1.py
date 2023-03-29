f = open("new_txt.txt", "a")
f.write("AKKFAKLFJ")
f.close()

f = open("new_txt.txt", "r")
print(f.read())
