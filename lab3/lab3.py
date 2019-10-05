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
import math
import sys

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
    
    def Insert(self, i):
        self.Append(i)

    def Delete(self, i):
        previous = None
        t = self.head
        
        try:
            while t.data != i:
                previous = t
                t = t.next
        except:
            return None

        if t == self.head:
            self.head = t.next
        else:
            previous.next = t.next

    def IndexOf(self, i):
        t = self.head
        index = 0
        while t is not None:
            if t.data == i:
                return index
            index += 1
            t = t.next
        return -1

    def Clear(self):
        self.head = None

    def Min(self):
        t = self.head
        if t is None:
            return math.inf
        min = sys.maxsize
        while t is not None:
            if t.data < min:
                min = t.data
            t = t.next
        return min

    def Max(self):
        t = self.head
        if t is None:
            return -math.inf
        max = -sys.maxsize - 1
        while t is not None:
            if t.data > max:
                max = t.data
            t = t.next
        return max

    def HasDuplicates(self):
        t = self.head
        while t.next is not None:
            if t.data == t.next.data:
                return True
            t = t.next
        return False
    
    def Select(self, k):
        if self is None:
            return math.inf
        index = 0
        t = self.head
        while t is not None:
            if index == k:
                return t.data
            t = t.next

    def Merge(self, M):
        s = M.head
        while s is not None:
            self.Append(s.data)
            s = s.next
            
if __name__ == "__main__":
    L = List() # create empty list to use for main output
    M = List() # list for merging

    # fill list with random values between 0-50
    for i in range(0, 10):
        L.Append(i)

    for i in range(0, 10):
        M.Append(rand.randint(0,12))

    while (True):
        print("\n1. Print\n2. Insert\n3. Delete\n4. Merge\n5. IndexOf")
        print("6. Clear\n7. Min\n8. Max\n9. HasDuplicates\n10. Select\n11. Exit\n")

        option = input("Please choose an option: ")
        
        if option == "1": # print all contents of list
            L.Print()

        elif option == "2": # insert node
            try:
                number = int(input("Enter a number to add to the list: "))
            except ValueError:
                print("Invalid input provided! Please provide an integer number as input.")
                break
            L.Insert(number)

        elif option == "3": # delete node
            try:
                number = int(input("Enter a number to remove from the list: "))
            except ValueError:
                print("Invalid input provided! Please provide an integer number as input.")
                break
            L.Delete(number)

        elif option == "4": # merge 

            L.Print()
            M.Print()
            L.Merge(M)
            L.Print()

        elif option == "5": # indexof
            try:
                key = int(input("Enter a number to find in the list: "))
            except ValueError:
                print("Invalid input provided! Please provide an integer number as input.")
                break
            print(key, "is found at the following index:", L.IndexOf(key))

        elif option == "6": # clear list - delete all elements
            L.Clear()

        elif option == "7": # min value of list
            print("Min value in list:", L.Min())

        elif option == "8": # max value of list
            print("Max value in list:", L.Max())

        elif option == "9": # returns whether duplicates exist in list
            print("Duplicates in list:", L.HasDuplicates())

        elif option == "10": # returns the kth smallest element in the list
            try:
                K = int(input("Enter a number for k: "))
            except ValueError:
                print("Invalid input provided! Please provide an integer number as input.")
                break
            print("Value at position k:", L.Select(K))

        elif option == "11": # quit program
            print("Bye! Thanks for using the program!")
            break

        else: # invalid
            print("Invalid input!")


