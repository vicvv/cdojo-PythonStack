import copy 
class _ListNode:
    def __init__(self, value, next_):
        self._value = copy.deepcopy(value)
        self._next = next_
        return
class List:
    def __init__(self):
        self._front = None
        self._count = 0
        return
    def addToFront(self, value):
        if self._front == None:
            self._front = _ListNode(value, None)
        else:
            buffer = _ListNode(value, self._front)
            self._front = buffer

    def addToEnd(self, value):
        current = self._front
        if current:
            while current._next != None:
                current = current._next
            current._next = _ListNode(value, None)
        else:
            self._front = _ListNode(value, None)

    def __str__(self):
        buffer = self._front
        result = ""
        while buffer._next != None:
            result+= buffer._value + " > "
            buffer = buffer._next
        result+= buffer._value
        return result

    def copy(self):
        result = List()
        buffer = self._front
        while buffer._next != None:
            result.addToEnd(buffer._value)
            buffer= buffer._next
        result.addToEnd(buffer._value)
        return result

##test:
x = List()
x.addToFront("f")
x.addToFront("e")
x.addToFront("d")
x.addToFront("c")
x.addToFront("b")
x.addToFront("a")
print(x)
print(x.copy())