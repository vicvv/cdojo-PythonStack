class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Slist:
    #count = 1
    def __init__(self):
        self.head = None
    
    ################ ADD STARTS ###############
    def add_to_front(self, value):
        nn = Node(value)
        nn.next = self.head
        self.head = nn
        #Slist.count += 1
        return self

    def add_to_the_back(self,value):
        if self.head is None:
            nn = Node(value)
            nn.next = self.head
            self.head = nn
            #Slist.count += 1
            return self

        runner = self.head
        while runner.next != None:
            runner = runner.next
        #print(runner.next)
        runner.next = Node(value)
        #Slist.count += 1
        return self

    ######################### ADD ENDS ###############

    ####################### REMOVE STARTS ############

    def remove_from_front(self):
        if self.head == None:
            print("Empty list, nothing to remove")
            return None   
        self.head = self.head.next
        #Slist.count -= 1
        return self

    def remove_from_back(self):
        #check if list is not empty

        runner = self.head
        while runner.next.next != None:
            runner = runner.next
        #print("One before the last",runner.value)
        Slist.count -= 1
        runner.next = None

#delete by postition with while loop
    def delete_by_position(self, pos):
        if self.head == None:
            return self
        if pos == 0:
            self.head = self.head.next
            return self
        current_position = 0
        runner = self.head
        temp = None
       
        while runner.next != None and pos > current_position:
            temp = runner
            runner = runner.next
            current_position += 1

        if pos > current_position:
            print("Provided position is outside of the list scope")
            return self
        temp.next = runner.next       
        return self



# remove by pos with forin
    def remove_by_pos_with_forin(self,pos):
        if self.head == None or pos < 0:
            print("list is empty, exiting")
            return self
        runner = self.head

        for _ in range(pos - 1):
            if runner.next == None:
               return self
            runner=runner.next

        runner.next = runner.next.next
        return self

    ######################## REMOVE ENDS #############
    ######################## INSERTS STARTS ###########

    # insert before position
    def insert_before_pos(self, val, pos):

        nn = Node(val)
        if pos == 0:
            print("I am here")
            nn.next = self.head
            self.head = nn
            return self

        temp = None
        current_pos = 0
        runner = self.head

        while runner.next != None and pos > current_pos:
            temp = runner
            runner= runner.next
            current_pos += 1
        
        if temp == None and pos == 1:
            runner.next = nn
        # check if the loop has ever executed
        if pos > current_pos:
            print("The position provide was outside the scope, exiting")
            return self
        
        
        temp.next = nn
        nn.next = runner
            
            


    # def insert_by_position(self, value, position):
    #     if self.head == None:
    #         self.add_to_front(value)
    #     if position > Slist.count - 1 or position <= 0:
    #         print(f"bad insert position {position}, should be no higher than {Slist.count - 1 }")
    #         return self   
    #     current_position = 0
    #     runner = self.head
    #     temp = None
    #     nn = Node(value)
        
    #     while runner.next != None:
    #         current_position += 1
    #         temp = runner
    #         runner = runner.next
    #         if current_position == position:
    #             break
            
    #     temp.next = nn
    #     nn.next = runner
    #     Slist.count += 1
    #     return self

    ############## Delete by value ######################################

    def delete_by_value(self, value):
        if self.head == None:
            return self
        runner = self.head
        while runner:
            if runner.next.value == value:
                break
            else:
                runner = runner.next 
                
        #print(lets check if value was in the list)
        if runner.next == None:
            print(f"Cant find node with value {value} exiting")
            return self

        runner.next = runner.next.next
        return self  


    # delete all negatives:

    def delete_all_negatives(self):
        
        if self.head == None:
            return self

        runner = self.head

        while runner.next != None:
            if runner.next.value < 0:
                runner.next = runner.next.next
            else:
                runner = runner.next

        if self.head.value < 0:
            self.head = self.head.next
        return self
        
    #print list ##################
    
    def traverse_the_list_old_way(self):
        if self.head == None:
            print("list empty")
            return self
        runner = self.head
        count = 1
        while runner.next != None:
            
            print("runner value:",runner.value)
            count += 1
            runner = runner.next
        
        print("runner value ",runner.value)
        return self


    def traverse_the_list(self):
        if self.head == None:
            print("list empty")
            return self
        runner = self.head
        count = 1
        while runner != None:
            
            print("runner value:",runner.value)
            count += 1
            runner = runner.next
        return self


myslist = Slist()

myslist.add_to_front(-1)
myslist.add_to_front(1)
myslist.add_to_front(2)
myslist.add_to_front(-3)
myslist.add_to_front(-5)
print("**************** ")
# myslist.traverse_the_list()

myslist.add_to_the_back(-9)

print("\n\n****************  ")
myslist.traverse_the_list()
#myslist.delete_by_position(3)
print("\n\n**Delete by positon with for_in  ")
#myslist.remove_by_pos_with_forin(2)
myslist.delete_all_negatives()
myslist.traverse_the_list()

# myslist.remove_from_front()
# print("********removef from front ********")
# myslist.traverse_the_list()
# print("****going to remove from back****")
# myslist.remove_from_back()
# myslist.traverse_the_list()
#print("\n\n****************  insert before pos ")
#myslist.insert_before_pos(7,0)
#myslist.insert_before_pos("vita",3)

#myslist.insert_before_pos("vita",20)
#myslist.insert_before_pos("vita",1)
#myslist.insert_by_position(f"ten was inserted after position:{position}, and a count is:",position)
#myslist.traverse_the_list()

#myslist.delete_by_value("ten:")
#myslist.traverse_the_list()
