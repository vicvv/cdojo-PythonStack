#1 my predictoin: prints 5 
def a():
    return 5
print(a())



#2 my prediction: prints 10
def a1():
    return 5
print(a1()+a1())


#3 my prediction: prints 5. Second retur is ingored or maybe it wont even run...
def a2():
    return 5
    return 10

print(a())

#4 my prediction: prints 5 because print statement in the funct is after return
def a3():
    return 5
    print(10)
print(a3())


#5 my prediction :None. Function does not return anuthing
def a4():
    print(5)

x = a4()
print(x)


#6 my prediction Error... 
def a5(b,c):
    print(b+c)
#print(a5(1,2) + a5(2,3))


#7 my prediction: 25
def a6(b,c):
    return str(b)+str(c)
print(a6(2,5))


#8 my prediction: 100 10
def a7():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(a7())


#9 my prediction  7  14 21
def a8(b,c):
    if b < c:
        return 7
    else:
        return 14
    return 3
print(a8(2,3))
print(a8(5,3))
print(a8(2,3) + a8(5,3))


#10 my prediction: 8
def a9(b,c):
    return b+c
    return 10
print(a9(3,5))


#11 my prediction: 500 500 300 500  because a10 does not return anything so the b external
# will not change
b = 500
print(b)
def a10():
    b = 300
    print(b)
print(b)
a10()
print(b)


#12 my prediction: 500 500 300 500 because return from function is not assig to anything
b = 500
print(b)
def a11():
    b = 300
    print(b)
    return b
print(b)
a11()
print(b)

#13 my prediction: 500 500 300 300
b = 500
print(b)
def a12():
    b = 300
    print(b)
    return b
print(b)
b=a12()
print(b)


#14 my prediction: 1  3  2
def a14():
    print(1)
    b1()
    print(2)
def b1():
    print(3)
a14()


#15  my prediction: 1 3 5 10
def a15():
    print(1)
    x = b15()
    print(x)
    return 10
def b15():
    print(3)
    return 5
y = a15()
print(y)
