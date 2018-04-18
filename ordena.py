#================INSERTSORT===================
def insert(vet, size, cmp):
    for i in range(1, size):
        selected = vet[i]
        j = i - 1
        while (j >= 0) and cmp(vet[j], selected) > 0:
            vet[j + 1] = vet[j]
            j = j - 1
        vet[j + 1] = selected
#=============================================



#==================QUICKSORT======================
def quick(vet, first, last, cmp):
    i = first
    j = last - 1
    pivot = vet[last - 1]
    while i <= j:
        while cmp(vet[i], pivot) == -1 and i < last:
            i = i + 1

        while cmp(vet[j], pivot) == 1 and j > first:
            j = j - 1
        if i <= j:
            vet[j], vet[i] = vet[i], vet[j]
            i = i + 1
            j = j - 1

    if j > first:
        quick(vet, first, j + 1, cmp)

    if i < last:
        quick(vet, i, last, cmp)
#=================================================



#================SHELLSORT====================
def shell(vet, h, size, cmp):
    flag = 0
    if h < 1:
        h = 2
    while h > 1 or flag:
        for i in range(h, size):

            selected = vet[i]
            j = i
            while  j >= h and cmp(vet[j-h], selected) > 0:
                vet[j] = vet[j-h]
                j = j - h
            vet[j] = selected

        h = (h + 1) // 2
#================================================



#=================HEAPSORT==================
def heap_bdm(vet, n, i, cmp):
    largest = i
    l = 2*i + 1
    r = 2*i + 2
    if l < n and cmp(vet[i], vet[l]) == -1:
        largest = l
    if r < n and cmp(vet[largest], vet[r]) == -1:
        largest = r
    if largest != i:
        vet[i], vet[largest] = vet[largest], vet[i]
        heap_bdm(vet, n, largest, cmp)

def heap(vet, cmp):
    n = len(vet)
    for i in range(n, -1, -1):
        heap_bdm(vet, n, i, cmp)
    for i in range(n - 1, 0, -1):
        vet[i], vet[0] = vet[0], vet[i]
        heap_bdm(vet, i, 0, cmp)
#===========================================



#===============BINARY INSERTSORT=================
def binary_search(vet, key, low, high, cmp):
    mid = (low + high) // 2
    if high <= low:
        if cmp(key, vet[low]) == 1:
            return low + 1
        else:
            return low
    if cmp(key, vet[mid]) == 0:
        return mid + 1
    elif cmp(key, vet[mid]) == 1:
        return binary_search(vet, key, mid + 1, high)
    return binary_search(vet, key, low, mid - 1)


def binary_insertSort(vet, size, cmp):
    for i in range(0, size):
        j = i - 1
        key = vet[i]
        location = binary_search(vet, key, 0, j, cmp)
        while j >= location:
            vet[j + 1] = vet[j]
            j = j - 1
        vet[j + 1] = key
#================================================



def timsort(the_array):
    runs, sorted_runs = [], []
    l = len(the_array)
    new_run = [the_array[0]]
    for i in range(1, l):
        if i == l-1:
            new_run.append(the_array[i])
            runs.append(new_run)
            break
        if the_array[i] < the_array[i-1]:
            if not new_run:
                runs.append([the_array[i-1]])
                new_run.append(the_array[i])
            else:
                runs.append(new_run)
                new_run = []
        else:
            new_run.append(the_array[i])
    for each in runs:
        sorted_runs.append(insertion_sort(each))
    sorted_array = []
    for run in sorted_runs:
        sorted_array = merge(sorted_array, run)
    print sorted_array