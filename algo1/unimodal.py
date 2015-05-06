""" You are a given a unimodal array of n distinct elements,
meaning that its entries are in increasing order up until its
maximum element, after which its elements are in decreasing order.
Give an algorithm to compute the maximum element that runs
in O(log n) time."""

def find_max(arr):
    if len(arr) == 2:
        #print arr
        return max(arr[0],arr[1])
    middle = len(arr)/2
    print middle
    if arr[middle] < arr[middle+1]:
        right = arr[middle:]
        #print right
        maxx = find_max(right)
    else:
        left = arr[:middle+1]
        #print left
        maxx = find_max(left)
    return maxx

#===============
if __name__ == "__main__":
    data = [1,3,5,7,8,6,4,2]
    maxx = find_max(data)
    print maxx
