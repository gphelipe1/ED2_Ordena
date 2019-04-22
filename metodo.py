
#================INSERTIONSORT===================
def insertionSortfreq(ar1,ar2):

    for i in range(1, len(ar1)):
 
        key = ar1[i]
        key2 = ar2[i]
        j = i-1
        while j >=0 and key > ar1[j] :
                ar1[j+1] = ar1[j]
                ar2[j+1] = ar2[j]
                j -= 1
        ar2[j+1] = key2
        ar1[j+1] = key

#~..................................

def insertionSortAlfa(ar1):

    for i in range(1, len(ar1)):
 
        key = ar1[i]
        j = i-1
        while j >=0 and key < ar1[j] :
                ar1[j+1] = ar1[j]
                j -= 1
        ar1[j+1] = key
#============================================



#=================QUICKSORT=====================
def partition(arr,low,high):
    i = ( low-1 )         # index do menor elemento
    pivot = arr[high]     # pivo
 
    for j in range(low , high):
 
        # Se o elemento atual eh menor que ou
        # igual ao pivo
        if   arr[j] <= pivot:
         
            # incrementa o index do menor elemento
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]
 
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return ( i+1 )

# arr[] --> Array 
# low  --> index inicial
# high  --> index final 
def quickSortAlfa(arr,low,high):
    if low < high:
 
        # pi eh o index particionado, arr[p] esta agora
        # no lugar certo
        pi = partition(arr,low,high)
 
        # ordenando separadamente os que
        # se encontram antes e depois da particao
        quickSortAlfa(arr, low, pi-1)
        quickSortAlfa(arr, pi+1, high)

#...................................

def partition2(arr,low,high,arr2):
    i = ( low-1 )         # index do menor elemento
    pivot = arr[high]     # pivo
 
    for j in range(low , high):
 
        # Se o elemento atual eh menor que ou
        # igual ao pivo
        if   not (arr[j] <= pivot):
         
            # incrementa o index do menor elemento
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]
            arr2[i],arr2[j] = arr2[j],arr2[i]
 
    arr[i+1],arr[high] = arr[high],arr[i+1]
    arr2[i+1],arr2[high] = arr2[high],arr2[i+1]
    return ( i+1 )
 

# arr[] --> Array 
# low  --> index inicial
# high  --> index final 
def quickSortFreq(arr,low,high,arr2):
    if low < high:
 
        # pi eh o index particionado, arr[p] esta agora
        # no lugar certo
        pi = partition2(arr,low,high,arr2)
 
        # ordenando separadamente os que
        # se encontram antes e depois da particao
        quickSortFreq(arr, low, pi-1,arr2)
        quickSortFreq(arr, pi+1, high,arr2)


#=================================================

#===================SHELLSORT=====================
def shellSortAlfa(arr):
 
    # Start with a big gap, then reduce the gap
    n = len(arr)
    gap = n//2
 
    # Do a gapped insertion sort for this gap size.
    # The first gap elements a[0..gap-1] are already in gapped 
    # order keep adding one more element until the entire array
    # is gap sorted
    while gap > 0:
 
        for i in range(gap,n):
 
            # add a[i] to the elements that have been gap sorted
            # save a[i] in temp and make a hole at position i
            temp = arr[i]
 
            # shift earlier gap-sorted elements up until the correct
            # location for a[i] is found
            j = i
            while  j >= gap and arr[j-gap] >temp:
                arr[j] = arr[j-gap]
                j -= gap
 
            # put temp (the original a[i]) in its correct location
            arr[j] = temp
        gap //= 2
#~..................................
def shellSortFreq(arr,arr2):
 
    # Start with a big gap, then reduce the gap
    n = len(arr)
    gap = n//2
 
    # Do a gapped insertion sort for this gap size.
    # The first gap elements a[0..gap-1] are already in gapped 
    # order keep adding one more element until the entire array
    # is gap sorted
    while gap > 0:
 
        for i in range(gap,n):
 
            # add a[i] to the elements that have been gap sorted
            # save a[i] in temp and make a hole at position i
            temp = arr[i]
            temp2= arr2[i]
 
            # shift earlier gap-sorted elements up until the correct
            # location for a[i] is found
            j = i
            while  (j >= gap and arr[j-gap] <temp):
                arr[j] = arr[j-gap]
                arr2[j] = arr2[j-gap]
                j -= gap
 
            # put temp (the original a[i]) in its correct location
            arr[j] = temp
            arr2[j] = temp2
        gap //= 2
#==================================================


#====================HEAPSORT=====================
def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1     # left = 2*i + 1
    r = 2 * i + 2     # right = 2*i + 2
 
    # See if left child of root exists and is
    # greater than root
    if l < n and arr[i] < arr[l]:
        largest = l
 
    # See if right child of root exists and is
    # greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r
 
    # Change root, if needed
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]  # swap
 
        # Heapify the root.
        heapify(arr, n, largest)
 
# The main function to sort an array of given size
def heapSortAlfa(arr):
    n = len(arr)
 
    # Build a maxheap.
    for i in range(n, -1, -1):
        heapify(arr, n, i)
 
    # One by one extract elements
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]   # swap
        heapify(arr, i, 0)

#~..................................

def heapifyF(arr, n, i,arr2):
    largest = i  # Initialize largest as root
    l = 2 * i + 1     # left = 2*i + 1
    r = 2 * i + 2     # right = 2*i + 2
 
    # See if left child of root exists and is
    # greater than root
    if l < n and arr[i] > arr[l]:
        largest = l
 
    # See if right child of root exists and is
    # greater than root
    if r < n and arr[largest] > arr[r]:
        largest = r
 
    # Change root, if needed
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]  # swap
        arr2[i],arr2[largest] = arr2[largest],arr2[i]
 
        # Heapify the root.
        heapifyF(arr, n, largest,arr2)
 
# The main function to sort an array of given size
def heapSortFreq(arr,arr2):
    n = len(arr)
 
    # Build a maxheap.
    for i in range(n, -1, -1):
        heapifyF(arr, n, i,arr2)
 
    # One by one extract elements
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]   # swap
        arr2[i], arr2[0] = arr2[0], arr2[i] 
        heapifyF(arr, i, 0,arr2)
#===============================================

#==============BINARY_INSERTIONSORT=============
def binary_search(arr, val, start, end):
    # we need to distinugish whether we should insert
    # before or after the left boundary.
    # imagine [0] is the last step of the binary search
    # and we need to decide where to insert -1
    if start == end:
        if arr[start] > val:
            return start
        else:
            return start+1
 
    # this occurs if we are moving bseyond left's boundary
    # meaning the left boundary is the least position to
    # find a number greater than val
    if start > end:
        return start
 
    mid = (start+end)//2
    if arr[mid] < val:
        return binary_search(arr, val, mid+1, end)
    elif arr[mid] > val:
        return binary_search(arr, val, start, mid-1)
    else:
        return mid
 
def binary_insert_sortAlfa(arr):
    for i in range(1, len(arr)):
        val = arr[i]
        j = binary_search(arr, val, 0, i-1)
        arr[:] = arr[:j] + [val] + arr[j:i] + arr[i+1:]

#.....................................

def binary_searchFreq(arr, val, start, end,arr2):
    # we need to distinugish whether we should insert
    # before or after the left boundary.
    # imagine [0] is the last step of the binary search
    # and we need to decide where to insert -1
    if start == end:
        if arr[start] < val:
            return start
        else:
            return start+1
 
    # this occurs if we are moving beyond left's boundary
    # meaning the left boundary is the least position to
    # find a number greater than val
    if start > end:
        return start
 
    mid = (start+end)//2
    if arr[mid] < val:
        return binary_searchFreq(arr, val, mid+1, end,arr2)
    elif arr[mid] > val:
        return binary_searchFreq(arr, val, start, mid-1,arr2)
    else:
        return mid
 
def binary_insert_sortFreq(arr,arr2):
    for i in range(1, len(arr)):
        val = arr[i]
        val2=arr2[i]
        j = binary_searchFreq(arr, val, 0, i-1,arr2)
        arr[:] = arr[:j] + [val] + arr[j:i] + arr[i+1:]
        arr2[:] = arr2[:j] + [val2] + arr2[j:i] + arr2[i+1:]
#==============================================
