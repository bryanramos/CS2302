'''
    Course: CS2302 Data Structures Fall 2019
    Author: Bryan Ramos [88760110]
    Assignment: Lab 2 Sorting
    Instructor: Dr. Olac Fuentes
    TA: Anindita Nath 
    Last Modified: September 20th 2019
    Purpose: 
'''

import time as t

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

def printSuffix(k):
    if k[-1] == "1":
        print("st", end="")
    elif k[-1] == "2":
        print("nd", end="")
    elif k[-1] == "3":
        print("rd", end="")
    else:
        print("th", end="")

# ask the user for length of list, ask for values for list
# sort using either: bubble sort, quick sort or modified quicksort
# find kth smallest element in the sorted list
def part1():

    numsList = []
    while (True):
        length = int(input("Enter desired length of list: "))
        for i in range(length):
            # only allow integer numbers be added to the list
            try: 
                value = int(input("Enter an integer to add to the list: "))
                numsList.append(value)
            except ValueError:
                print("\nError: Only integer numbers are allowed.\n")
                return
        break

    print("\nList:", numsList)

    while (True):

        # sorting menu
        print("1. Bubble Sort\n2. Quicksort\n3. Modified Quicksort\n4. Return to Main Menu")
        choice = input("Choose the sorting algorithm to run: ")

        # sorting choice switch
        if choice == "1":
            k = 0
            try:
                k = int(input("Enter a value for k: "))
            except: 
                print("\nInvalid! Please enter a integer number.\n")

            # k should be less than the len of the list & cannot be less than 0
            if (k >= len(numsList)) or k < 0:
                print("\nError: Value for k out of bounds.\n")
                continue

            start = t.time()
            L, numAtIndex = select_bubble(numsList, k)
            stop = t.time()

            print("\nList sorted with bubble sort:", L)
            print(k, end="")
            printSuffix(str(k));
            print(" smallest element is", numAtIndex)
            
            print("It took", round(stop-start, 6), "seconds to sort.\n")

        elif choice == "2":
            # quick sort
            print("")
        elif choice == "3":
            # modified quick sort
            print("")
        elif choice == "4":
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
            print("")
        elif choice == "3" or not choice:
            print("Bye thanks for using the program!\n")
            break
        else:
            print("Invalid! Please choose a valid option.\n")

