class MathDojo:
    def __init__(self):
    	self.result = 0

    def add(self, num, *nums):
        self.result += num
        for item in nums:
            self.result = self.result + item
        print("Add result",self.result)
        return self

    def subtract(self, num, *nums):
        self.result -= num
        for item in nums:
            self.result = self.result - item
        print("Substract result",self.result)
        return self

md = MathDojo()
# to test:
x = md.add(2).add(2,5,1).subtract(3,2).result
#x = md.subtract(10,2).result
print(x)	# should print 5
# run each of the methods a few more times and check the result!



