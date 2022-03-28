# 1. Bubble sort a one-dimensional integer array in descending order,
# given by random numbers in the range [-100; 100).
# Display the original and sorted arrays.
# Sorting must be implemented as a function.
# Refine the algorithm if possible (make it smarter).

# Let's check for cleverness, compare the modified implementation of the algorithm from the lecture (version 1)
# with a slightly modified version 2 on two indicators, a little on memory (only memory consumption for variables)
# and on time

import cProfile
import random
import sys

array1 = [random.randint(-100, 100) for _ in range(10)]
print(f'Input: {array1}')
print('#' * 50)
array2 = array1.copy()


def get_memory(dictionary):
    total = 0
    for key in dictionary.keys():
        value = dictionary[key]
        if key != '__len__' and type(value) == int or type(value) == float or type(value) == str or type(
                value) == list or type(
            value) == set or type(value) == tuple or type(value) == dictionary:
            total = total + sys.getsizeof(value)
    return total


initial = get_memory(locals())


def bubble1(lst):
    n = 1
    permutation = True
    while n < len(lst) and permutation:
        permutation = False
        for i in range(len(lst) - n):
            if lst[i] < lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                permutation = True
        n += 1
    sorted_li = lst
    return f'{sorted_li}, memory: {get_memory(locals())}'


print('1st sort option: ')
print(bubble1(array1))
print('#' * 55)


def bubble2(lst):
    for n in range(len(lst) - 1, 0, -1):
        for i in range(n):
            if lst[i] < lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
    sorted_li = lst
    return f'{sorted_li}, memory: {get_memory(locals())}'


print('2nd sort option: ')
print(bubble2(array2))
print('#' * 55)

cProfile.run('bubble1(array1)')
cProfile.run('bubble2(array2)')

# The evaluation of "smartness":
# A noticeable difference in time starts with the length of the input array order 10**3:
# First option: 14 function calls in 0.001 seconds, two orders of magnitude faster,
# but memory occupied is slightly more than 18104
# Second option: 12 function calls in 0.079 seconds, slower, more memory efficient memory 16180
# Giant time difference with the length of the input array order 10**4:
# First option: 14 function calls in 0.003 seconds, 4 orders of magnitude faster than the second option
# Second option: 12 function calls in 7.664 seconds
