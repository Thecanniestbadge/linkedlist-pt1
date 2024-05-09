#Name: Nicholas Vickery
#Date: 3/6/2024
#project: Linked List pt1


class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class linked_list:
    def __init__(self):
        self.head = node()

    def append(self,data):
        new_node=node(data)
        cur=self.head #address of head node of the list
        while cur.next != None:
            cur=cur.next
        cur.next=new_node


    def length(self):
        cur=self.head
        total = 0
        while cur.next !=None:
            total+=1
            cur=cur.next
        return total
    
    def display(self):
        elems= []
        cur_node = self.head
        while cur_node.next != None:
            cur_node=cur_node.next
            elems.append(cur_node.data)
        print(elems)

mylist = linked_list()

valid_input = False
while not valid_input:
    user_input = input("Enter numbers separated by spaces: ")
    numbers = user_input.split()
    
    if all(number.isdigit() for number in numbers):  # Check if all inputs are numbers
        valid_input = True  # Exit the loop if all inputs are valid numbers
        # Insert numbers into the list
        for number in numbers:
            mylist.append(int(number))
    else:
        print("Error: Please enter numbers only.")

# Display list
mylist.display()

# Display the length of the list
print("Length:", mylist.length())