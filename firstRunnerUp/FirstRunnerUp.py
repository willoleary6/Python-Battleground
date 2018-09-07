import copy

n = int(input())
arr = map(int, input().split())

copyOfArr = copy.deepcopy(arr)
currentBiggest = list(copy.deepcopy(arr))[0]
runnerUp = list(copy.deepcopy(arr))[0]

for i in list(arr):
    if currentBiggest < i:
        currentBiggest = i

for j in list(copyOfArr):
    if j != currentBiggest:
        if runnerUp < j:
            runnerUp = j
print(runnerUp)


