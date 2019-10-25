# Python implementation of the approach 

# Node class 
class Node: 
	def __init__(self, data): 
		self.data = data 
		self.next = None

# Function to push the new node 
# to head of the linked list 
def push(head, data): 

	# If head is null return new node as head 
	if not head: 
		return Node(data) 
	temp = Node(data) 
	temp.next = head 
	head = temp 
	return head 

# Function to find the sum of all odd 
# frequency nodes of the linked list 
def sumOfOddFreqEle(head): 

	# Hash to store the frequencies of 
	# the nodes of the linked list 
	mp ={} 
	temp = head 
	while(temp): 
		d = temp.data 
		if d in mp: 
			mp[d]= mp.get(d)+1
		else: 
			mp[d]= 1
		temp = temp.next
	
	# Initialize total_sum as zero 
	total_sum = 0

	# Traverse through the map to get the sum 
	for digit in mp: 

		# keep tracking the to 
		tms = mp.get(digit) 

		# If it appears for odd number of 
		# times then add it to the sum 
		if tms % 2 == 1: 
			total_sum+=(tms * digit) 
	return total_sum 

def sum_recursive(head):
	if head != None:
		temp = head.data
		print(temp)
		if head.data > 0:
			return (head.data + sum_recursive(head.next))

	return 0

# def sum_list(head):
# 	nsum = None
# 	msum = head.data
# 	while head:
# 		head = head.next
# 		msum = msum + head.data

# 	return msum


# Driver code 
if __name__=='__main__': 
	head = None
	head = push(head, 8) 
	head = push(head, -2) 
	# head = push(head, 1) 
	# head = push(head, 4) 
	# head = push(head, 1) 
	# head = push(head, 8) 
	# head = push(head, 8) 

	#print(sumOfOddFreqEle(head)) 
	#print(sum_recursive(head))
	print(sum_list(head))
