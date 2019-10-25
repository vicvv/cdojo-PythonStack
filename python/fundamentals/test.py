#find([1,2,3,4,5,6], lambda x: x>4)
# lst = [1,2,3,4,5,6]
# print(list(i for i in lst if i > 4)[0])

# res = next(x for x, val in enumerate(lst) if val > 4)
# print(res)

# res1 = list(filter(lambda i: i > 4, lst))[0]
# print(res1)




# res4 = list(filter(lambda x: x%2 == 0, lst))
# print(res4)

# print(set(lst) - set(res4))


students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

def iterateDictionary(students) :
    for x in students:

        #result = " ".join(str(key) + " - " + str(value) for key, value in item.items())
        print({key: value for key, value in x.items()})
        
            

iterateDictionary(students)


dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# Put all keys of `dict1` in a list and returns the list
print(dict1.keys())
print(dict1.values())


print(dict1)
dict1_keys = {k : v for (k,v) in dict1.items()}
print(*dict1_keys)



