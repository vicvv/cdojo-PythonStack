# import the python testing framework
import unittest
# our "unit"
# this is what we are running our test on
def reverseArray(mylist):
    for i in range(int((len(mylist)/2)-1)):
        mylist[i], mylist[len(mylist) - 1] = mylist[len(mylist) - 1], mylist[i]
    return mylist

def isPalindrome(mylist):
    myreversed = mylist[::-1]
    if myreversed == mylist:
        return myreversed
    else:
        return False
# our "unit tests"
# initialized by creating a class that inherits from unittest.TestCase
class reverseArrayTests(unittest.TestCase):
    # each method in this class is a test to be run
    def testTwo(self):
        self.assertEqual(reverseArray([1,2,3]), [1,2,3])
        #self.assertEqual(reverseArray([5,2,3]), [3,2,5])
        pass
    def testThree(self):
        self.assertEqual(isPalindrome("elle"),"elle")
        #self.assertEqual( isPalindrome("racecar"), True ) or self.assertTrue( isPalindrome("racecar"))
    def setUp(self):
        # add the setUp tasks
        print("running setUp")
    # any task you want run after the tests are executed, put them in the tearDown method
    def tearDown(self):               
        print("running tearDown tasks")





if __name__ == '__main__':
    unittest.main() # this runs our tests
