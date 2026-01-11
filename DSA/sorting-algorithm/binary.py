import math

def binarySearch(arr , target):
    start = 0
    end = len(arr) - 1
    mid = math.floor((start + end) / 2)
    
    for x in range(len(arr)):
        if arr[x] == target:
            print(f"{arr[x]} is list location is {x}")
        elif mid < target:
            start = mid + 1
        else:
            end = mid - 1
    return -1

listItems = [10,20,30,40,50,60,70,80,90,100]

target = 80
binarySearch(listItems , target)