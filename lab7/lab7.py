# imports
import graph_AL as graph
import numpy as np
from cc import connected_components
import time

# using my code from the quiz for in degree of vertex v
def in_degree(g, v):
    d = 0
    for vert in range(len(g.al)):
        for edge in g.al[vert]:
            if edge.dest == v:
                d += 1
    return d

def randomizedHamiltonian(G, trials = 1000):
    edgeList = G.as_EL()
    
    for t in range(trials):
        # inherit attributes from G
        g = graph.Graph(len(G.al), weighted=G.weighted, directed=G.directed)
        
        # convert to edge list
        g = g.as_EL()
        
        edges = edgeList.el[:] # reference to copy of the list
        for vertex in range(g.vertices):
            g.el.append(edges.pop(np.random.randint(len(edges))))
            
        # convert back to adjacency list
        g = g.as_AL()
        # check for connected components
        c, s = connected_components(g)
        
        # if graph has one connected component and the in-degree of every vertex in g is 2, 
        # forms hamiltonian cycle
        
        # if graph has one connected component
        if c == 1:
            check_degree2 = True
            # check if the in-degree of every vertex in g is 2
            for v in range(len(g.al)):
                indegree = in_degree(g, v)
                # if the in_degree of just one vertex is not 2, then it is not a hamiltonian cycle
                # because every vertex in g must have an in degree of 2
                if indegree != 2:
                    check_degree2 = False
                
            # if there is a hamiltonian cycle return g
            if check_degree2:
                return g
    
    # no hamiltonian cycle was found             
    return None

def printCycleInfo(cycle, g):
    if cycle is not None:
        print("Solution exists: Hamiltonian Cycle Found")
        g.draw()
    else:
        g.draw()
        print("Could not find hamiltonian cycle!")
        
# check if every vertex has in degree 2
# parameters: list, edge list
def backtracking(g1, g2):
    # out of edges = stop 
    if len(g2.el) == g2.vertices:
        adjacencyList = g2.as_AL()
        c, s = connected_components(adjacencyList)
        if c == 1:
            for i in range(len(adjacencyList.al)):
                # if the in_degree of just one vertex is not 2, then it is not a hamiltonian cycle
                # because every vertex in g must have an in degree of 2
                if in_degree(adjacencyList, i) != 2:
                    return None
            return adjacencyList
        return None
    if len(g1) == 0:
        return None
    else:
        next = g1[0]
        g2.el = g2.el + [next]
        answer = backtracking(g1[1:], g2)
        if answer is not None:
            return answer
        g2.el.remove(next)
        answer = backtracking(g1[1:], g2)
        return answer
        
# backtracking algorithm
def backtrackingHamiltonian(G):
    # turn graph into edge list
    edgeList = G.as_EL()
    
    for e in edgeList.el:
        print(e.source, e.dest, e.weight)
        
    g = graph.Graph(len(G.al), weighted=G.weighted, directed=G.directed)
    return backtracking(edgeList.el, g.as_EL())

# dynamic programming
def editDistance(word1, word2):
    m = np.zeros((len(word1)+1, len(word2)+1), dtype=int)
    consonants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','z']
    vowels = ['a','e','i','o','u']
    
    print("Word 1 {}  Word2 {}".format(word1, word2))
    
    word1.lower()
    word2.lower()
    
    for i in range(len(m)):
        m[i][0] = i
        
    for i in range(len(m[0])):
        m[0][i] = i
        
    for i in range(1, len(m)):
        for j in range(1, len(m[i])):
            # if chars are equivalent
            if word1[i-1] == word2[j-1]:
                m[i][j] = m[i-1][j-1]
            else:
                # if both are consonants and vowels, find the min + 1
                if (word1[i-1] in consonants and word2[j-1] in consonants) or (word1[i-1] in vowels and word2[j-1] in vowels):
                    m[i][j] = min(m[i-1][j], m[i][j-1], m[i-1][j-1]) + 1
                else:
                # otherwise both are not consonants or vowels
                # not possible to replace (upper left) 
                    m[i][j] = min(m[i-1][j], m[i][j-1]) + 1
    print(m)
    
if __name__ == "__main__":
    
    # test for hamiltonian cycle - should have hamiltonian cycle
    g1 = graph.Graph(5, weighted=False, directed=False)
    g1.insert_edge(0,1)
    g1.insert_edge(1,2)
    g1.insert_edge(2,4)
    g1.insert_edge(1,4)
    g1.insert_edge(1,3)
    g1.insert_edge(0,3)
    g1.insert_edge(3,4)
    
    # test for no hamiltonian cycle
    g2 = graph.Graph(5, weighted=False, directed=False)
    g2.insert_edge(0,1)
    g2.insert_edge(1,2)
    g2.insert_edge(2,4)
    g2.insert_edge(1,4)
    g2.insert_edge(1,3)
    g2.insert_edge(0,3)
    
    choice = 0
    
    while choice < 1 or choice > 3:
        print("Options\n1. Randomized Hamiltonian\n2. Backtracking\n3. Dynamic Programming")
        choice = int(input("Choose an option: "))
        
    # randomized hamiltonian
    if choice == 1:
        
        start = time.time()
        cycle = randomizedHamiltonian(g1)
        printCycleInfo(cycle, g1)
        end = time.time()
        print("Runtime: {}".format(end - start))
        
        start = time.time()
        cycle = randomizedHamiltonian(g2)
        printCycleInfo(cycle, g2)
        end = time.time()
        print("Runtime: {}".format(end - start))

    # backtracking hamiltonian
    if choice == 2:
    
        start = time.time()
        cycle = backtrackingHamiltonian(g1)
        printCycleInfo(cycle, g1)
        end = time.time()
        print("Runtime: {}".format(end - start))
        
        start = time.time()
        cycle = backtrackingHamiltonian(g2)
        printCycleInfo(cycle, g2)
        end = time.time()
        print("Runtime: {}".format(end - start))
        
    # dynamic programming
    if choice == 3:
        
        start = time.time()
        editDistance("money", "miners")
        end = time.time()
        print("Runtime: {}".format(end - start))
        
        start = time.time()
        editDistance("aei", "iou")
        end = time.time()
        print("Runtime: {}".format(end - start))
        
        start = time.time()
        editDistance("aei", "bcd")
        end = time.time()
        print("Runtime: {}".format(end - start))
        
        start = time.time()
        editDistance("utep", "utsa")
        end = time.time()
        print("Runtime: {}".format(end - start))
            
            
            
            