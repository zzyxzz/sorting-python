
"""
The goal of this problem is to implement a variant of the 2-SUM algorithm
(covered in the Week 6 lecture on hash table applications).
The file contains 1 million integers, both positive and negative (there
might be some repetitions!).This is your array of integers, with the ith row
of the file specifying the ith entry of the array.

Your task is to compute the number of target values t in the interval [-10000,10000] (inclusive)
such that there are distinct numbers x,y in the input file that satisfy x+y=t. (NOTE:
ensuring distinctness requires a one-line addition to the algorithm from lecture.)

Write your numeric answer (an integer between 0 and 20001) in the space provided.

OPTIONAL CHALLENGE: If this problem is too easy for you, try implementing your own hash
table for it. For example, you could compare performance under the chaining and open
addressing approaches to resolving collisions.
"""

def two_sum(data, data_dict, w, T_min):

    results = []
    for key in data:
        try:
            for t in (data_dict[(T_min-key)/w]):
                if key != t and T_min <= key + t <= T_max:
                    results.append(key + t)
        except:
            pass
        try:
            for t in (data_dict[(T_min-key)/w + 1]):
                if key != t and T_min <= key + t <= T_max:
                    results.append(key + t)
        except:
            pass
    return set(results)
        


####==========================
if __name__ == "__main__":
    data = {}
    data_dict = {}
    T_max = 10000
    T_min = -10000
    w = T_max - T_min + 1

    with open("algo1-programming_prob-2sum.txt","r") as f:
        for line in f:
            data[int(line)] = True
            data_dict[int(line)/w] = data_dict.get(int(line)/w,[]) + [int(line)]
    print len(data)
    print len(data_dict)
    print len(two_sum(data, data_dict, w, T_min))
    
