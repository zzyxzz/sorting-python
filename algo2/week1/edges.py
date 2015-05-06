"""
In this programming problem you'll code up Prim's minimum spanning tree
algorithm. Download the text file here. This file describes an undirected
graph with integer edge costs. It has the format
[number_of_nodes] [number_of_edges]
[one_node_of_edge_1] [other_node_of_edge_1] [edge_1_cost]
[one_node_of_edge_2] [other_node_of_edge_2] [edge_2_cost]
...
For example, the third line of the file is "2 3 -8874",
indicating that there is an edge connecting vertex #2 and vertex #3
that has cost -8874. You should NOT assume that edge costs are positive,
nor should you assume that they are distinct.

Your task is to run Prim's minimum spanning tree algorithm on this graph.
You should report the overall cost of a minimum spanning tree ---
an integer, which may or may not be negative --- in the box below.

IMPLEMENTATION NOTES: This graph is small enough that the straightforward
O(mn) time implementation of Prim's algorithm should work fine.
OPTIONAL: For those of you seeking an additional challenge, try
implementing a heap-based version. The simpler approach, which should
already give you a healthy speed-up, is to maintain relevant edges
in a heap (with keys = edge costs). The superior approach stores the
unprocessed vertices in the heap, as described in lecture.
Note this requires a heap that supports deletions, and you'll probably
need to maintain some kind of mapping between vertices and their positions
in the heap.
"""
import heapq

def prim_algo(edges,number_of_nodes):

    visited = {}
    #print edges.keys()
    init_node = 15
    visited[init_node] = True
    spanning_tree = edges[init_node]
    heapq.heapify(spanning_tree)
    edge_cost = 0
    
    print spanning_tree
    while len(visited) < number_of_nodes:
        spanning_edge_cost,new_spanning_node = heapq.heappop(spanning_tree)
        if not visited.get(new_spanning_node,False):
            edge_cost += spanning_edge_cost
            visited[new_spanning_node] = True
            for edge in edges[new_spanning_node]:
                heapq.heappush(spanning_tree,edge)

    return edge_cost
    
###############
if __name__ == "__main__":
    edges = {}
    idx = True
    with open("edges.txt") as f:
        for line in f:
            edge = [int(e) for e in line.split()]
            if idx:
                num_of_nodes = edge[0]
                num_of_edges = edge[1]
                idx = False
            else:
                one_node   = edge[0]
                other_node = edge[1]
                edge_cost  = edge[2]
                edges[one_node] = edges.get(one_node,[]) + [(edge_cost,other_node)]
                edges[other_node] = edges.get(other_node,[]) + [(edge_cost,one_node)]#reverse
    print " number of nodes {},\n number of nodes {},\n number of edges {}".format(len(edges),num_of_nodes,num_of_edges)
    cost = prim_algo(edges,num_of_nodes)
    print "edge cost {}".format(cost)    





    
