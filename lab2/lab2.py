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

# ---------- PART 1 ----------

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
    return L, L[k]

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
    return L, L[k]

def quicksort_modified(L, low, high):
    while low < high:
        partitionIndex = partition(L, low, high)

        # separetly sort element before partition and after partition
        quicksort_modified(L, low, partitionIndex - 1)
        low = partitionIndex + 1

def select_modified_quick(L, k):
    quicksort_modified(L, 0, len(L) - 1)
    return L, L[k]

# ask the user for len of list, ask for values for list
# sort using either: bubble sort, quick sort or modified quicksort
# find kth smallest element in the sorted list
def part1():
    numsList = []

    while (True):
        # ask for len of list and build a list from user input int values
        length = int(input("Enter desired length of list: "))
        for i in range(length):
            # only allow int nums be added to the list
            try:
                value = int(input("Enter an integer to add to the list: "))
                numsList.append(value)
            except ValueError:
                print("\nError: Only integer numbers are allowed.\n")
                return
        break

    print("\nUnsorted List:", numsList)

    while (True):
        # sorting menu for Part 1
        print("1. Bubble Sort\n2. Quicksort\n3. Modified Quicksort\n4. Return to Main Menu")
        choice = input("Choose the algorithm to run: ")

        # sorting choice switch
        if choice == "1":
            # bubble sort
            k = 0
            while (True):
                try:
                    k = int(input("Enter a value for k: "))
                    break
                except: 
                    print("\nInvalid! Please enter a integer number.\n")

            # k should be less than the len of the list & cannot be less than 0
            if (k >= len(numsList)) or k < 0:
                print("\nError: Value for k out of bounds. List size:", len(numsList), "\n")
                continue

            start = t.time()
            L, numAtIndex = select_bubble(numsList, k)
            stop = t.time()

            print("\nList sorted with bubble sort:", L)
            print(k+1, end="")
            printSuffix(str(k + 1))
            print(" smallest element is", numAtIndex)

            print("It took", round(stop-start, 6), "seconds to sort.\n")
        elif choice == "2":
            # quicksort
            k = 0
            while (True):
                try:
                    k = int(input("Enter a value for k: "))
                    break
                except: 
                    print("\nInvalid! Please enter a integer number.\n")

            # k should be less than the len of the list & cannot be less than 0
            if (k >= len(numsList)) or k < 0:
                print("\nError: Value for k out of bounds. List size:", len(numsList), "\n")
                continue

            start = t.time()
            L, numAtIndex = select_quick(numsList, k)
            stop = t.time()

            print("\nList sorted with bubble sort:", L)
            print(k+1, end="")
            printSuffix(str(k + 1))
            print(" smallest element is", numAtIndex)

            print("It took", round(stop-start, 6), "seconds to sort.\n")
        elif choice == "3":
            # modified quick sort
            k = 0
            while (True):
                try:
                    k = int(input("Enter a value for k: "))
                    break
                except: 
                    print("\nInvalid! Please enter a integer number.\n")

            # k should be less than the len of the list & cannot be less than 0
            if (k >= len(numsList)) or k < 0:
                print("\nError: Value for k out of bounds. List size:", len(numsList), "\n")
                continue

            start = t.time()
            L, numAtIndex = select_modified_quick(numsList, k)
            stop = t.time()

            print("\nList sorted with bubble sort:", L)
            print(k+1, end="")
            printSuffix(str(k + 1))
            print(" smallest element is", numAtIndex)

            print("It took", round(stop-start, 6), "seconds to sort.\n")
        elif choice == "4":
            # return to main menu
            print("")
            return
        else:
            # invalid input
            print("Invalid! Please choose a valid option.\n")

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
    return L, L[k]

def select_quick_while(L, low, high, k):
    pivot = partition(L, low, high)

    while pivot != k:
        if k > pivot:
            pivot = partition(L, pivot + 1, high)
        elif k < pivot:
            pivot = partition(L, low, pivot - 1)
    return L, L[pivot]

def part2():
    numsList = []

    while (True):
        # ask for len of list and build a list from user input int values
        length = int(input("Enter desired length of list: "))
        for i in range(length):
            # only allow int nums be added to the list
            try:
                value = int(input("Enter an integer to add to the list: "))
                numsList.append(value)
            except ValueError:
                print("\nError: Only integer numbers are allowed.\n")
                return
        break

    print("\nUnsorted List:", numsList)

    while (True):
        # sorting menu
        print("1. Quicksort with Stack\n2. Quicksort Only While Loop\n3. Return to Main Menu")
        choice = input("Choose the algorithm to run: ")

        if choice == "1":
            # quicksort with stack
            k = 0
            while (True):
                try:
                    k = int(input("Enter a value for k: "))
                    break
                except: 
                    print("\nInvalid! Please enter a integer number.\n")

            # k should be less than the len of the list & cannot be less than 0
            if (k >= len(numsList)) or k < 0:
                print("\nError: Value for k out of bounds. List size:", len(numsList), "\n")
                continue

            start = t.time()
            L, numAtIndex = select_quick_stack(numsList, 0, len(numsList) - 1, k)
            stop = t.time()

            print("\nList sorted with bubble sort:", L)
            print(k+1, end="")
            printSuffix(str(k + 1))
            print(" smallest element is", numAtIndex)

            print("It took", round(stop-start, 6), "seconds to sort.\n")
        elif choice == "2":
            # quicksort with while loop
            k = 0
            while (True):
                try:
                    k = int(input("Enter a value for k: "))
                    break
                except: 
                    print("\nInvalid! Please enter a integer number.\n")

            # k should be less than the len of the list & cannot be less than 0
            if (k >= len(numsList)) or k < 0:
                print("\nError: Value for k out of bounds. List size:", len(numsList), "\n")
                continue

            start = t.time()
            L, numAtIndex = select_quick_while(numsList, 0, len(numsList) - 1, k)
            stop = t.time()

            print("\nList sorted with bubble sort:", L)
            print(k+1, end="")
            printSuffix(str(k + 1))
            print(" smallest element is", numAtIndex)

            print("It took", round(stop-start, 6), "seconds to sort.\n")
        elif choice == "3":
            # return to main menu
            print("")
            return
        else:
            # invalid input
            print("Invalid! Please choose a valid option.\n")

if __name__ == '__main__':
    while (True):
        # primary menu
        print("1. Part 1\n2. Part 2\n3. Exit")
        choice = input("Choose the part of the lab to execute: ")

        # menu choice switch
        if choice == "1":
            part1()
        elif choice == "2":
            part2()
        elif choice == "3":
            print("Bye thanks for using the program!\n")
            break
        else:
            print("Invalid! Please choose a valid option.\n")