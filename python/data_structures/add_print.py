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

    def printlist(self):
        runner = self.head
        while(runner):
            print(runner.value, end = " ")
            runner = runner.next

mylist = Slist()
mylist.addfront(3)
mylist.addfront(3)
mylist.addfront(3)

mylist.printlist()