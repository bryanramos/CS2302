'''
    Course: CS2302 Data Structures Fall 2019
    Author: Bryan Ramos [88760110]
    Assignment: Lab 3 Linked Lists
    Instructor: Dr. Olac Fuentes
    TA: Anindita Nath 
    Last Modified: October 4th 2019
    Purpose: 
'''

import random as rand

class Node(object):
    # Constructor
    def __init__(self, data, next=None):  
        self.data = data
        self.next = next 
        
#List Functions
class List(object):   
    # Constructor
    def __init__(self): 
        self.head = None
        self.tail = None

    def Append(self, data):
        node = Node(data)
        current = self.head
        previous = None

        while current is not None and current.data < data:
            previous = current
            current = current.next

        if previous == None:
            self.head = node
        else:
            previous.next = node

        node.next = current

    def Print(self):
        # Prints list L's items in order using a loop
        t = self.head
        while t is not None:
            print(t.data, end=' ')
            t = t.next
        print()

if __name__ == "__main__":
    L = List() # create empty list to use for main output

    # fill list with values 0-10
    for i in range(0, 10):
        L.Append(i)

    while (True):
        print("Original List:")
        L.Print()
        print("")
        print("1. Print\n2. Insert\n3. Delete\n4. Merge\n5. IndexOf")
        print("6. Clear\n7. Min\n8. Max\n9. HasDuplicates\n10. Select")
        break;
    

