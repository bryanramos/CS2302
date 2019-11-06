from wordEmbedding import WordEmbedding

# hash table chain for words - lab 5
class HashTableChainLab5(object):
    def __init__(self, size):
        self.bucket = [[] for i in range(size)]
    
    def h(self, k):
        return k % len(self.bucket)

    # The length of the string % n
    def insert1(self, k):
        b = self.h(len(k.word))
        if not k in self.bucket[b]:
            self.bucket[b].append(k) 
    def find1(self, k):
        b = self.h(len(k))
        try:
            for i in self.bucket[b]:
                if i == k:
                    return i
        except:
            return None

    # The ascii value (ord(c)) of the first character in the string % n
    def insert2(self, k):
        b = self.h(ord(k.word[0]))
        if not k in self.bucket[b]:
            self.bucket[b].append(k)
    def find2(self, k):
        b = self.h(ord(k[0]))
        try:
            for i in self.bucket[b]:
                if i == k:
                    return i
        except:
            return None

    # The product of the ascii values of the first and last characters in the string % n
    def insert3(self, k):
        b = self.h(ord(k.word[0]) * ord(k.word[-1]))
        if not k in self.bucket[b]:
            self.bucket[b].append(k)
    def find3(self, k):
        b = self.h(ord(k[0]) * ord(k[-1]))
        try:
            for i in self.bucket[b]:
                if i == k:
                    return i
        except:
            return None

    # The sum of the ascii values of the characters in the string % n
    def insert4(self, k):
        s = 0
        for e in k.word:
            s += ord(e)
        b = self.h(s)
        if not k in self.bucket[b]:
            self.bucket[b].append(k)
    def find4(self, k):
        s = 0
        for e in k:
            s += ord(e)
        b = self.h(s)
        try:
            for i in self.bucket[b]:
                if i == k:
                    return i
        except:
            return None

    def h2(self, s, n):
        if len(s) == 0:
            return 1
        else:
            return (ord(s[0]) + 255 * self.h2(s[1:], n)) % n
    
    # The recursive formulation h(”,n) = 1; h(S,n) = (ord(s[0]) + 255*h(s[1:],n))% n
    def insert5(self, k):
        b = self.h2(k.word, len(self.bucket))
        if not k in self.bucket[b]:
            self.bucket[b].append(k)
    def find5(self, k):
        b = self.h2(k, len(self.bucket))
        try:
            for i in self.bucket[b]:
                if i == k:
                    return i
        except:
            return None

    # (The length of the string // 2) % n
    def insert6(self, k):
        b = self.h(len(k.word) // 2)
        if not k in self.bucket[b]:
            self.bucket[b].append(k) 

    def find6(self, k):
        b = self.h(len(k) // 2)
        try:
            for i in self.bucket[b]:
                if i == k:
                    return i
        except:
            return None
    
# Implementation of hash tables with chaining
# Programmed by Olac Fuentes
# Last modified October 9, 2019

class HashTableChain(object):
    # Builds a hash table of size 'size'
    # Item is a list of (initially empty) lists
    # Constructor
    def __init__(self,size):  
        self.bucket = [[] for i in range(size)]
        
    def h(self,k):
        return k%len(self.bucket)    
            
    def insert(self,k):
        # Inserts k in appropriate bucket (list) 
        # Does nothing if k is already in the table
        b = self.h(k)
        if not k in self.bucket[b]:
            self.bucket[b].append(k)         #Insert new item at the end
            
    def find(self,k):
        # Returns bucket (b) and index (i) 
        # If k is not in table, i == -1
        b = self.h(k)
        try:
            i = self.bucket[b].index(k)
        except:
            i = -1
        return b, i
     
    def print_table(self):
        print('Table contents:')
        for b in self.bucket:
            print(b)
    
    def delete(self,k):
        # Returns k from appropriate list
        # Does nothing if k is not in the table
        # Returns 1 in case of a successful deletion, -1 otherwise
        b = self.h(k)
        try:
            self.bucket[b].remove(k)
            return 1
        except:
            return -1
