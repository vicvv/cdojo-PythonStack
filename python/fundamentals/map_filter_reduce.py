


# map() function returns a list of the results after applying 
# the given function to each item of a given iterable (list, tuple etc.)

numbers = [2,3,4,5]
print(list(map(lambda x: x**2, numbers)))  #--> [4, 9, 16, 25]

mylist = [5, 6, 7]
newlist = list(map(lambda x: x**2, mylist)) #-->[25, 36, 49]
print(newlist)

#FILTER() As the name suggests, filter creates a list of elements for which a function returns true.
#Given the list shown below:
mylist =[2,3,4,6,7,9,11]
#Write a filter to produce the following output:
#[3, 7, 9, 11]
print( list(filter(lambda x: x%2 != 0, mylist)))
print("filter:", list(filter(lambda x: x > 4, mylist)))

#reduce

# is a function for performing some computation on 
# a list and returning the result. It applies a rolling computation 
# to sequential pairs of values in a list. For example, if you wanted 
# to compute the product of a list of integers.

# So the normal way you might go about doing this task in python is 
# using a basic for loop:

product = 1
list = [1, 2, 3, 4]
for num in list:
    product = product * num

# product = 24
#Now let’s try it with reduce:

from functools import reduce
product = reduce((lambda x, y: x * y), [1, 2, 3, 4])

# Output: 24

from functools import reduce
print(reduce(lambda x, y: x + y, numbers))

# converts strings into sentences
strings = ["This", "is", "us"]
print(strings)
print(reduce(lambda x, y: x +  ' ' + y, strings))  #—> prints This is us

myitems = [1,2,3]
print(reduce(lambda x,y: x+y, myitems)) #—> finds sum --> prints 6