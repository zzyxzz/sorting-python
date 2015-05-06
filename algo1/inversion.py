def merge_count(arr, temp, left, right):
    middle = 0
    inv_count = 0
    
    if(left < right):
        middle = (left + right)/2
        #print middle
        inv_count = merge_count(arr, temp, left, middle)
        inv_count += merge_count(arr, temp, middle+1, right)
        inv_count += merge(arr, temp, left, middle, right)
    return inv_count

def merge(arr, temp, left, middle, right):
    i = left
    j = middle + 1
    k = left
    inv_count = 0

    while (i <= middle and j <= right):
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            inv_count += (middle + 1 - i)
            j += 1
        k += 1

    while i <= middle:
        temp[k] = arr[i]
        k += 1
        i += 1

    while j <= right:
        temp[k] = arr[j]
        k += 1
        j += 1

    t = left
    while t <= right:
        arr[t] = temp[t]
        t += 1
    
    return inv_count

#====================
if __name__ == '__main__':
    with open("IntegerArray.txt",'r') as f:
        data = [int(line) for line in f]
    #data = [1,5,4,8,10,2,6,9,12,11,3,7]
    temp = [0 for i in range(len(data))]
    left = 0
    right = len(data)-1
    
    count = merge_count(data, temp, left, right)
    print count
    #print temp
    
    
