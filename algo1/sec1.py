## to find index of max_element in array
def max_ind(arr, start, end):
    
    ## base case
    if start == end:
        return start               

    mid = (start+end)/2 ## partioning the array to solve subproblems

    ## solving problems recursivly
    first = max_ind(arr, start, mid) 
    second = max_ind(arr, mid+1, end)

    if arr[first] > arr[second]:
        num[first].append(arr[second]) ## storing values compared in corresponding array
        return first
    else:
        num[second].append(arr[first])
        return second

#=================
if __name__ == "__main__":
##    data = [1,5,4,8,10,13,2,6,9,12,15,16,14,11,3,7] ## sample input array
    
    with open("IntegerArray.txt","r") as f:
        data = [int(line) for line in f]
    
    num = [[] for i in xrange(len(data))]    ## array of arrays to store path corresponding to each element

    ind = max_ind(data, 0, len(data)-1) ## get index of max_element in array

    ## calculating the max value among the values compared with the overall max value in array
    max_val = num[ind][0]
    for i in num[ind][1:]:
        max_val = max(max_val, i)
    print 'second largest value:', max_val
    print len(num[10000])
