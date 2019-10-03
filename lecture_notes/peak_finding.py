# Algorithm's Lecture 1
# https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/lecture-videos/lecture-1-algorithmic-thinking-peak-finding/

import math
import random
from prettytable import PrettyTable

def generate_1d_list(n=100):
    ''' Function to generate a unsorted list of n random numbers '''
    random_list = random.sample(range(n*10), n)
    return random_list

def print_1d_list(l, peak=None):
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

def generate_2d_list(n=10,m=10):
    ''' Generates a 2D list of n-rows * m-columns'''
    l = list()
    for i in range(n):
        row = random.sample(range(m*10), m)
        l.append(row)
    return l

def print_2d_list(l):
    ''' Prints a 2D list into a better readable format '''
    print('', end='\t')
    for i in range(len(l[0])):
        print(i, end="\t")
    print()
    for i, row in enumerate(l):
        print(i, end='\t')
        for n in row:
            print(n, end="\t")
        print()

def simple_2d_peak_finder(l):
    ''' Peak finding algorithm for a 2-D array of delta(n*m) complexity.
        Uses greedy search to find the peak.
    '''
    i, j = 0, 0
    flag = 1
    while flag:
        newi, newj = find_biggest_neighbour(l, i, j)
        if newi == i and newj == j:
            flag = 0
        else:
            i, j = newi, newj
    return i, j

def find_biggest_neighbour(l, i, j):
    ''' Finds the biggest neighbour for the cell l[i][j] '''
    n, m = len(l), len(l[0])
    maxi, maxj = i, j
    if i > 0:
        if l[maxi][maxj] < l[i-1][j]:
            maxi, maxj = i-1, j
    if j > 0:
        if l[maxi][maxj] < l[i][j-1]:
            maxi, maxj = i, j-1
    if i < n-1:
        if l[maxi][maxj] < l[i+1][j]:
            maxi, maxj = i+1, j
    if j < m-1:
        if l[maxi][maxj] < l[i][j+1]:
            maxi, maxj = i, j+1
    return maxi, maxj

def binary_2d_peak_finder(l, start=0, end=None):
    ''' Peak finding algorithm for a 2-D array of delta(n*log(m)) complexity '''
    if end is None:
        end = len(l)-1
    if start == end:
        maxi = find_max_element(l, start)
        return maxi, start
    else:
        mid = math.floor((start+end) / 2)
        maxi = find_max_element(l, mid)
        if mid != start and l[maxi][mid] < l[maxi][mid-1]:
            return binary_2d_peak_finder(l, start=start, end=mid-1)
        elif mid != end and l[maxi][mid] < l[maxi][mid+1]:
            return binary_2d_peak_finder(l, start=mid+1, end=end)
        else:
            return maxi, mid

def find_max_element(l, column):
    ''' Finds and returns the biggest element's position in the column '''
    maxi = 0
    for i in range(1, len(l[0])):
        if l[maxi][column] < l[i][column]:
            maxi = i
    return maxi

if __name__ == '__main__':
    for i in range(2):
        ll = generate_1d_list(50)
        print_1d_list(ll, peak=simple_1d_peak_finder(ll))
        print_1d_list(ll, peak=binary_1d_peak_finder(ll))
        l = generate_2d_list()
        print_2d_list(l)
        peak = simple_2d_peak_finder(l)
        print(peak)
        peak = binary_2d_peak_finder(l)
        print(peak)

