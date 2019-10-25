
#BUBBLE SORT ARRAY

array = [8,2,1,5,3,6]

def myBblsort(array):
    count = 0
    for j in range(len(array)- 1):
        for i in range(len(array)- 1 - j):
            count += 1
            print("*" * 80 )
            if array[i] > array[i+1]:
                print("index:", i, "swapping", array[i], "and", array[i+1])
                array[i], array[i+1] =  array[i+1],array[i]
                print("new array:", array)
            else:
                print("no need to swap", array[i], "and", array[i+1])
    print("number of evaluations: ", count)
    return array

print("yay I bubble sort the array!!!", myBblsort(array))
            
