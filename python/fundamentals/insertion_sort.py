# INSERTION SORT works by starting at index 1, shifting that value to the left until it is 
# sorted relative to all values to the left, and then moving on to the next index position 
# and performing the same shifts until the end of 
# the list is reached. 

arr = [6,3,4, 9,1,2,5,3]

def insertionSort(arr): 
  
    # Traverse through 1 to len(arr) 
    for i in range(1, len(arr)): 
        current_value = arr[i]  
        #print("*"*50)
        #print("i is", i, "current_value of arr[i] is ", current_value )
        # Move elements of arr[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position 
        j = i-1
        print("j is:", j)
        while j >= 0 and current_value < arr[j] : 
            #print(current_value, "< arr[",j,"] ", arr[j], "swaping..." )
            arr[j + 1] = arr[j] 
            #print("current_array: ", arr)
            j -= 1
        #print("arr[j + 1] gets current_value")
        arr[j + 1] = current_value 
        #print("current_array: ", arr)
    return arr

print(insertionSort(arr))

