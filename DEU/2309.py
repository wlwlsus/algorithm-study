import sys


def find(mList):
    temp1 = 0
    temp2 = 0
    for i in range(len(mList)):
        for j in range(i+1,len(mList)):
            if(sum(mList) - (mList[i]+mList[j]) == 100):
                temp1 = mList[i]
                temp2 = mList[j]

    mList.remove(temp1)
    mList.remove(temp2)

    for i in mList:
       print(i)


tall = [int(input()) for _ in range(9)]
tall.sort()
find(tall)
