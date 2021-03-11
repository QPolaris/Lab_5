#!/usr/bin/python3
from random import randrange


def RandomizedPartition(A, p, r):
    """
    Implement Randomized partitioning from Cormen book (same as lab 4)
    """
    i = randrange(p,r)
    A[r], A[i] = A[i], A[r]
    return part(A, p, r)
    
def part(A, p, r):
    x = A[r]
    i = p-1
    for j in range(p, r):
        if A[j] <= x:
            i = i+1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return (i+1)
    


def OrderStatistics(array, p, r, i):
    """
    Return ith order statistics
    OrderStatistics(array, p, r, i), returns  the ith smallest element of the array array[p...r]
    
    For example in array = [81,71,99,68,45,55,0,22,11,34]
    return 0 for i = 0 [smallest]
    return 11 for i = 1
    return 22 for i = 2
    return 34 for i = 3
    return 45 for i = 4
    return 55 for i = 5
    return 68 for i = 6
    return 71 for i = 7
    return 81 for i = 8
    return 99 for i = 9 [largest]
    
    Your solution should run in lineartime using RandomizedPartition.
    40% points will be deducted for non-linear solutions
    
    For hints check Chapter 9 from Cormen book.
    
    """
    if p == r:
        return array[p]
    q = RandomizedPartition(array, p, r)
    k = (q - p) + 1
    if i+1 == k:
        return array[q]
    elif i+1 < k:
        return OrderStatistics(array, p, (q-1), i)
    else:
        return OrderStatistics(array, (q+1), r, (i-k))
