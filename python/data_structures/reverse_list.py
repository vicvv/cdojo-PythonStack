

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

# Initialize three pointers prev as NULL, curr as head and next as NULL.
# Iterate trough the linked list. In loop, do following.
# // Before changing next of current,
# // store next node
# next = curr->next
# // Now change next of current
# // This is where actual reversing happens
# curr->next = prev

# // Move prev and curr one step forward
# prev = curr
# curr = next


    def reverse_list(self): 
        temp1 = None
        temp2 = None
        runner = self.head 
        while(runner): 
            temp2 = runner.next
            runner.next = temp1 
            temp1 = runner 
            runner = temp2
        self.head = runner

mylist = Slist()
mylist.addfront(1)
mylist.addfront(2)
mylist.addfront(3)

mylist.printlist()
print('\n','#'*50)
mylist.reverse_list()
mylist.printlist()