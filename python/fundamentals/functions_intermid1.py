# write a single function, randInt() that takes up to 2 arguments.

# If no arguments are provided, the function should return a random integer between 0 and 100.
# If only a max number is provided, the function should return a random integer between 0 and the max number.
# If only a min number is provided, the function should return a random integer between the min number and 100
# If both a min and max number are provided, the function should return a random integer between those 2 values.
# Here are a couple of important notes about using random.random() and rounding. (Create this function without using 
# random.randInt() -- we are trying to build that method ourselves for this assignment!)

# random.random() returns a random floating number between 0.000 and 1.000
# random.random() * 50 returns a random floating number between 0.000 and 50.000
# random.random() * 25 + 10 returns a random floating number between 10.000 and 35.000
# round(num) returns the rounded integer value of num


import random
def randInt(min = None, max = None):
    if not min and not max:
        num = random.random()
        num = int(num*100)
        return num

    if not min:
        num = random.random()*max
        return int(num)
    if not max:
        num = random.random()* min + 50
        return int(num)
    if max and min:
        num = random.random()* min + (max - min)
        return int(num)
    if min > max:
        return False
    if max < 0:
        return False

    
print(randInt()) 		# should print a random integer between 0 to 100
print(randInt(max=50)) 	# should print a random integer between 0 to 50
print(randInt(min=50)) 	# should print a random integer between 50 to 100
print(randInt(min=50, max=500))    # should print a random integer between 50 and 500
