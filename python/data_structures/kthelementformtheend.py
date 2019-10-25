class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Slist:
    #count = 1
    def __init__(self):
        self.head = None

    def addfront(self, val):
        nn = Node(val)
        nn.next = self.head
        self.head = nn


    def kthElemFromTheEnd(self,k):
        runner = self.head
        temp = self.head
        count = 1
        if k <= 0:
            return self

        while (count <= k and runner != None):      
            runner = runner.next
            print("count:", count, "runner.value=")
            if count == k:
                temp = runner
                print("in w",temp.value)
                count = 1
            temp = temp.next
            count += 1
        print("k after func:", temp.value)
        return temp.value





    def removeNthFromEnd(self, n):
        length, count, temp = 1, 1, self.head

        while temp.next:
            length, temp = length + 1, temp.next
        temp = self.head

        if length == n: return self.head.next

        while count < length - n:
            count, temp = count + 1, temp.next
        temp.next = temp.next.next
        print(temp.next.value)
        return self

    def kthwith2whileloops(self, k):
        runner = self.head
        count = 1

        while count < k:
            runner2 = runner.next
            count += 1

            while runner2.next:
                runner =  runner.next
                runner2 = runner2.next
        
        return runner.val



    def printlist(self):
        runner = self.head
        while(runner):
            print(runner.value, end = " ")
            runner = runner.next

mylist = Slist()
mylist.addfront(6)
mylist.addfront(5)
mylist.addfront(4)
mylist.addfront(3)
mylist.addfront(2)
mylist.addfront(1)

mylist.printlist()
k=2
print(f"the k={k} The kth element is:")
#mylist.kthElemFromTheEnd(k)
mylist.kthwith2whileloops(1)

#mylist.removeNthFromEnd(2)

mylist.printlist()
