# Algorithm's Lecture 1
# https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/lecture-videos/lecture-1-algorithmic-thinking-peak-finding/


import math
import random
from prettytable import PrettyTable

def generate_list(n=100):
    ''' Function to generate a unsorted list of n random numbers '''
    random_list = random.sample(range(n*10), n)
    return random_list

def print_list(l, peak=None):
    ''' Prints the unsorted list "l" into a readable format and points out the peak. '''
    if peak is not None:
        x = PrettyTable(["Index", "Number", "Peak"])
        for i, n in enumerate(l):
            if i == peak:
                x.add_row([i, n, 'Peak'])
            else:
                x.add_row([i, n, ''])
    else:
        x = PrettyTable(["Index", "Number"])
        for i, n in enumerate(l):
            x.add_row([i, n])
    print(x)

def simple_1d_peak_finder(l):
    ''' Peak finding algorithm for a 1-D array of delta(n) complexity '''
    list_length = len(l)
    for i, n in enumerate(l):
        if i == 0:
            if n >= l[1]:
                return i
        elif i == list_length-1:
            if n >= l[list_length-2]:
                return i
        else:
            if n >= l[i+1] and n >= l[i-1]:
                return i

def binary_1d_peak_finder(l, start=0, end=None):
    ''' Peak finding algorithm for a 1-D array of delta(log(n)) complexity '''
    if end is None:
        end = len(l)-1
    if start == end:
        return start
    else:
        mid = math.floor((start + end) / 2)
        if mid != start and l[mid] < l[mid-1]:
            return binary_1d_peak_finder(l, start=start, end=mid-1)
        elif mid != end and l[mid] < l[mid+1]:
            return binary_1d_peak_finder(l, start=mid+1, end=end)
        else:
            return mid

if __name__ == '__main__':
    for i in range(10):
        ll = generate_list(50)
        print_list(ll, peak=binary_1d_peak_finder(ll))

