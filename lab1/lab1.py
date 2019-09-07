'''
    Course: CS2302 Data Structures Fall 2019
    Author: Bryan Ramos [88760110]
    Assignment: Lab 1 Recursion
    Instructor: Dr. Olac Fuentes
    TA: Anindita Nath 
    Last Modified: Sep 6 2019
    Purpose: Find the anagrams for a word provided by the user using recursion.
'''

import time as t

# ---------- PART 1 ----------

# Read in file
# parameter filename: The name of the file to read.
# returns: set of words from file
def readFile1(filename):
    # attempt to open the file
    try:
        file = open(filename, "r")
        # each word is saved as a value in the set
        setOfWords = set(file.read().split())
        return setOfWords
    # if file not found, catch file not found exception and output an error
    except IOError:
        print("Error: File", filename, "not found!")
        
def findAnagrams1(r_letters, originalWord, setOfWords, setOfAnagrams, s_letters = ""):
    # all the letters have been used in our base case
    if len(r_letters) == 0 and s_letters in setOfWords and originalWord != s_letters:
        setOfAnagrams.add(s_letters)
    # recursive case
    else: 
        for i in range(len(r_letters)):
            # move a letter from r_letters to scrambled letters, remove it from remaining letters
            scrambleLetter = r_letters[i]
            remainingLetters = r_letters[:i] + r_letters[i + 1:]
            scrambled = s_letters + scrambleLetter
            
            findAnagrams1(remainingLetters, originalWord, setOfWords, setOfAnagrams, scrambled)
        
# Display prompt for user
# parameter setOfWords: Set of the words from the file.
def prompt1(setOfWords):
    print("PART 1")
    # the prompt will instruct the user to do one of the following:
    # (1) enter a word, the anagrams for that word will be found, then the prompt is reshown
    # (2) enter an empty string and the program will terminate
    while (True):
        word = input("Enter a word or empty string to finish: ").lower()
        
        # if no word is provided: terminate the program
        if not word:
            print("Bye thanks for using the program!")
            break
        # else if: input provided is not a valid word or a number
        elif word not in setOfWords:
            print(word, "is not a valid word. Please enter a valid word.")
        # else: find the anagrams for that word
        else:
            # split a word into a list of its characters, organize them alphabetically
            splitWord = sorted(list(word))
            # take the ordered list of characters and join them into a string
            splitWord = "".join(splitWord)
            
            # init empty set to store the returned set of anagrams
            setOfAnagrams = set()
            
            start = t.time()
            findAnagrams1(splitWord, word, setOfWords, setOfAnagrams, "")
            end = t.time()
            
            print("The word", word, "has the following", len(setOfAnagrams), "anagrams:")
            # sort anagrams in alphabetical order
            setOfAnagrams = sorted(list(setOfAnagrams))
            # print each anagram
            for anagram in setOfAnagrams:
                print(anagram)
            print("It took", round(end-start, 6), "seconds to find the anagrams.\n")

# ---------- PART 2 ----------
     
# ----- FIRST OPTIMIZATION -----
            
# If the string has duplicate characters, only make recursive calls the first time the character\
# appears. This will avoid generating the same anagram multiple times.
def findAnagrams2_opt1(r_letters, originalWord, setOfWords, setOfAnagrams, s_letters = ""):
    # all the letters have been used in our base case
    if len(r_letters) == 0 and s_letters in setOfWords and originalWord != s_letters:
        setOfAnagrams.add(s_letters)
    # recursive case
    else: 
        lettersAlreadyUsed = set()
        for i in range(len(r_letters)):
            # move a letter from r_letters to scrambled letters, remove it from remaining letters
            scrambleLetter = r_letters[i]
            remainingLetters = r_letters[:i] + r_letters[i + 1:]
            
            if scrambleLetter in lettersAlreadyUsed:
                continue
            lettersAlreadyUsed.add(scrambleLetter)
            scrambled = s_letters + scrambleLetter
            
            findAnagrams2_opt1(remainingLetters, originalWord, setOfWords, setOfAnagrams, scrambled)
            
# Display prompt for user
# parameter setOfWords: Set of the words from the file.
def prompt2_forOpt1(setOfWords):
    print("\nPART 2 - FIRST OPTIMIZATION")
    
    # the prompt will instruct the user to do one of the following:
    # (1) enter a word, the anagrams for that word will be found, then the prompt is reshown
    # (2) enter an empty string and the program will terminate
    while (True):
        word = input("Enter a word or empty string to finish: ").lower()
        
        # if no word is provided: terminate the program
        if not word:
            print("Bye thanks for using the program!")
            break
        # else if: input provided is not a valid word or a number
        elif word not in setOfWords:
            print(word, "is not a valid word. Please enter a valid word.")
        # else: find the anagrams for that word
        else:
            # split a word into a list of its characters, organize them alphabetically
            splitWord = sorted(list(word))
            # take the ordered list of characters and join them into a string
            splitWord = "".join(splitWord)
            
            # init empty set to store the returned set of anagrams
            setOfAnagrams = set()
            
            start = t.time()
            findAnagrams2_opt1(splitWord, word, setOfWords, setOfAnagrams, "")
            end = t.time()
            
            print("The word", word, "has the following", len(setOfAnagrams), "anagrams:")
            # sort anagrams in alphabetical order
            setOfAnagrams = sorted(list(setOfAnagrams))
            # print each anagram
            for anagram in setOfAnagrams:
                print(anagram)
            print("It took", round(end-start, 6), "seconds to find the anagrams.\n")
          
# ----- SECOND (BOTH) OPTIMIZATIONS -----
     
 # Read in file
# parameter filename: The name of the file to read.
# returns: set of words from file and the set of prefixes
def readFile2(filename):
    # attempt to open the file
    try:
        file = open(filename, "r")
        # set will contain the prefixes of all the words in the word set
        setOfPrefixes = set()
        # each word is saved as a value in the set
        setOfWords = set(file.read().split())
        for word in setOfWords:
            # i.e. word set is {’data’, ’science’}, your prefix set should 
            # be {”, ’d’, ’da’, ’dat’, ’s’, ’sc’, ’sci’, ’scie’, ’scien’, 
            # ’scienc’}
            for i in range(len(word)):
                setOfPrefixes.add(word[:i])
        return setOfWords, setOfPrefixes
    
    # if file not found, catch file not found exception and output an error
    except IOError:
        print("Error: File", filename, "not found!")
        
# If the string has duplicate characters, only make recursive calls the first time the character\
# appears. This will avoid generating the same anagram multiple times.
# Stop recursion if the partial word you have is not a prefix of any word in the word set.
def findAnagrams2_opt2(r_letters, originalWord, setOfWords, setOfPrefixes, setOfAnagrams, s_letters = ""):
    # all the letters have been used in our base case
    if len(r_letters) == 0 and s_letters in setOfWords and originalWord != s_letters:
        setOfAnagrams.add(s_letters)
    # recursive case
    else: 
        lettersAlreadyUsed = set()
        for i in range(len(r_letters)):
            # move a letter from r_letters to scrambled letters, remove it from remaining letters
            scrambleLetter = r_letters[i]
            remainingLetters = r_letters[:i] + r_letters[i + 1:]
            
            if (len(remainingLetters) != 0) and not ((s_letters + scrambleLetter) in setOfPrefixes):
                continue
            if scrambleLetter in lettersAlreadyUsed:
                continue
            
            lettersAlreadyUsed.add(scrambleLetter)
            scrambled = s_letters + scrambleLetter
            
            findAnagrams2_opt2(remainingLetters, originalWord, setOfWords, setOfPrefixes, setOfAnagrams, scrambled)

# Display prompt for user
# parameter setOfWords: Set of the words from the file.
# parameter setOfPrefixes: Set of prefixes 
def prompt2_forOpt2(setOfWords, setOfPrefixes):
    print("\nPART 2 - SECOND (BOTH) OPTIMIZATIONS")
    
    # the prompt will instruct the user to do one of the following:
    # (1) enter a word, the anagrams for that word will be found, then the prompt is reshown
    # (2) enter an empty string and the program will terminate
    while (True):
        word = input("Enter a word or empty string to finish: ").lower()
        
        # if no word is provided: terminate the program
        if not word:
            print("Bye thanks for using the program!")
            break
         # else if: input provided is not a valid word or a number
        elif word not in setOfWords:
            print(word, "is not a valid word. Please enter a valid word.")
        # else: find the anagrams for that word
        else:
            # split a word into a list of its characters, organize them alphabetically
            splitWord = sorted(list(word))
            # take the ordered list of characters and join them into a string
            splitWord = "".join(splitWord)
            
            # init empty set to store the returned set of anagrams
            setOfAnagrams = set()
            
            start = t.time()
            findAnagrams2_opt2(splitWord, word, setOfWords, setOfPrefixes, setOfAnagrams, "")
            end = t.time()
            
            print("The word", word, "has the following", len(setOfAnagrams), "anagrams:")
            # sort anagrams in alphabetical order
            setOfAnagrams = sorted(list(setOfAnagrams))
            # print each anagram
            for anagram in setOfAnagrams:
                print(anagram)
            print("It took", round(end-start, 6), "seconds to find the anagrams.\n")
            
if __name__ == '__main__':
    # Part 1 of the lab assignment
    setOfWords = readFile1("words_alpha.txt")
    prompt1(setOfWords)
    
    # Part 2 of the lab assignment with first optimization
    prompt2_forOpt1(setOfWords)
    
    # Part 2 of the lab assignment with second (both) optimizations
    setOfWords, setOfPrefixes = readFile2("words_alpha.txt")                      
    prompt2_forOpt2(setOfWords, setOfPrefixes)
    