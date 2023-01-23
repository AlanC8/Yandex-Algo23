def averageNum(list):
    sumOfAll = sum(list)
    length = len(list)
    aver = sumOfAll / length
    return aver

list = [5,10,15,20,25,30]
print(averageNum(list))