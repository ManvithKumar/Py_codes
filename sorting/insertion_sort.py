def insertion_sort(arr):
    n=len(arr)
    for i in range(1,n):
        key=arr[i]
        j=i-1
        while j>=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j =j- 1
        arr[j+1]=key

elements = [39, 12, 18, 85, 72, 10, 2, 18]
 
print("Unsorted list is,")
print(elements)
insertion_sort(elements)
print("Sorted Array is, ")
print(elements)