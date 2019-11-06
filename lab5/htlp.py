from wordEmbedding import WordEmbedding
import numpy as np

class HashTableLP(object):
    def __init__(self,size):  
        self.item = np.zeros(size,dtype=WordEmbedding)-1

    # The length of the string % n
    def insert1(self, k):
        for e in range(len(self.item)):
            p = self.h(len(k.word) + e)
            if self.item[p] < 0:
                self.item[p] = k
                return p
        return -1
    def find1(self, k):
        for e in range(len(self.item)):
            p = self.h(len(k) + e)
            if self.item[p] == k:
                return self.item[p]
            if self.item[p] == -1:
                return None
        return None
    
    # The ascii value (ord(c)) of the first character in the string % n
    def insert2(self, k):
        for e in range(len(self.item)):
            p = self.h(ord(k.word[0]) + e)
            if self.item[p] < 0:
                self.item[p] = k
                return p
        return -1
    def find2(self, k):
        for e in range(len(self.item)):
            p = self.h(ord(k[0]) + e)
            if self.item[p] == k:
                self.item[p]
            if self.item[p] == -1:
                return None
        return None

    # The product of the ascii values of the first and last characters in the string % n
    def insert3(self, k):
        for e in range(len(self.item)):
            p = self.h((ord(k.word[0]) * ord(k.word[-1])) + e)
            if self.item[p] < 0:
                self.item[p] = k
                return p
        return -1
    def find3(self, k):
        for e in range(len(self.item)):
            p = self.h((ord(k[0]) * ord(k[-1])) + e)
            if self.item[p] == k:
                return self.item[p]
            if self.item[p] == -1:
                return None
        return None
    
    # The sum of the ascii values of the characters in the string % n
    def insert4(self, k):
        s = 0
        for e in k.word:
            s += ord(e)
        for i in range(len(self.item)):
            p = self.h(s + i)
            if self.item[p] < 0:
                self.item[p] = k
                return p
        return -1
    def find4(self, k):
        s = 0
        for e in k:
            s += ord(e)
        for i in range(len(self.item)):
            p = self.h(s + i)
            if self.item[p] == k:
                return self.item[p]
            if self.item[p] == -1:
                return None
        return None

    def h2(self, s, n):
        if len(s) == 0:
            return 1
        else:
            return (ord(s[0]) + 255 * self.h2(s[1:],n)) % n

    # The recursive formulation h(”,n) = 1; h(S,n) = (ord(s[0]) + 255*h(s[1:],n))% n
    def insert5(self, k):
        for e in range(len(self.item)):
            p = self.h2(k.word, len(self.item)) + e
            if self.item[p] < 0:
                self.item[p] = k
                return p
        return -1
    def find5(self, k):
        for e in range(len(self.item)):
            p = self.h2(k, len(self.item)) + e
            if self.item[p] == k:
                return self.item[p]
            if self.item[p] == -1:
                return None
        return None

    # (The length of the string // 2) % n
    def insert6(self, k):
        for e in range(len(self.item)):
            p = self.h((len(k.word)//2) + e)
            if self.item[p] < 0:
                self.item[p] = k
                return p
        return -1
    def find6(self, k):
        for e in range(len(self.item)):
            p = self.h((len(k)//2) + e)
            if self.item[p] == k:
                return self.item[p]
            if self.item[p] == -1:
                return None
        return None
     
    def delete(self,k):
        # Deletes k from table. It returns the position where k was, or -1 if k was not in the table
        # Sets table item where k was to -2 (which means deleted)
        f = self.find(k)
        if f >=0:
            self.item[f] = -2
        return f
    
    def h(self,k):
        return k%len(self.item)  
            
    def print_table(self):
        print('Table contents:')
        print(self.item)
