# Create a Python file called for_loop_basic1.py that performs the following tasks.
# Basic - Print all integers from 0 to 150.

print(list(x for x in range (151)))

# Multiples of Five - Print all the multiples of 5 from 5 to 1,000

print(list(x for x in range(1001) if x%5 == 0))

# Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, 
# print "Coding" instead. If divisible by 10, print "Coding Dojo".

ar = [('Coding Dojo' if i % 10 == 0 else 'Coding' if i % 5 == 0  else i) for i in range(1, 101)]
print(ar)


# Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.

print(sum(list(i for i in range(5000000) if i%2 != 0)))

# Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.

print(list(i for i in range(2018,0, -4)))

# Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and 
# going through highNum, print only the integers that are a multiple of mult. For example, 
# if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)

lowNum=2 
highNum=9
mult=3
print(list(i for i in range (lowNum, highNum+1) if i%mult == 0))