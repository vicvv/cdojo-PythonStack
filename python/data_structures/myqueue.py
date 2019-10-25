class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Q:
    def __init__(self):
        self.first = self.last = None

    def isEmpty(self):
        return self.first == None

    def enQ(self, value):
        nn = Node(value)

        if self.last == None:
            self.last = self.first = nn
            return
        self.last.next = nn
        self.last = nn

    def deQ(self):

        if self.isEmpty:
            return
        
        temp = self.first
        self.first.next = temp.next

        if self.first == None:
            self.last = None
        print(temp.value)
        return str(temp.value)

q = Q()

q.enQ(1)
q.enQ(2)
q.enQ(3)
q.enQ(4)

mydq = q.deQ()
print(mydq)


