#!/usr/bin/python
import math
import timeit
import json
import random
import sys

class Sorting_Method:
    def __init__(self, name, elapsed_time):
        self.name = name
        self.elapsed_time = elapsed_time

class Sorting_Methods:
    def __init__(self):
        sys.setrecursionlimit(1000000)
        self.methods = []

sorting_methods = Sorting_Methods()


def parse():
    data = json.loads(open('data.json').read())
    print('Parsed {} elements'.format(len(data)))
    return data


def insertion_sort(data):
    print('Executing insertion sort')
    start_time = timeit.default_timer()
    for i in range(1, len(data)):
        key = data[i]
        j = i
        while j >0 and data[j-1] > key:
            data[j] = data[j-1]
            j-=1
        data[j] = key 
    elapsed = timeit.default_timer() - start_time
    method_info = Sorting_Method('insertion sort', elapsed)
    sorting_methods.methods.append(method_info)
    return method_info


def bubble_sort(data):
    print('Executing bubble sort')
    start_time = timeit.default_timer()
    sorted = False
    x = len(data)
    while x > 1 and sorted is False:
        sorted = True
        for i in range(1, x):
            if (data[i-1] > data[i]):
                temp = data[i-1]
                data[i] = temp
                sorted - False
        x-=1
    elapsed = timeit.default_timer() - start_time
    method_info = Sorting_Method('bubble sort', elapsed)
    sorting_methods.methods.append(method_info)
    return method_info

def selection_sort(data):
    print('Executing selection sort')    
    start_time = timeit.default_timer()
    sub = []
    x=0
    for i in range(1, len(data)):
        j=i
        lower = data[j]
        for j in range(i, len(data)):
            if data[j] < lower:
                lower = data[j]
                data.remove(j)
        sub.append(lower)
        x+=1
    data = sub
    elapsed = timeit.default_timer() - start_time
    method_info = Sorting_Method('selection sort', elapsed)
    sorting_methods.methods.append(method_info)
    return method_info


def merge(a, b):
    c = []
    while len(a) and len(b) > 0:
        if a[0] > b[0]:
            c.append(b[0])
            b.remove(0)
        else:
            c.append(a[0])
            a.remove(0)
    while len(a) > 0:
        c.append(a[0])
        a.remove(0)
    while len(b) > 0:
        c.append(b[0])
        b.remove(0)
    return c
        

def merge_sort(data):  
    print('Executing merge sort')    
    start_time = timeit.default_timer()
    a=[]
    b=[]
    atomic = False
    while atomic is False:
        if not isinstance(len(data)/2, int):
            atomic = True
            break
        for i in range (0, len(data)/2):
            a.append(data[i])
        for j in range((len(data)/2)+1, len(data)):
            b.append(data[j])
        a = merge_sort(a)
        b = merge_sort(b)
        data = merge(a,b)
    elapsed = timeit.default_timer() - start_time
    method_info = Sorting_Method('merge sort', elapsed)
    sorting_methods.methods.append(method_info)
    return method_info


def partition(data, low, high):

#    while True:
#        if low >= high:
#            break
#        else:
#            temp = data[low]
#            data[low] = data[high]
#            data[high] = temp
#            break
#    return low-1
    i = low-1
    pivot = data[high]
    for j in range(low, high):
        if data[j] <= pivot:
            i+=1
            data[i],data[j] = data[j], data[i]
    data[i+1],data[high] = data[high],data[i+1]
    return i+1
def quick_sort(data, left, right, flag):
    if flag == 0:
        print('Executing quick sort')   
    if left < right:
        pp = partition(data, left, right)
        quick_sort(data, left, pp-1,1)
        quick_sort(data, pp+1, right,1)
    return
def heap_sort(data):
    print('Executing heap sort')    
    start_time = timeit.default_timer()

    elapsed = timeit.default_timer() - start_time
    method_info = Sorting_Method('heap sort', elapsed)
    sorting_methods.methods.append(method_info)
    return method_info

def counting_sort(data):
    print('Executing counting sort')
    start_time = timeit.default_timer()

    elapsed = timeit.default_timer() - start_time
    return
            
    start_time = timeit.default_timer()

    elapsed = timeit.default_timer() - start_time
    method_info = Sorting_Method('counting sort', elapsed)
    sorting_methods.methods.append(method_info)
    return method_info
def bucket_sort(data):
    print('Executing bucket sort')
    start_time = timeit.default_timer()

    elapsed = timeit.default_timer() - start_time
    method_info = Sorting_Method('bucket sort', elapsed)
    sorting_methods.methods.append(method_info)
    return method_info

def bogo_sort(data):
    print('Executing bogo sort')
    start_time = timeit.default_timer()
    is_sorted = False
    while is_sorted is False:
        random.shuffle(data)
        if all(data[i]<= data[i+1] for i in range (len(data)-1)):
            is_sorted = True
    elapsed = timeit.default_timer() - start_time
    method_info = Sorting_Method('bogo sort', elapsed)
    sorting_methods.methods.append(method_info)
    return method_info



def main():
    data = parse()
    insertion_sort(data)
    bubble_sort(data)
    selection_sort(data)
    merge_sort(data)
    start_time = timeit.default_timer()
    quick_sort(data, 0, len(data)-1,1)
    elapsed = timeit.default_timer() - start_time
    method_info = Sorting_Method('quick sort', elapsed)
    sorting_methods.methods.append(method_info)
    #heap_sort(data)
    #counting_sort(data)
    #bucket_sort(data)
    #bogo_sort(data)
    low_cl = sorting_methods.methods[0]
    lower = low_cl.elapsed_time
    low_name = ''
    print('-----------------------------------------------------------------------------')
    for method in sorting_methods.methods:
        if method.elapsed_time >=1:
            print('{} completed in {} seconds'.format(method.name, method.elapsed_time))
        else:           
            print('{} completed in {} milliseconds'.format(method.name, round(method.elapsed_time*1000,5)))
        if method.elapsed_time < lower:
            lower = method.elapsed_time
            low_name = method.name 
    print('{} was the fastest!'.format(low_name))
if __name__ == "__main__":
    main()