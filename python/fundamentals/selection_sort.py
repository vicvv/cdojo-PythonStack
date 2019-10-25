
# SELECTION SORT works by iterating through the list, finding the 
# minimum value, and moving it to the beginning of the list. Then, 
# ignoring the first position, which is now sorted, iterate through 
# the list again to find the next minimum value and move it to index 1. 

arr = [7,3,24,8,9,0,1,4]

def mySelectionSort(arr):
    print("in funcition")

    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
print(mySelectionSort(arr))


