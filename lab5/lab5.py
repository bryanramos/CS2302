
'''
Course: CS2302 Data Structures Fall 2019
Author: Bryan Ramos [88760110]
Assignment: Lab 5
Instructor: Dr. Olac Fuentes
TA: Anindita Nath 
Last Modified: November 5th 2019
Purpose: Model the use of hash tables with chaining and hash tables
with linear probing to store Word Embedding objects using different
hash functions and analyze their running times to compare them to
that of trees.
'''

import os
import numpy as np
from htc import HashTableChainLab5
from htlp import HashTableLP
import time
from wordEmbedding import WordEmbedding

# build hash table of Word Embedding objects using chaining
# parameters: name of file, hash function to build table, maximum 
# amount of lines to deal with high amount of building time
def buildHashTableChaining(file_name, hashFunction, max):
    # catch file not found exception
    try:
        # file utilizes utf8 encoding
        f = open(file_name, "r", encoding="utf8")
        totaltime = 0

        H = HashTableChainLab5(400009)

        lines = 0 # compare to max amount of lines limit
        for line in f:
            tokens = line.split(" ")
            # store if value begins with alphabetic letter (A-Z, lowercase or uppercase)
            if tokens[0].isalpha():

                # The length of the string % n
                if hashFunction == 1:
                    start = time.time()
                    H.insert1(WordEmbedding(tokens[0], tokens[1:]))
                    end = time.time()
                    totaltime += end - start
                
                # The ascii value (ord(c)) of the first character in the string % n
                if hashFunction == 2:
                    start = time.time()
                    H.insert2(WordEmbedding(tokens[0], tokens[1:]))
                    end = time.time()
                    totaltime += end - start

                # The product of the ascii values of the first and last characters in the string % n
                if hashFunction == 3:
                    start = time.time()
                    H.insert3(WordEmbedding(tokens[0], tokens[1:]))
                    end = time.time()
                    totaltime += end - start

                # The sum of the ascii values of the characters in the string % n
                if hashFunction == 4:
                    start = time.time()
                    H.insert4(WordEmbedding(tokens[0], tokens[1:]))
                    end = time.time()
                    totaltime += end - start
                
                # The recursive formulation h(”,n) = 1; h(S,n) = (ord(s[0]) + 255*h(s[1:],n))% n
                if hashFunction == 5:
                    start = time.time()
                    H.insert5(WordEmbedding(tokens[0], tokens[1:]))
                    end = time.time()
                    totaltime += end - start

                # (The length of the string // 2) % n
                if hashFunction == 6:
                    start = time.time()
                    H.insert6(WordEmbedding(tokens[0], tokens[1:]))
                    end = time.time()
                    totaltime += end - start
            
            lines = lines + 1

            # if the current line matches the maximum amount of lines alloted
            if lines == max:
                return totaltime, H

        f.close() # close glove file to save memory
        return totaltime, H
    except IOError:
        print("File {} was not found!".format(file_name))

# build hash table of Word Embedding objects using probing
# parameters: name of file, hash function to build table, maximum 
# amount of lines to deal with high amount of building time
def buildHashTableProbing(file_name, hashFunction, max):
    # catch file not found exception
    try:
        # file utilizes utf8 encoding
        f = open(file_name, "r", encoding="utf8")
        totaltime = 0

        HTLP = HashTableLP(400009)

        lines = 0 # compare to max amount of lines limit
        for line in f:
            tokens = line.split(" ")
            # store if value begins with alphabetic letter (A-Z, lowercase or uppercase)
            if tokens[0].isalpha():

                # The length of the string % n
                if hashFunction == 1:
                    start = time.time()
                    HTLP.insert1(WordEmbedding(tokens[0], tokens[1:]))
                    end = time.time()
                    totaltime += end - start

                # The ascii value (ord(c)) of the first character in the string % n
                if hashFunction == 2:
                    start = time.time()
                    HTLP.insert2(WordEmbedding(tokens[0], tokens[1:]))
                    end = time.time()
                    totaltime += end - start

                # The product of the ascii values of the first and last characters in the string % n
                if hashFunction == 3:
                    start = time.time()
                    HTLP.insert3(WordEmbedding(tokens[0], tokens[1:]))
                    end = time.time()
                    totaltime += end - start

                # The sum of the ascii values of the characters in the string % n
                if hashFunction == 4:
                    start = time.time()
                    HTLP.insert4(WordEmbedding(tokens[0], tokens[1:]))
                    end = time.time()
                    totaltime += end - start

                # The recursive formulation h(”,n) = 1; h(S,n) = (ord(s[0]) + 255*h(s[1:],n))% n
                if hashFunction == 5:
                    start = time.time()
                    HTLP.insert5(WordEmbedding(tokens[0], tokens[1:]))
                    end = time.time()
                    totaltime += end - start

                # (The length of the string // 2) % n
                if hashFunction == 6:
                    start = time.time()
                    HTLP.insert6(WordEmbedding(tokens[0], tokens[1:]))
                    end = time.time()
                    totaltime += end - start

            lines = lines + 1

            # if the current line matches the maximum amount of lines alloted
            if lines == max:
                return totaltime, HTLP
        
        f.close() # close glove file to save memory
        return totaltime, HTLP

    except IOError:
        print("File {} was not found!".format(file_name))

# build spreadsheet data for lab report
def calculateRuntimes():
    f = open("runtimes.csv", "w")

    for r in range(1, 7):
        runtime, H = buildHashTableChaining("glove.6B.50d.txt", int(r), 10000)
        totalTime, embeddingsList = embeddings(H, "similarities.txt", int(r))
        f.write("Hash Function " + str(r) + "," + str(runtime) + "," + str(totalTime) + "\n") 
    
    for r in range(1, 7):
        runtime, H = buildHashTableProbing("glove.6B.50d.txt", int(r), 10000)
        totalTime, embeddingsList = embeddings(H, "similarities.txt", int(r))
        f.write("Hash Function " + str(r) + "," + str(runtime) + "," + str(totalTime) + "\n") 

    f.close() # close file to save memory

# retrieve embeddings from the similarities file
def embeddings(H, file_name, hashFunction):
    # catch file not found exception - in main, there is a condition that guarantees 
    # similarities file will be found - but nonetheless, an exception is provided 
    try:
        f = open(file_name)
        totaltime = 0
        embeddings = []

        for line in f:
            # 1st remove remove new line character from line
            if "\n" in line:
                line = line[:-1]
            # split by comma tokenize into list
            words = line.split(",")

            # The length of the string % n
            if hashFunction == 1:
                start = time.time() 
                firstWord = H.find1(words[0])
                secondWord = H.find1(words[1])

                if firstWord == None or secondWord == None:
                    embeddings.append(words)
                else:
                    embeddings.append([firstWord, secondWord])
                totaltime = totaltime + (time.time() - start)

            # The ascii value (ord(c)) of the first character in the string % n
            if hashFunction == 2:
                start = time.time() 
                firstWord = H.find2(words[0])
                secondWord = H.find2(words[1])

                if firstWord == None or secondWord == None:
                    embeddings.append(words)
                else:
                    embeddings.append([firstWord, secondWord])
                totaltime = totaltime + (time.time() - start)

            # The product of the ascii values of the first and last characters in the string % n
            if hashFunction == 3:
                start = time.time() 
                firstWord = H.find3(words[0])
                secondWord = H.find3(words[1])

                if firstWord == None or secondWord == None:
                    embeddings.append(words)
                else:
                    embeddings.append([firstWord, secondWord])
                totaltime = totaltime + (time.time() - start)

            # The sum of the ascii values of the characters in the string % n
            if hashFunction == 4:
                start = time.time() 
                firstWord = H.find4(words[0])
                secondWord = H.find4(words[1])

                if firstWord == None or secondWord == None:
                    embeddings.append(words)
                else:
                    embeddings.append([firstWord, secondWord])
                totaltime = totaltime + (time.time() - start)
            
            # The recursive formulation h(”,n) = 1; h(S,n) = (ord(s[0]) + 255*h(s[1:],n))% n
            if hashFunction == 5:
                start = time.time() 
                firstWord = H.find5(words[0])
                secondWord = H.find5(words[1])

                if firstWord == None or secondWord == None:
                    embeddings.append(words)
                else:
                    embeddings.append([firstWord, secondWord])
                totaltime = totaltime + (time.time() - start)

            # (The length of the string // 2) % n
            if hashFunction == 6:
                start = time.time() 
                firstWord = H.find6(words[0])
                secondWord = H.find6(words[1])

                if firstWord == None or secondWord == None:
                    embeddings.append(words)
                else:
                    embeddings.append([firstWord, secondWord])
                totaltime = totaltime + (time.time() - start)
        
        f.close()
        return totaltime, embeddings

    except IOError: 
        print("File {} was not found!".format(file_name))

# used in lab 4
def similarities(e1, e2):
	return np.dot(e1.emb, e2.emb)/(np.linalg.norm(e1.emb) * np.linalg.norm(e2.emb))

def hashTableType(H):
    import htc
    import htlp
    if type(H) == htc.HashTableChainLab5:
        return "Hash Table Chaining"
    if type(H) == htlp.HashTableLP:
        return "Hash Table Probing"

# get a file of words, create a new file, and write to
# the file having two words per line in the new file
def writeToSimilaritiesFile(file_name):
    try:

        # open file to read words from
        # create new file to write to
        f = open(file_name)
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
        print("File", file_name, "not found!\n") 

# main method
if __name__ == "__main__":

    # calculateRuntimes()

    # txt file from nlp.stanford.edu
    file_name = "glove.6B.50d.txt"

    # check if similarities text file exists
    # if not - open a file containing English words and write to a new file
    # two words per row to be used to find similarities in part 3
    if not os.path.exists("similarities.txt"):
        writeToSimilaritiesFile("english-words.txt")

    # vars
    choice = 0
    hashFunction = 0
    hashFunctions = [
        "The length of the string % n",
        "The ascii value (ord(c)) of the first character in the string % n",
        "The product of the ascii values of the first and last characters in the string % n",
        "The sum of the ascii values of the characters in the string % n",
        "The recursive formulation h(”,n) = 1; h(S,n) = (ord(s[0]) + 255*h(s[1:],n))% n",
        "Another function of your choice"]
    H = None # hash table initially null

    # catch non-integer input from user
    try:
        # valid input for choice: 1 (Hash Table Chaining) or 2 (Hash Table Probing)
        while choice < 1 or choice > 2:
            print("Choose hash table implementation:\nType 1 for Hash Table Chaining or 2 Hash Table Probing")
            choice = int(input("Choice: "))
        
        # hash functions from lab instructions
        # valid input for functions: 1, 2, 3, 4, 5, 6
        while hashFunction < 1 or hashFunction > 6:
            print("Choose hash function:")
            # print each of the strings for the types of hash functions options
            for i in range(len(hashFunctions)):
                print("{}. {}".format(i + 1, hashFunctions[i]))
            hashFunction = int(input("Hash function choice: "))

    except ValueError:
        print("Invalid input! Provide an integer value.")

    # build hash table
    # hash table chaining
    if choice == 1:
        print("\nBuilding Hash Table Chaining\n")
        runtime, H = buildHashTableChaining(file_name, hashFunction, 10000)
    # hash table probing
    else:
        print("\nBuilding Hash Table Probing\n")
        runtime, H = buildHashTableProbing(file_name, hashFunction, 10000)

    file_name2 = "similarities.txt"
    print("\nReading word file to determine similarities\n")

    totalTime, embeddings = embeddings(H, file_name2, hashFunction)

    for element in embeddings:
        if any(isinstance(words, str) for words in element):
            print("No embedding for {} or {}".format(element[0], element[1]))
        else:
            print("Similarity [{},{}] = {}".format(element[0].word, element[1].word, similarities(element[0], element[1])))
    
    print("Running time for {} construction: {}".format(hashTableType(H), runtime))
    print("Running time for {} searching: {}".format(hashTableType(H), totalTime))