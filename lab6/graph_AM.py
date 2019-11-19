# Adjacency matrix representation of graphs
import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.interpolate import interp1d

class Graph:
    # Constructor
    def __init__(self, vertices, weighted=False, directed = False):
        self.am = np.zeros((vertices,vertices),dtype=int) - 1
        self.weighted = weighted
        self.directed = directed
        self.representation = 'AM'
        
    def insert_edge(self,source,dest,weight=1):
        if weight!=1 and not self.weighted:
            print('Error, inserting weighted edge to unweighted graph')
        else:
            self.am[source][dest] = weight
            if not self.directed:
                self.am[dest][source] = weight
        
    def delete_edge(self,source,dest):
        self.am[source][dest] = -1
        if not self.directed:
            self.am[dest][source] = -1
                
    def display(self):
        print(self.am)
     
    def draw(self):
        self.as_AL().draw() 
    
    def as_EL(self):
        from graph_EL import Graph
        EL = Graph(len(self.am),self.weighted,self.directed)
        for i in range(len(self.am)):
            for j in range(len(self.am)):
                if not self.directed and j == i: #only insert one instance of every edge design choice for EL
                    if self.am[i][j] != -1:
                        EL.insert_edge(i, j, self.am[i][j])
        return EL

    def as_AM(self):
        return self
    
    def as_AL(self):
        from graph_AL import Graph
        AL = Graph(len(self.am), self.weighted, self.directed)
        for i in range(len(self.am)):
            for j in range(len(self.am[i])):
                if not self.directed and i == j:
                    break
                if self.am[i][j] != -1:
                    AL.insert_edge(i, j, self.am[i][j])
        return AL


    def depthFirst(self,start,end):
        stack = [start]
        discoveredSet = [start]
        # set the length of the path list
        path = [-1] * 16
        
        while stack:
            v = stack.pop()
            for i in range(len(self.am[v])):
                if self.am[v][i] != -1 and i not in discoveredSet:
                    stack.append(i)
                    discoveredSet.append(i)
                    path[i] = v
        return path 
    
    def breadthFirst(self, start, end):
        queue = [start]
        discoveredSet = [start]
        # set the length of the path list
        path = [-1] * 16
        
        while queue:
            v = queue.pop(0)
            for i in range(len(self.am[v])):
                if self.am[v][i] != -1 and i not in discoveredSet:
                    queue.append(i)
                    discoveredSet.append(i)
                    path[i] = v
        return path
        
    def printP(self, path, dest):
        if path[dest] != -1:
            self.printP(path, path[dest])
            print(dest, end = " ")
        else:
            print(dest, end = " ")
            return -1

    def printBreadthFirst(self, start, end):
        path = self.breadthFirst(start, end)
        self.printP(path, end)
        print()

    def printDepthFirst(self, start, end):
        path = self.depthFirst(start, end)
        self.printP(path, end)
        print()   
        
