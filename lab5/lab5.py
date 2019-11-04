import time
from htc import HashTableChainLab5
from wordEmbedding import WordEmbedding
import os

# accepts function type as a parameter and builds hash table 
# using chaining based on function type provided
# return runtime, table
def buildHashTableChaining(filename, fType, limit = -1):
    try:
        totalTime = 0
        # file uses utf8 encoding
        f = open(filename, encoding="utf8")
        lineCount = 0

        HTC = HashTableChainLab5(40009)

        for line in f:
            tokens = line.split(" ")
            # store if value begins with alphabetic letter
            if tokens[0].isalpha():
                
                if fType == 1: # The length of the string % n
                    start = time.time()
                    HTC.insert1(WordEmbedding(tokens[0], tokens[1:]))
                    totalTime += time.time() - start
            
            lineCount += 1
            if lineCount == limit:
                return totalTime, HTC

        f.close() # close the file to save memory
        return totalTime, HTC
    except IOError:
        print("File", filename, "not found!\n")
    
# accepts function type as a parameter and builds hash table
# using linear probing based on function type provided
# return runtime, table
def buildHashTableLinearProbing(fType):
    try:
        return None, None
    except IOError:
        print("File", filename, "not found!\n")

def getEmbeddings(table, filename, fType):
    totaltime = 0
    f = open(filename, "r")
    embeddings = []

    for line in f:
        # first remove new line char from line
        if "\n" in line:
            line = line[:-1]
        # split by commas
        words = line.split(",")

        if fType == 1:
            start = time.time()
            first = table.find1(words[0])
            second = table.find1(words[1])

            if first == None or second == None:
                embeddings.append(words)
            else:
                embeddings.append([first, second])
                
            totaltime = totaltime + (time.time() - start)
    return totaltime, embeddings

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

# used in lab 4
def similarities(e1, e2):
	return np.dot(e1.emb, e2.emb)/(np.linalg.norm(e1.emb) * np.linalg.norm(e2.emb))

if __name__ == "__main__":

    # txt file from nlp.standford.edu
    filename = "glove.6B.50d.txt"

    # check if similarities text file exists
    # if not - open a file containing English words and write to a new file
    # two words per row to be used to find similarities in part 3
    if not os.path.exists("similarities.txt"):
        writeToSimilaritiesFile("english-words.txt")

    # variables
    choice = 0
    hashFuncType = 0
    hashFunctStrings = [
        "The length of the string % n", 
        "The ascii value (ord(c)) of the first character in the string % n", 
        "The product of the ascii values of the first and last characters in the string % n", 
        "The sum of the ascii values of the characters in the string % n", 
        "The recursive formulation h(”,n) = 1; h(S,n) = (ord(s[0]) + 255*h(s[1:],n))% n", 
        "Another function"]
    table = None

    try:
        # valid input: 1 or 2
        while choice < 1 or choice > 2:
            print("Choose table implementation\nType 1 for Hash Table Chaining or 2 Hash Table Probing")
            choice = int(input("Choice: "))

        # hash functions for lab 5
        # valid input: 1, 2, 3, 4, 5, 6
        while hashFuncType < 1 or hashFuncType > 6:
            print("Choose hash function:")
            for i in range(len(hashFunctStrings)):
                print("{}. {}".format(i+1, hashFunctStrings[i]))
            hashFuncType = int(input("Choice: "))

    except ValueError:
        print("Invalid input! Provide valid integer value.")

    # build table based on user input
    if choice == 1:
        runtime, table = buildHashTableChaining(filename, hashFuncType, 10000)

    print("\nReading word file to determine similarities\n")

    totalTime, embeddings = getEmbeddings(table, "similarities.txt", hashFuncType)

    for element in embeddings:
            if any(isinstance(words, str) for words in element):
                print("No embedding for {} -or- {}".format(element[0], element[1]))
            else:
                print("Similarity [{},{}] = {}".format(element[0].word, element[1].word, similarities(element[0], element[1])))

    print("{}\n{}".format(runtime, totalTime))
