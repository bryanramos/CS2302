# Adjacency list representation of graphs
import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.interpolate import interp1d

class Edge:
    def __init__(self, dest, weight=1):
        self.dest = dest
        self.weight = weight
        
class Graph:
    # Constructor
    def __init__(self, vertices, weighted=False, directed = False):
        self.al = [[] for i in range(vertices)]
        self.weighted = weighted
        self.directed = directed
        self.representation = 'AL'
        
    def insert_edge(self,source,dest,weight=1):
        if source >= len(self.al) or dest>=len(self.al) or source <0 or dest<0:
            print('Error, vertex number out of range')
        elif weight!=1 and not self.weighted:
            print('Error, inserting weighted edge to unweighted graph')
        else:
            self.al[source].append(Edge(dest,weight)) 
            if not self.directed:
                self.al[dest].append(Edge(source,weight))
    
    def delete_edge_(self,source,dest):
        i = 0
        for edge in self.al[source]:
            if edge.dest == dest:
                self.al[source].pop(i)
                return True
            i+=1    
        return False
    
    def delete_edge(self,source,dest):
        if source >= len(self.al) or dest>=len(self.al) or source <0 or dest<0:
            print('Error, vertex number out of range')
        else:
            deleted = self.delete_edge_(source,dest)
            if not self.directed:
                deleted = self.delete_edge_(dest,source)
        if not deleted:        
            print('Error, edge to delete not found')      
            
    def display(self):
        print('[',end='')
        for i in range(len(self.al)):
            print('[',end='')
            for edge in self.al[i]:
                print('('+str(edge.dest)+','+str(edge.weight)+')',end='')
            print(']',end=' ')    
        print(']')   
     
    def draw(self):
        scale = 30
        fig, ax = plt.subplots()
        for i in range(len(self.al)):
            for edge in self.al[i]:
                d,w = edge.dest, edge.weight
                if self.directed or d>i:
                    x = np.linspace(i*scale,d*scale)
                    x0 = np.linspace(i*scale,d*scale,num=5)
                    diff = np.abs(d-i)
                    if diff == 1:
                        y0 = [0,0,0,0,0]
                    else:
                        y0 = [0,-6*diff,-8*diff,-6*diff,0]
                    f = interp1d(x0, y0, kind='cubic')
                    y = f(x)
                    s = np.sign(i-d)
                    ax.plot(x,s*y,linewidth=1,color='k')
                    if self.directed:
                        xd = [x0[2]+2*s,x0[2],x0[2]+2*s]
                        yd = [y0[2]-1,y0[2],y0[2]+1]
                        yd = [y*s for y in yd]
                        ax.plot(xd,yd,linewidth=1,color='k')
                    if self.weighted:
                        xd = [x0[2]+2*s,x0[2],x0[2]+2*s]
                        yd = [y0[2]-1,y0[2],y0[2]+1]
                        yd = [y*s for y in yd]
                        ax.text(xd[2]-s*2,yd[2]+3*s, str(w), size=12,ha="center", va="center")
            ax.plot([i*scale,i*scale],[0,0],linewidth=1,color='k')        
            ax.text(i*scale,0, str(i), size=20,ha="center", va="center",
             bbox=dict(facecolor='w',boxstyle="circle"))
        ax.axis('off') 
        ax.set_aspect(1.0)
            
    def as_EL(self):
        # import edge list from graph_EL.py
        from graph_EL import Graph
        EL = Graph(len(self.al), self.weighted, self.directed)
        edges = [[] for i in range(len(self.al))]
        for i in range(len(self.al)):
            for edge in self.al[i]:
                if i not in edges[edge.dest]:
                    edges[edge.dest].append(i)
                    EL.insert_edge(i, edge.dest, edge.weight)
        return EL
    
    def as_AM(self):
        # import adjacency matrix from graph_AM.py
        from graph_AM import Graph
        AM = Graph(len(self.al), self.weighted, self.directed)
        for i in range(len(self.al)):
            for edge in self.al[i]:
                AM.insert_edge(i, edge.dest, edge.weight)
        return AM
    
    def as_AL(self):
        return self
    
    def depthFirst(self, start, end):
        stack = [self.al[start]]
        discoveredSet = [self.al[start]]
        # set the length of the path list
        path = [-1] * 16
        
        while stack:
            v = stack.pop()
            for e in v:
                if self.al[e.dest] not in discoveredSet:
                    stack.append(self.al[e.dest])
                    discoveredSet.append(self.al[e.dest])
                    path[e.dest] = self.al.index(v)
        return path

    def breadthFirst(self, start, end):
        queue = [self.al[start]]
        discoveredSet = [self.al[start]]
        # set the length of the path list
        path = [-1] * 16
        
        while queue:
            v = queue.pop(0)
            for e in v:
                if self.al[e.dest] not in discoveredSet:
                    queue.append(self.al[e.dest])
                    discoveredSet.append(self.al[e.dest])
                    path[e.dest] = self.al.index(v)
        return path
    
    def printP(self, path, dest):
        if path[dest] != -1:
            self.printP(path, path[dest])
            print(dest, end=' ')
        else:
            print(dest, end=' ')
            return -1
        
    def printDepthFirst(self, start, end):
        path = self.breadthFirst(start, end)
        self.printP(path, end)
        print()

    def printBreadthFirst(self, start, end):
        path = self.depthFirst(start, end)  
        self.printP(path, end)  
        print()        
                    