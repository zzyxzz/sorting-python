def max_one(arr):
    if len(arr)==2:
        if arr[0] < arr[1]:
            return arr[1],[arr[0],]
        else:
            return arr[0],[arr[1],]
    else:
        middle = len(arr)/2
        left = arr[:middle]
        right = arr[middle:]

        maxL,secL = max_one(left)
        maxR,secR = max_one(right)      

        if maxL < maxR:
            secR.append(maxL)
            return maxR,secR
        else:
            secL.append(maxR)
            return maxL,secL

def sec_max(arr):
    max0,list_path = max_one(arr)
    return max(list_path)
    
#====================
if __name__ == '__main__':
    '''large data will incur recursion deep error'''
    #with open("IntegerArray.txt",'r') as f:
    #    data = [int(line) for line in f]
    data = [1,5,4,8,10,13,2,6,9,12,15,16,14,11,3,7]
    secMax = sec_max(data)
    print secMax
