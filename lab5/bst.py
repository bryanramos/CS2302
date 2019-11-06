# Code to implement a binary search tree 
# Programmed by Olac Fuentes
# Last modified October 3, 2019

import matplotlib.pyplot as plt
import numpy as np
from wordEmbedding import WordEmbedding

class BST(object):
    # Constructor
    def __init__(self, word=None, embedding=None, left=None, right=None):  
        if word is not None and embedding is not None:
            self.data = WordEmbedding(word, embedding)
        else:
            self.data = None
        self.left = left 
        self.right = right      
        
def Insert(T, word, embedding):
    if T == None:
        T = BST(word, embedding)
    elif word <= T.data.word:
        T.left = Insert(T.left,word,embedding)
    else:
        T.right = Insert(T.right,word,embedding)
    return T

# for lab 4
def NumberOfNodes(T):
    if T is None:
        return 0
    else:
        return 1 + NumberOfNodes(T.left) + NumberOfNodes(T.right)
# for lab 4
def Height(T):
    if T is None:
        return -1
    lh = Height(T.left)
    rh = Height(T.right)
    return 1 + max(lh, rh)
# for lab 4
def Search(T, word):
    if T is None:
        return None    
    elif T.data.word == word:
        return T.data
    elif word < T.data.word:
        return Search(T.left, word)
    else:
        return Search(T.right, word)
def ShowBST(T,ind):
    # Display rotated BST in text form
    if T is not None:
        ShowBST(T.right,ind+'   ')
        print(ind, T.data)
        ShowBST(T.left,ind+'   ')

def DrawBST_(T, x0, x1, y, y_inc,ax):
    if T is not None:
        xm = (x0+x1)/2
        yn = y-y_inc
        if T.left is not None:
            p=np.array([[xm,y], [(x0+xm)/2,yn]])
            ax.plot(p[:,0],p[:,1],linewidth=1,color='k')
            DrawBST_(T.left,x0,xm,yn, y_inc,ax)
        if T.right is not None:
            p=np.array([[xm,y], [(x1+xm)/2,yn]])
            ax.plot(p[:,0],p[:,1],linewidth=1,color='k')
            DrawBST_(T.right,xm,x1,yn, y_inc,ax)
        ax.plot([xm,xm],[y,y],linewidth=1,color='k')
        ax.text(xm,y, str(T.data), size=10,ha="center", va="center",
            bbox=dict(facecolor='w',boxstyle="circle"))

def DrawBST(T): 
    #
    fig, ax = plt.subplots()
    DrawBST_(T, 0, 200, 400, 20, ax)
    ax.set_aspect(1.0)
    ax.axis('off') 
    plt.show() 


   
    