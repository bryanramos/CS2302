'''
    Course: CS2302 Data Structures Fall 2019
    Author: Bryan Ramos [88760110]
    Assignment: Lab 4 BSTs and BTrees
    Instructor: Dr. Olac Fuentes
    TA: Anindita Nath 
    Last Modified: October 21st 2019
    Purpose: Using both binary search trees and b-trees as deliberate practice 
    to read data from a file and store in either type of tree and then access 
    the data from the tree using operations to find the number of nodes, similarities
    between words, etc.
'''

import time
import bst
import btree
import os
import numpy as np
from wordEmbedding import WordEmbedding

# returns a built BST from the file
# if file not found, throw exception
def buildBST(filename):
    try:
        T = None
        # file uses utf8 encoding
        f = open(filename, "r", encoding="utf8")

        for line in f:
            # tokenize each line into a list of strings
            tokens = line.split(" ")
            # if the value stored at the index begins with an alphabetical letter
            if tokens[0].isalpha():
                T = bst.Insert(T, tokens[0], tokens[1:])
        
        f.close() # close the file to save memory
        return T # return bst
    except IOError:
        print("File", filename, "not found!\n") 

# returns a built B-tree from the file
# if file not found, throw exception
def buildBTree(max, filename):
    try:
        # set the max value of b tree to the value passed as max parameter
        T = btree.BTree([], max_data = max) 
        f = open(filename, "r", encoding="utf8")
        for line in f:
            # tokenize each line into a list of strings
            tokens = line.split(" ")
            # if the value stored at the index begins with an alphabetical letter
            if tokens[0].isalpha():
                btree.Insert(T, WordEmbedding(tokens[0], tokens[1:]))

        f.close() # close the file to save memory
        return T # return btree
    except IOError:
        print("File", filename, "not found!\n") 

def getEmbeddings(T,filename):
    totaltime = 0
    f = open(filename, "r")
    embeddings = []

    for line in f:
        # first remove new line char from line
        if "\n" in line:
            line = line[:-1]
        # split by commas
        words = line.split(",")

        # if its of type binary search tree
        if type(T) == bst.BST:
            start = time.time()
            first = bst.Search(T, words[0])
            second = bst.Search(T, words[1])

            if first == None or second == None: #if word is not in tree, just appends the string words
                embeddings.append(words)
            else:
                embeddings.append([first, second])

            totaltime = totaltime + (time.time() - start)
        # if its of type Btree - similar code as the one for BST above
        if type(T) == btree.BTree:
            start = time.time()
            first = btree.Search(T, words[0])
            second = btree.Search(T, words[1])

            if first == None or second == None:
                embeddings.append(words)
            else:
                embeddings.append([first, second])
            
            totaltime = totaltime + (time.time() - start)
    # return the runtime of either BST or BTree operation and the embeddings list
    return totaltime, embeddings 

def treeType(T):
    if type(T) == bst.BST:
        return "binary search tree"
    if type(T) == btree.BTree:
        return "B-tree"

# get a file of words, create a new file, and write to
# the file having two words per line in the new file
def writeToSimilaritiesFile(filename):
    try:

        # open file to read words from
        # create new file to write to
        f = open(filename)
        new = open("similarities.txt", "w")

        word = 0
        for line in f:
            if "\n" in line:
                line = line[:-1]
            if word == 1:
                new.write(line + "\n")
                word = 0
            else:
                new.write(line + ",")
                word = word + 1

        f.close() # close the files to save memory
        new.close()
    except IOError:
        print("File", filename, "not found!\n") 

# part 3
def similarities(e1, e2):
	return np.dot(e1.emb, e2.emb)/(np.linalg.norm(e1.emb) * np.linalg.norm(e2.emb))

if __name__ == "__main__":

    # txt file from nlp.stanford.edu
    filename = "glove.6B.50d.txt"

    # check if similarities text file exists
    # if not - open a file containing English words and write to a new file
    # two words per row to be used to find similarities in part 3
    if not os.path.exists("similarities.txt"):
        writeToSimilaritiesFile("english-words.txt")

    # part 1
    while (True):
        c = 0
        try:
            while (c < 1 or c > 2):
                print("\nChoose table implementation\nType 1 for binary search tree or 2 B-Tree") # menu
                c = int(input("Choice: "))
        except ValueError:
            print("Invalid input! Provide an integer value.")
            break

        # build bst
        if c == 1:
            print("\nBuilding binary search tree\n")
            start = time.time()
            T = buildBST(filename)
            end = time.time()

            # stats 
            print("Binary Search Tree stats:\nNumber of Nodes: {}".format(bst.NumberOfNodes(T)))
            print("Height: {}".format(bst.Height(T)))
            print("Running time for {} construction: {}".format(treeType(T), end-start))

        # build b-tree
        if c == 2:
            max = int(input("Maximum number of items in node: "))
            print("\nBuilding B-tree\n")
            start = time.time()
            T = buildBTree(max, filename)
            end = time.time()

            print("B-tree stats:\nNumber of Nodes: {}".format(btree.NumberOfNodes(T)))
            print("Height: {}".format(btree.Height(T)))
            print("Running time for {} construction (with max_items = {}): {}".format(treeType(T), max, end-start))

        print("\nReading word file to determine similarities\n")

        totalTime, embeddings = getEmbeddings(T, "similarities.txt" )

        for element in embeddings:
            if any(isinstance(words, str) for words in element):
                print("No embedding for {} -or- {}".format(element[0], element[1]))
            else:
                print("Similarity [{},{}] = {}".format(element[0].word, element[1].word, similarities(element[0], element[1])))

        # final running time output message based on type of tree
        if type(T) == bst.BST:
            print("Running time for {} query processing: {}".format(treeType(T), totalTime))

        if type(T) == btree.BTree:
            print("Running time for {} query processing (with max_items = {}): {}".format(treeType(T), max, totalTime))

        break;



    