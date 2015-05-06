import operator
import sys,threading

"""
The file contains the edges of a directed graph. Vertices are labeled as positive integers from 1 to 875714.
Every row indicates an edge, the vertex label in first column is the tail and the vertex label in second
column is the head (recall the graph is directed, and the edges are directed from the first column vertex
to the second column vertex). So for example, the 11th row looks liks : "2 47646". This just means that the
vertex with label 2 has an outgoing edge to the vertex with label 47646

Your task is to code up the algorithm from the video lectures for computing strongly connected components(SCCs),
and to run this algorithm on the given graph. 

Output Format: You should output the sizes of the 5 largest SCCs in the given graph, in decreasing order of sizes,
separated by commas (avoid any spaces). So if your algorithm computes the sizes of the five largest SCCs to be
500, 400, 300, 200 and 100, then your answer should be "500,400,300,200,100". If your algorithm finds less than 5 SCCs,
then write 0 for the remaining terms. Thus, if your algorithm computes only 3 SCCs whose sizes are 400, 300, and 100,
then your answer should be "400,300,100,0,0".

WARNING: This is the most challenging programming assignment of the course. Because of the size of the graph
you may have to manage memory carefully. The best way to do this depends on your programming language and
environment, and we strongly suggest that you exchange tips for doing this on the discussion forums
"""

class scc_kosaraju:
    def __init__(self, n_size):
        self.visited = None
        self.leader = {}
        self.ft = {}
        self.order = [i for i in xrange(n_size, 0, -1)]
        self.node_size = n_size
        self.t = 0
        self.count = 0
        
    def dfs(self, graph, i, s_node):
        self.visited[i] = True
        self.leader[i] = s_node
        for j in graph.get(i, []):
            if not self.visited[j]:
                self.count += 1
                self.dfs(graph, j, s_node)
        self.t += 1
        self.ft[i] = self.t

    def dfs_loop(self, graph):
        self.t = 0
        source_node = None
        #print self.order
        record = []
        for o in self.order:
            self.count = 0
            if not self.visited[o]:
                self.count += 1
                source_node = o
                self.dfs(graph, o, source_node)
                record.append(self.count)
        return sorted(record, reverse=True)

    def scc(self, graph,rev_graph):
        self.visited = [False for i in xrange(self.node_size+1)]
        self.dfs_loop(rev_graph)
        self.visited = [False for i in xrange(self.node_size+1)]
        self.order = sorted(self.ft.keys(), key=self.ft.get, reverse = True)
        s = self.dfs_loop(graph)
        print s[:5]
        print "finished"

    
                
"""
use dictionary rather than list
"""
#===================
if __name__ == "__main__":
    """
    test case ans= 3,3,3,0,0
    """
##    test_case = [[1,4],
##                 [2,8],
##                 [3,6],
##                 [4,7],
##                 [5,2],
##                 [6,9],
##                 [7,1],
##                 [8,5],
##                 [8,6],
##                 [9,7],
##                 [9,3]]
##    
##    test_case1 = [[1,2],
##                  [2,6],
##                  [2,3],
##                  [2,4],
##                  [3,1],
##                  [3,4],
##                  [4,5],
##                  [5,4],
##                  [6,5],
##                  [6,7],
##                  [7,6],
##                  [7,8],
##                  [8,5],
##                  [8,7]]
##    
##    test_case2 = [[1,2],
##                  [2,3],
##                  [3,1],
##                  [3,4],
##                  [5,4],
##                  [6,4],
##                  [8,6],
##                  [6,7],
##                  [7,8]]
##    
##    test_node_size = 9
##    test_node_size1 = 8
##    test_node_size2 = 8
    data = {}
    rev_data = {}
    """
    modify test_case
    """
##    for arc in test_case:
##        data[arc[0]] = data.get(arc[0], []) + [arc[1]]
##        rev_data[arc[1]] = rev_data.get(arc[1], []) + [arc[0]]
##    
##    print data,rev_data
    """
    modify test_node_size
    """
##    scc_instance = scc_kosaraju(test_node_size)
##    scc_instance.scc(data, rev_data)

    #stack size = 64 Mb
    threading.stack_size(67108864)
    sys.setrecursionlimit(10**6)
    
    with open("SCC.txt","r") as f:
        for line in f:
            d = [int(x) for x in line.split()]
            data[d[0]] = data.get(d[0], []) + [d[1]] 
            rev_data[d[1]] = rev_data.get(d[1], []) + [d[0]] 
    #print rev_data["1"]
    node_size = 875714
    scc_instance = scc_kosaraju(node_size)
    #scc_instance.scc(data, rev_data)
    thread = threading.Thread(target=scc_instance.scc, args=(data, rev_data,))
    thread.start()
    
    
    
