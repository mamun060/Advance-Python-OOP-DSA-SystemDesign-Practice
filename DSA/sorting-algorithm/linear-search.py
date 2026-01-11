import math

def linearSearch(arr, target):
    for i in range(len(arr)):
        if(arr[i] == target):
            print(f"{arr[i]} list location is {i}")
    
    return f"Not Found {target}"


arr = [10,20,30,40,50,60,70,80,90,100]
target = 50
linearSearch(arr , target)