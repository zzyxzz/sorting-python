import heapq

"""
The file contains an adjacency list representation of an undirected weighted graph with 200 vertices
labeled 1 to 200. Each row consists of the node tuples that are adjacent to that particular vertex
along with the length of that edge. For example, the 6th row has 6 as the first entry indicating that
this row corresponds to the vertex labeled 6. The next entry of this row "141,8200" indicates that
there is an edge between vertex 6 and vertex 141 that has length 8200. The rest of the pairs of
this row indicate the other vertices adjacent to vertex 6 and the lengths of the corresponding edges.

Your task is to run Dijkstra's shortest-path algorithm on this graph, using 1 (the first vertex) as
the source vertex, and to compute the shortest-path distances between 1 and every other vertex of
the graph. If there is no path between a vertex v and vertex 1, we'll define the shortest-path
distance between 1 and v to be 1000000. 

You should report the shortest-path distances to the following ten vertices, in order:
7,37,59,82,99,115,133,165,188,197. You should encode the distances as a comma-separated string of
integers. So if you find that all ten of these vertices except 115 are at distance 1000 away from
vertex 1 and 115 is 2000 distance away, then your answer should be 1000,1000,1000,1000,1000,2000,1000,1000,1000,1000.
Remember the order of reporting DOES MATTER, and the string should be in the same order in
which the above ten vertices are given. Please type your answer in the space provided.

IMPLEMENTATION NOTES: This graph is small enough that the straightforward O(mn) time implementation
of Dijkstra's algorithm should work fine. OPTIONAL: For those of you seeking an additional challenge,
try implementing the heap-based version. Note this requires a heap that supports deletions, and you'll
probably need to maintain some kind of mapping between vertices and their positions in the heap.
"""
    
def dijkstra(graph, source, dest):
    dist_d = {}
    cloud = {}
    hq = []
    record = {}
    trace = {}

    """
    initialise the graph using priority queue implemented by heapq
    """
    for v in graph:
        if v is source:
            dist_d[v] = 0
        else:
            dist_d[v] = 1000000
        heapq.heappush(hq,(dist_d[v], v))

    """
    do dijkstra algorithm    
    """
    while hq:
        #pop the vertex with min distance from source;key is distance
        key, u = heapq.heappop(hq)
        #check whether current vertex is visited
        if u in cloud:
            continue
        #if not visited, mark it visited
        cloud[u] = key
        #if u is target record the distance
        if u in dest:
            record[u] = key
        #visit all the neighbours of u
        for v in graph[u]:
            #if not visited
            if v not in cloud:
                #get the distance between u and v
                wgt = graph[u][v]
                #if current distance from source to v is smaller than previous distance
                if dist_d[u] + wgt < dist_d[v]:
                    #replace previous distance; update distance
                    dist_d[v] = dist_d[u] + wgt
                    #push updated distance to queue
                    heapq.heappush(hq,(dist_d[v],v))
                    #record pre vertex u of current v or update pre vertex of v
                    #trace can be used to show path from target to source
                    #such as:   path = trace[target] --> path = trace[path] until path == source
                    trace[v] = u
    return record

##============================
if __name__ == "__main__":
    data = {}
    with open("dijkstraData.txt","r") as f:
        for line in f:
            l = line.split()
            key = int(l[0])
            l = l[1:]
            data[key] = {}
            for x in l:
                pair = x.split(",")
                data[key][int(pair[0])] = int(pair[1])
    print "start"

    source = 1
    dest = [7,37,59,82,99,115,133,165,188,197]
    
    print dijkstra(data, source, dest)
    
        
        
        
