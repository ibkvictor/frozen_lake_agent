import numpy as np
import pandas as pd

def merge (left,right):
    new_list = []
    counteri, counterj = 0, 0
    while counteri < len(right) and counterj < len(right):
        if left[counteri] < right[counterj]:
            new_list.append(left[counteri])
            counteri += 1
        else :
            new_list.append(right[counterj])
            counterj += 1
    while counteri < len(left):
        new_list.append(left[counteri])
        counteri += 1
    while counterj < len(right):
        new_list.append(right[counterj])
        counterj += 1
    return new_list

def merge_sort(L):
    if len(L) < 2:
        return L[:]

    else:
        middle = int(len(L)/2)
        left = merge_sort(L[:middle])
        right = merge_sort(L[middle:])
        print("just broke a list")
        return merge(left,right)
    
# listy = [5,6,3,2,6,7,2,5]
# print (merge_sort(listy))

print (np.random.randn(10,10))