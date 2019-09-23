'''
    Course: CS2302 Data Structures Fall 2019
    Author: Bryan Ramos [88760110]
    Assignment: Lab 2 Sorting
    Instructor: Dr. Olac Fuentes
    TA: Anindita Nath 
    Last Modified: September 20th 2019
    Purpose: Implementing sorting algorithms like bubble sort and quick sort to understand how they function, implement quick sort using a stack and implement modified with no stack or recursion. Understand the differences in their run times.
'''

import time as t
import random as rand

# ---------- PART 1 ----------

# bubble sort
def select_bubble(L, k):
    for i, num in enumerate(L):
        try:
            if L [i+1] < num:
                L[i] = L[i+1]
                L[i+1] = num
                select_bubble(L, k)
        except IndexError:
            pass
    return L[k]

# take the last element as a pivot, the pivot element is placed in the 
# correct position, and places all smaller (smaller than pivot) values
# to the left of pivot and all greater elements to the right
# smaller <- pivot -> larger
def partition(L, low, high):
    # smaller element index
    i = low - 1
    pivot = L[high]

    for j in range(low, high):
        # current element is smaller than the pivot
        if L[j] < pivot:
            # increment index of smaller element
            i = i + 1
            L[i], L[j] = L[j], L[i]
    L[i + 1], L[high] = L[high], L[i + 1]
    return (i + 1)

def quicksort(L, low, high):
    if low < high:
        # partioning index, L[p] is now at right place
        partitionIndex = partition(L, low, high)

        # separately sort elements before partition and after partition
        quicksort(L, low, partitionIndex - 1)
        quicksort(L, partitionIndex + 1, high)

def select_quick(L, k):
    quicksort(L, 0, len(L) - 1)
    return L[k]

def quicksort_modified(L, low, high):
    while low < high:
        partitionIndex = partition(L, low, high)

        # separately sort element before partition and after partition
        quicksort_modified(L, low, partitionIndex - 1)
        low = partitionIndex + 1

def select_modified_quick(L, k):
    quicksort_modified(L, 0, len(L) - 1)
    return L[k]

# ---------- PART 2 ----------

class stackRecord:
    def __init__(self, L, low, high):  
        self.L = L
        self.low = low
        self.high = high

def select_quick_stack(L, low, high, k):
    stack = [stackRecord(L, low, high)]

    while len(stack) > 0:
        # get the last element
        stackElement = stack.pop(-1)
        if stackElement.low < stackElement.high:
            # partitionIndex -> get pivot value
            partitionIndex = partition(stackElement.L, stackElement.low, stackElement.high)

            # add in left and right sublists
            stack.append(stackRecord(stackElement.L, stackElement.low, partitionIndex - 1))
            stack.append(stackRecord(stackElement.L, partitionIndex + 1, stackElement.high))
    return L[k]

def select_quick_while(L, low, high, k):
    pivot = partition(L, low, high)

    while pivot != k:
        if k > pivot:
            pivot = partition(L, pivot + 1, high)
        elif k < pivot:
            pivot = partition(L, low, pivot - 1)
    return L[pivot]

# ---------- MAIN ----------

def printSuffix(k):
    # suffix to add after the kth element number
    if k[-1] == "1":
        print("st", end="")
    elif k[-1] == "2":
        print("nd", end="")
    elif k[-1] == "3":
        print("rd", end="")
    else:
        print("th", end="")

if __name__ == '__main__':

    # empty list to add random int values to
    numsList = []

    # ask for len of list and build a list from user input int values
    length = int(input("Enter desired length of list: "))
        
    # add random integer values to list from 0-50
    for i in range(length):
        numsList.append(rand.randint(0, 50))

    # lists to use in each sorting operation will have same values as numsList
    list1 = numsList
    list2 = numsList
    list3 = numsList
    list4 = numsList
    list5 = numsList

    print("List:", numsList)

    # ask user to the value for k -> must be an integer value
    k = 0
    while (True):
        try:
            k = int(input("Enter a value for k: "))
            break
        except: 
            print("\nInvalid! Please enter an integer number.\n")

    # sort using either: bubble sort, quick sort or modified quicksort
    # find kth smallest element in the sorted list

    # k should be less than the len of the list & cannot be less than 0
    if (k >= len(numsList)) or k < 0:
        print("\nError: Value for k out of bounds. List size:", len(numsList), "\n")
    else:
        print("")

        # bubble sort
        start = t.time()
        numAtIndex = select_bubble(list1, k)
        stop = t.time()
        print("Bubble sort:", k+1, end="")
        printSuffix(str(k + 1))
        print(" smallest element is", numAtIndex)
        print("It took", round(stop-start, 6), "seconds to sort and find k.")

        print("")

        # quicksort
        start = t.time()
        numAtIndex = select_quick(list2, k)
        stop = t.time()
        print("Quicksort:", k+1, end="")
        printSuffix(str(k + 1))
        print(" smallest element is", numAtIndex)
        print("It took", round(stop-start, 6), "seconds to sort and find k.")

        print("")

        # modified quicksort
        start = t.time()
        numAtIndex = select_modified_quick(list3, k)
        stop = t.time()
        print("Modified Quicksort:", k+1, end="")
        printSuffix(str(k + 1))
        print(" smallest element is", numAtIndex)
        print("It took", round(stop-start, 6), "seconds to sort a find k.")

        print("")

        # quicksort with stack implem.
        start = t.time()
        numAtIndex = select_quick_stack(list4, 0, len(list4) - 1, k)
        stop = t.time()
        print("Quicksort with Stack:", k+1, end="")
        printSuffix(str(k + 1))
        print(" smallest element is", numAtIndex)
        print("It took", round(stop-start, 6), "seconds to sort a find k.")

        print("")

        # quicksort with a while loop
        start = t.time()
        numAtIndex = select_quick_while(list5, 0, len(list5) - 1, k)
        stop = t.time()
        print("Quicksort with only a while loop:", k+1, end="")
        printSuffix(str(k + 1))
        print(" smallest element is", numAtIndex)
        print("It took", round(stop-start, 6), "seconds to sort.")
