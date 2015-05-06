def build_tree(arr):
    arr_len = len(arr)
    num_nodes = 1
    
    while num_nodes < arr_len:
        num_nodes = num_nodes * 2
        
    tree_size = 2*num_nodes - 1
    offset = tree_size - arr_len
    tree = [0 for i in xrange(tree_size)]
    
    for i in xrange(arr_len):
        tree[offset + i] = i

    for i in xrange(tree_size - 1, 0, -2):
        tree[i/2-1] = (tree[i] if arr[tree[i]] > arr[tree[i-1]] else tree[i-1])
    return tree,offset

def adjust(tree,arr,offset):
    maxInd = tree[0]
    arr[maxInd] = None
    idx = offset + maxInd
    while idx != 0:
        if idx%2 == 0:
            tree[idx/2 - 1] = (tree[idx] if arr[tree[idx]]> arr[tree[idx-1]] else tree[idx-1])
            idx = idx/2-1
        else:
            tree[idx/2] = (tree[idx] if arr[tree[idx]] > arr[tree[idx+1]] else tree[idx+1])
            idx = idx/2
    return tree
    
def find_sec(arr,topk):
    tree,offset = build_tree(arr)
    topV = [0 for i in xrange(topk)]
    topV[0] = arr[tree[0]]
    for i in xrange(1,topk):
        new_tree = adjust(tree,arr,offset)
        topV[i] = arr[new_tree[0]]
    return topV
    
#====================
if __name__ == '__main__':
    with open("IntegerArray.txt",'r') as f:
        data = [int(line) for line in f]
    #data = [1,5,4,8,10,13,2,6,9,12,15,16,14,11,3,7]
    tree = find_sec(data,100)
    print tree
