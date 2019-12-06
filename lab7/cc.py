# code from class website

import graph_AL as graph
import dsf

def connected_components(g):
    vertices = len(g.al)
    components = vertices
    s = dsf.DSF(vertices)
    for v in range(vertices):
        for edge in g.al[v]:
            components -= s.union(v, edge.dest)
            # s.draw()
    return components, s
        
