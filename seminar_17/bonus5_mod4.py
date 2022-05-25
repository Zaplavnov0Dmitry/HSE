import random
import numpy as np
import time

start_time = time.perf_counter()
def quickselectsort(l, k):
    if (len(l) == 1):
        k = 0
        return l[k]
    pivot = l[random.randint(0, len(l)-1)]

    lesser_els = [el for el in l if el < pivot]
    greater_els = [el for el in l if el > pivot]
    pivots = [el for el in l if el == pivot]

    if (k < len(lesser_els)):
        return quickselectsort(lesser_els, k)
    elif (k < len(lesser_els) + len(pivots)):
        return pivots[0]
    else:
        return quickselectsort(greater_els, k - len(lesser_els) - len(pivots))


if __name__ == '__main__':
    l = np.random.randint(0, 10, 6000)
    print(sorted(l))
    k = (len(l) // 2)
    print(quickselectsort(l, k))
print("--- %.8f seconds ---" %(time.perf_counter() - start_time))