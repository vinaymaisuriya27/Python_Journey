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

#Merge_Sort_Start
def merge_sorted(lst):
    if len(lst) <= 1:
        return

    mid = len(lst)//2
    left_lst = lst[:mid]
    right_lst = lst[mid:]

    merge_sorted(left_lst)
    merge_sorted(right_lst)

    merge_list(left_lst, right_lst, lst)
    return lst

def merge_list(left_lst, right_lst, lst):
    i = j = k = 0
    while i < len(left_lst) and j < len(right_lst):
        if left_lst[i] <= right_lst[j]:
            lst[k] = left_lst[i]
            i += 1
        else:
            lst[k] = right_lst[j]
            j += 1
        k +=1

    while i < len(left_lst):
        lst[k] = left_lst[i]
        i += 1
        k += 1

    while j < len(right_lst):
        lst[k] = right_lst[j]
        j += 1
        k += 1
    return lst
#Merge_Sort_End

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

start = time()
merge_sorted(lst)
end = time()
print("%0.10f" % (end-start))