from sys import *
from array import *
S = int(input("S: "))
V = input("[Vs]:")
V = [int(x) for x in V.split()]

memo = { }
def DP_memo(x):
    if x == 0: return 0
    if x in memo: return memo[x]
    minList = []
    for i in range(len(V)):
        if V[i] <= x:
            temp = 1 + DP_memo(x-V[i])
            minList.append(temp)
    memo[x] = min(minList)
    return memo[x]

def DP_table(x):
    arr = [maxsize] * (x+1)
    arr[0] = 0
    for i in range(1, x + 1):
        for n in V:
            if i >= n:
                arr[i] = min(arr[i], arr[i-n] + 1)
    return arr[x]
print(DP_table(14))