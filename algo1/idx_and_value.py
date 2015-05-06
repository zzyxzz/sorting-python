"""You are given a sorted (from smallest to largest) array A of n distinct
integers which can be positive, negative, or zero. You want to decide
whether or not there is an index i such that A[i] = i.
Design the fastest algorithm that you can for solving this problem"""

def idx_eq_value(arr,start,end):
    val = False
    if start == end:
        return True if arr[start] == start else False
    middle = (start + end)/2
    print middle
    if middle < arr[middle]:
        val = idx_eq_value(arr, start, middle - 1)
    elif middle > arr[middle]:
        val = idx_eq_value(arr, middle + 1, end)
    else:
        return True
    return val

#=============
if __name__ == "__main__":
    data = [-3, -2, -1, 1, 2, 5, 15, 26, 47]
    val = idx_eq_value(data,0,len(data)-1)
    print val



