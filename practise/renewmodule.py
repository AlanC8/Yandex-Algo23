n = int(input())
list = []
for i in range(n):
    newList = []
    for j in range(n):
        x = int(input())
        newList.append(x)
    list.append(newList)
max = list[0][0]
maxI = 0
maxJ = 0
for i in range(n):
    for j in range(n + 1):
        if (list[i][j] > max):
            maxI = i
            maxJ = j

print(maxI, maxJ, end=' ')
