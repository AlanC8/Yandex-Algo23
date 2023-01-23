num = int(input())
cnt = 0
k = 0
for i in num:
    if(num[i] == 0): cnt += 1
    else:
        if(max < k): max = k;
        k = 0;
    print(cnt)