import random
import copy

"""
The file contains the adjacency list representation of a simple undirected graph. There are 200 vertices labeled 1 to 200.
The first column in the file represents the vertex label, and the particular row (other entries except the first column)
tells all the vertices that the vertex is adjacent to. So for example, the 6th row looks like : "6 155 56 52 120......".
This just means that the vertex with label 6 is adjacent to (i.e., shares an edge with) the vertices with labels 155,56,52,120,......,etc

Your task is to code up and run the randomized contraction algorithm for the min cut problem and use it on the above graph
to compute the min cut (i.e., the minimum-possible number of crossing edges). (HINT: Note that you'll have to figure out
an implementation of edge contractions. Initially, you might want to do this naively, creating a new graph from the old
every time there's an edge contraction. But you should also think about more efficient implementations.) (WARNING: As
per the video lectures, please make sure to run the algorithm many times with different random seeds, and remember the
smallest cut that you ever find.) Write your numeric answer in the space provided. So e.g., if your answer is 5,
just type 5 in the space provided
"""

def generate_rand(l_size):
    return random.randint(0,l_size-1)

def make_edge_list(data):
    edges = []
    for i in data:
        for j in i:
            if j != i[0]:
                edge = [i[0], j]
                edge.sort()
                if edge not in edges:
                    edges.append(edge)
    return edges
    
def min_cut(edges,nodes):
    if nodes <= 2:
        return edges
    idx = generate_rand(len(edges))
    edge = edges[idx]
    vertex1 = edge[0]
    vertex2 = edge[1]

    ##merge two vertices that v1 replaces v2
    for i in xrange(len(edges)-1,-1,-1):
        if edges[i][0] == vertex2:
            edges[i][0] = vertex1
        if edges[i][1] == vertex2:
            edges[i][1] = vertex1
        edges[i].sort()

        if edges[i][0] == edges[i][1]:

            edges.pop(i)
    nodes -= 1
    cut = min_cut(edges,nodes)
    return cut
        

##################
if __name__ == "__main__":
    data = []
    with open("kargerMinCut.txt","r") as f:
        for line in f:
            data.append([int(x) for x in line.split()])
    test_case = [[1,4,2,7,3],
                 [2,4,1,3],
                 [3,1,2,4],
                 [4,5,1,2,3],
                 [5,8,7,6,4],
                 [6,8,5,7],
                 [7,6,8,5,1],
                 [8,7,6,5]]

    cnts = []
    ## trials
    d_edges = make_edge_list(data)
    for _ in xrange(100):
        nodes = len(data)
        #print len(edges)
        edges = copy.deepcopy(d_edges)
        count = min_cut(edges,nodes)
        #print len(count)
        cnts.append(len(count))
    print "-------"
    print min(cnts)
            
