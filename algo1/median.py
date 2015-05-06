# -*- coding: utf-8 -*-
"""
The goal of this problem is to implement the "Median Maintenance" algorithm
covered in the Week 5 lecture on heap applications). The text file contains
a list of the integers from 1 to 10000 in unsorted order; you should treat
this as a stream of numbers, arriving one by one. Letting xi denote the ith
number of the file, the kth median mk is defined as the median of the numbers
x1,…,xk. (So, if k is odd, then mk is ((k+1)/2)th smallest number among x1,…,xk;
if k is even, then mk is the (k/2)th smallest number among x1,…,xk.)

In the box below you should type the sum of these 10000 medians, modulo 10000
(i.e., only the last 4 digits). That is, you should compute
(m1+m2+m3+⋯+m10000)mod10000.

OPTIONAL EXERCISE: Compare the performance achieved by heap-based and
search-tree-based implementations of the algorithm.
"""

import heapq

class streamMedian: 
	def __init__(self): 
		self.minHeap, self.maxHeap = [], [] 
		self.N=0   
		
	def insert(self, num): 
		if self.N%2==0: 
			heapq.heappush(self.maxHeap, -1*num) 
			self.N+=1 
			if len(self.minHeap)==0: 
				return 
			if -1*self.maxHeap[0]>self.minHeap[0]: 
				toMin=-1*heapq.heappop(self.maxHeap) 
				toMax=heapq.heappop(self.minHeap) 
				heapq.heappush(self.maxHeap, -1*toMax) 
				heapq.heappush(self.minHeap, toMin) 
		else: 
			toMin=-1*heapq.heappushpop(self.maxHeap, -1*num) 
			heapq.heappush(self.minHeap, toMin) 
			self.N+=1
			
	def getMedian(self): 
		return -1*self.maxHeap[0]

##=================
if __name__ == "__main__":
    sm = streamMedian()
    median = []
    with open("Median.txt","r") as f:
        for line in f:
            d = int(line)
            sm.insert(d)
            m = sm.getMedian()
            median.append(m)
    print sum(median)%10000
