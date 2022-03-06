from time import time
import random

def bubble_sort(lst):
    for i in range(len(lst)):
        for element in range(len(lst)-i-1):
            if lst[element] > lst[element+1]:
                lst[element], lst[element+1] = lst[element+1], lst[element]
    print(lst)

def selection_sort(lst):
    global min_pos
    for i in range(len(lst)-1):
        for element in range(i+1, len(lst)):
            min = lst[i]
            min_pos = i
            if min > lst[element]:
                min = lst[element]
                min_pos = element
        lst[i], lst[min_pos] = lst[min_pos], lst[i]
    print(lst)

def insertion_sort(lst):
    for i in range(1, len(lst)):
        x = lst[i]
        j = i - 1
        while j >= 0 and x < lst[j]:
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = x
    print(lst)

lst = [random.randint(0, 5) for i in range(1000)]
print(lst)

start = time()
bubble_sort(lst)
end = time()
print("%0.10f" % (end-start))

start = time()
selection_sort(lst)
end = time()
print("%0.10f" % (end-start))

start = time()
insertion_sort(lst)
end = time()
print("%0.10f" % (end-start))