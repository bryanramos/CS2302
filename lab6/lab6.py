'''
Course: CS2302 Data Structures Fall 2019
Author: Bryan Ramos [88760110]
Assignment: Lab 6
Instructor: Dr. Olac Fuentes
TA: Anindita Nath 
Last Modified: November 18th 2019
Purpose: Implement Adjacency List, Adjacency Matrix and Edge List graph
representations.
'''

import graph_AL as graphAL
import graph_AM as graphAM
import graph_EL as graphEL

# build three graph representation:
# - adjacency list
# - adjacency matrix
# - edge list
def buildGraphRepresentations():
    # vars
    v = 16
    weighted = False
    directed = False
    
    # build adjacency list
    AL = graphAL.Graph(v, weighted, directed)
    AL.insert_edge(0, 5)
    AL.insert_edge(2, 11)
    AL.insert_edge(2, 7)
    AL.insert_edge(4, 5)
    AL.insert_edge(4, 7)
    AL.insert_edge(4, 13)
    AL.insert_edge(8, 11)
    AL.insert_edge(8, 13)
    AL.insert_edge(10, 11)
    AL.insert_edge(10, 15)
    
    # build adjacency matrix, build edge list
    AM = AL.as_AM()
    EL = AL.as_EL()
    
    # return all three representations
    return AL, AM, EL

# for lab report
def graphs(AL, AM, EL):
    AL.draw()
    AM.draw()
    EL.draw()
    
if __name__ == "__main__":
    
    AL, AM, EL = buildGraphRepresentations()
    
    # adjacency list
    # depth first
    print("Adjancency List Depth First:")
    print(AL.depthFirst(0, 15))
    AL.printDepthFirst(0, 15)
    # breadth first
    print("Adjacency List Breadth First:")
    print(AL.breadthFirst(0, 15))
    AL.printBreadthFirst(0, 15)
    
    print()
    print()
    
    # adjancency matrix
    # depth first
    print("Adjancency Matrix Depth First:")
    print(AM.depthFirst(0, 15))
    AM.printDepthFirst(0, 15)
    # breadth first
    print("Adjacency Matrix Breadth First:")
    print(AM.breadthFirst(0, 15))
    AM.printBreadthFirst(0, 15)
    
    print()
    print()
    
    # edge list
    # depth first
    print("Edge List Depth First:")
    print(EL.depthFirst(0, 15))
    EL.printDepthFirst(0, 15)
    # breadth first
    print("Edge List Breadth First:")
    print(EL.breadthFirst(0, 15))
    AM.printBreadthFirst(0, 15)
    
    print()
    print()
    
    # for lab report
    graphs(AL, AM, EL)
    
        

