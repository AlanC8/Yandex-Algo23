n = int(input())
arr = []
for i in range(n):
    x = int(input());
    arr.append(x)

for i in arr:
    if((i % 2 != 0) >= (i % 2 == 0)):
        print("NO")
        break
    else:
        print("YES")
        break
    
