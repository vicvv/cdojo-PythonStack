class Underscore:
    def map(self, iterable, callback):
        result = list(map (callback ,iterable))
        print(result)
        return result
    def find(self, iterable, callback):
        res1 = list(filter(callback, iterable))[0]
        print(res1)
        return res1
    def filter(self, iterable, callback):
        res2 = list(filter(callback, iterable))
        print(res2)
        return res2
    def reject(self, iterable, callback):
        res3 = list(filter(callback, iterable))
        print(set(iterable) - set(res3))
        newres3 = list(set(iterable) - set(res3))
        print(newres3)
        return newres3

# you just created a library with 4 methods!
# let's create an instance of our class
_ = Underscore() # yes we are setting our instance to a variable that is an underscore
evens = _.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
# should return [2, 4, 6] after you finish implementing the code above
_.map([1,2,3], lambda x: x*2) # should return [2,4,6]
_.find([1,2,3,4,5,6], lambda x: x>4) # should return the first value that is greater than 4
_.filter([1,2,3,4,5,6], lambda x: x%2==0) # should return [2,4,6]
_.reject([1,2,3,4,5,6], lambda x: x%2==0) # should return [1,3,5]