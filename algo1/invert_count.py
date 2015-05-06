def merge_count(left_arr, right_arr):
    i = 0
    j = 0
    invM = 0
    sortedA = []

    while left_arr and right_arr and i < len(left_arr) and j < len(right_arr):
        if left_arr[i] < right_arr[j]:
            sortedA.append(left_arr[i])
            i += 1
        else:
            sortedA.append(right_arr[j])
            invM += len(left_arr) - i
            j += 1
    while i < len(left_arr):
        sortedA.append(left_arr[i])
        i += 1

    while j < len(right_arr):
        sortedA.append(right_arr[j])
        j += 1

    return invM, sortedA

def sort_count(arr):
    if len(arr) <= 1:
        return 0, arr 
    middle = len(arr)/2
    left_arr = arr[:middle]
    right_arr = arr[middle:]
    
    invL, sortedL = sort_count(left_arr)
    invR, sortedR = sort_count(right_arr)

    invM, sortedA = merge_count(sortedL, sortedR)
    inv_total = invL + invR + invM
    return inv_total, sortedA


#====================
if __name__ == '__main__':
    with open("IntegerArray.txt",'r') as f:
        data = [int(line) for line in f]
    #data = [1,5,4,8,10,2,6,9,12,11,3,7]
    
    count,sorted_arr = sort_count(data)
    print count
    
  
