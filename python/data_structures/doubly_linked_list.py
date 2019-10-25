
class Node:
    def __init__(self, data):
        self.item = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.start_node = None

    # insert new node into empty list
    def insert_in_empty_list(self,data):
        if self.start_node == None:
            newnode = Node(data)
            self.start_node = newnode
        else:
            print("list is not empty")

    # insert the node at the beginnoing

    def insert_at_the_beginning(self, data):
        if self.start_node == None:
            self.insert_in_empty_list(data)
            return
        newnode = Node(data)
        newnode.next = self.start_node
        self.start_node.previous = newnode
        self.start_node = newnode


# Inserting an element at the end of the doubly linked list is somewhat similar to inserting 
# an element at the start. At first, we need to check if the list is empty. 
# If the list is empty then we can simply use the insert_in_emptylist() method to insert 
# the element. If the list already contains some element, we traverse through the list 
# until the reference to the next node becomes None. When the next node reference becomes 
# None it means that the current node is the last node.

# The previous reference for the new node is set to the last node, and the next reference 
# for the last node is set to the newly inserted node. The script for inserting an item 
# at the last node is as follows:
    
    def insert_at_end(self, data):
        if self.start_node is None:
            self.insert_in_empty_list(data)
            return

        current = self.start_node
        while current.next is not None:
            current = current.next
        new_node = Node(data)
        current.next = new_node
        new_node.prev = current
       
# Inserting Item after another Item
# To insert an item after another item, we first check whether or not the list is empty. 
# If the list is actually empty, we simply display the message that the "list is empty".

# Otherwise we iterate through all the nodes in the doubly linked list. In case if 
# the node after which we want to insert the new node is not found, we display the
#  message to the user that the item is not found. Else if the node is found, 
# it is selected and we perform four operations:

# Set the previous reference of the newly inserted node to the selected node.
# Set the next reference of the newly inserted node to the next reference of the selected.
# If the selected node is not the last node, set the previous reference of the next 
# node after the selected node to the newly added node.
# Finally, set the next reference of the selected node to the newly inserted node.
# The script for inserting item after another item is as follows:

    def insert_after_item_by_value(self, x, data):
        if self.start_node is None:
            self.insert_in_empty_list(data)
            return
        current = self.start_node
        while current != None:
            if current.item == x:
                break
            current = current.next
        if current is None:
            print("No node with provided value found")
            return
        else:
            newnode = Node(data)
            newnode.next =  current.next
            newnode.prev = current
            if current.next is not Node:
                current.prev= newnode
            current.next = newnode


# Inserting Item before another Item
# To insert an item before another item, we first check whether or not the list is empty. 
# If the list is actually empty, we simply display the message that the "list is empty".

# Otherwise we iterate through all the nodes in the doubly linked list. In case if the 
# node before which we want to insert the new node is not found, we display the message to 
# the user that the item is not found. Else if the node is found, it is selected and we 
# perform four operations:

# Set the next reference of the newly inserted node to the selected node.
# Set the previous reference of the newly inserted node to the previous reference of the selected.
# Set the next reference of the node previous to the selected node, to the newly added node.
# Finally, set the previous reference of the selected node to the newly inserted node.
# The script for adding item before another item in a doubly linked list is as follows:


    def insert_before_the_item_by_value(self, x, data):
        if self.start_node is None:
            print("List is empty")
            return
        else:
            n = self.start_node
            while n is not None:
                if n.item == x:
                    break
                n = n.next
            if n is None:
                print("item not in the list")
            else:
                new_node = Node(data)
                new_node.next = n
                new_node.prev = n.prev
                if n.prev is not None:
                    n.prev.next = new_node
                n.prev = new_node
      

    def print_dd_list(self):
        if self.start_node is None:
            print("List is empty")
            return
        current = self.start_node
        print("\n\nMY LIST:  ", end = '')
        while (current != None):
            print(current.item, end = ' ')
            current = current.next 	# set the runner to its neighbor
        return self # once the loop is done, return self to allow for chaining

    
    def delete_at_start(self):
        if self.start_node is None:
            print("The list has no element to delete")
            return 
        if self.start_node.nref is None:
            self.start_node = None
            return
        self.start_node = self.start_node.nref
        self.start_prev = None

    def delete_at_end(self):
        if self.start_node is None:
            print("The list has no element to delete")
            return 
        if self.start_node.nref is None:
            self.start_node = None
            return
        n = self.start_node
        while n.nref is not None:
            n = n.nref
        n.pref.nref = None


    def delete_element_by_value(self, x):
        if self.start_node is None:
            print("The list has no element to delete")
            return 
        if self.start_node.nref is None:
            if self.start_node.item == x:
                self.start_node = None
            else:
                print("Item not found")
            return 

        if self.start_node.item == x:
            self.start_node = self.start_node.nref
            self.start_node.pref = None
            return

        n = self.start_node
        while n.nref is not None:
            if n.item == x:
                break
            n = n.nref
        if n.nref is not None:
            n.pref.nref = n.nref
            n.nref.pref = n.pref
        else:
            if n.item == x:
                n.pref.nref = None
            else:
                print("Element not found")

mydlist = DoublyLinkedList()
mydlist.insert_at_the_beginning("first")
mydlist.insert_at_end("last")
mydlist.insert_at_end("last_again")
mydlist.insert_after_item_by_value("last", "before-last_again")
mydlist.insert_before_the_item_by_value("before", "last")
mydlist.print_dd_list()


        
        




