x = [5,7,8,7,2,17,2,9,4,11,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

target = 12

for item in x:
    if item == target:
        print(f"Targeted item {item}")
    

def binarySearch(arr, target):
    start = 0
    end = len(arr) - 1
    mid = None
    