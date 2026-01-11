# Bubble sort for data sorting 
class BubbleSort:
    def datasorting(self, arr):
        for i in range(0, len(arr)):
            for j in range( i , len(arr)):
                if arr[i] > arr[j]:
                    temp = arr[i]
                    arr[i] = arr[j]
                    arr[j] = temp
        return arr

class BinarySearch:
    def search(self, arr, target):
        start = 0
        end = len(arr) - 1
        for i in range(len(arr)):
            mid = (start + end) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                start = mid + 1
            else:
                end = mid - 1 
        return -1


arrList = [14,15,18,20, 1,5,8,12,13,2]
findValue = 12

#create object
sortObject = BubbleSort() 
searchObject = BinarySearch()
print(arrList)
sortList = sortObject.datasorting(arrList)
print(sortList)

result = searchObject.search(sortList , findValue)
print(result)