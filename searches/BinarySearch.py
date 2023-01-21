def BinarySearch(arr,size,key):
    arr = sorted(arr)
    start = 0
    end = size
    while start <= end:
        mid = (start+end)//2
        if arr[mid] == key :
            return mid
        elif arr[mid] < key:
            start = mid + 1
        else:
            end = mid-1
    return -1

arr = [5,6,7,8,9,3,1]
size = len(arr)
key = 3
print(BinarySearch(arr,size,key))