# 1. Calculate how much memory was allocated for variables in previously developed programs in
# within the first three lessons. Analyze the result and identify programs with the most effective use
# memory.
#
# Note: For analysis, take any 1-3 of your programs or several code options for the same task.
# Insert the results of the analysis as comments to the code.


import sys
import random

####################################################################################################################
# Task5 Find the largest negative element in an array. Display its value and position in the array.
####################################################################################################################
SIZE = 1000
MIN_ITEM = -100
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
output = 'Amount of memory allocated for variables: '


def get_memory(dictionary):
    total = 0
    for key in dictionary.keys():
        value = dictionary[key]
        if key != '__len__' and type(value) == int or type(value) == float or type(value) == str or type(value) == set \
                or type(value) == tuple or type(value) == dictionary:
            total = total + sys.getsizeof(value)
    return total


initial = get_memory(locals())


# 1st solution:
def search_max_negative_1(list_init):
    list_negative = []
    for i in list_init:
        if i < 0:
            list_negative.append(i)
    min_item = abs(list_negative[0])
    for i in list_negative:
        if abs(i) < min_item:
            min_item = abs(i)
    return [- min_item, list_init.index(- min_item)], get_memory(locals())


eggs1 = search_max_negative_1(array)[1] + initial
print(f" 1st method: {output} {eggs1}")


# 2nd solution:
def search_max_negative_2(list_init):
    max_negative = float("-inf")

    for i in list_init:
        if i < 0:
            if i > max_negative:
                max_negative = i

    index_max_negative = list(i for i, e in enumerate(list_init) if e == max_negative)[0]

    return [max_negative, index_max_negative], get_memory(locals())


spam2 = search_max_negative_2(array)[1] + initial
print(f" 2nd method {output} {spam2}")


# 3rd solution:
def search_max_negative_3(list_init):
    array_negative = []
    for i in list_init:
        if i < 0:
            array_negative.append(i)
    max_negative = max(array_negative)
    index_max_negative = list(i for i, e in enumerate(list_init) if e == max_negative)[0]

    return [max_negative, index_max_negative], get_memory(locals())


eggs3 = search_max_negative_3(array)[1] + initial
print(f" 3rd method. {output} {eggs3}")
print(f' The most economical memory consumption: {min(spam2, eggs1, eggs3)}')


# Insert the results of the analysis as comments to the code.

# With SIZE = 1000, elements are generated from -100 to 100:
# 1st method. Amount of memory allocated for variables: 23368
# 2nd method. Amount of memory allocated for variables: 18548
# 3rd method. Amount of memory allocated for variables: 23396
# The most economical memory consumption: 18548, in the second method of solving the problem.

# With SIZE = 10, elements are generated from -3 to 10:
# 1st method. Amount of memory allocated for variables: 952
# 2nd method. Amount of memory allocated for variables: 884
# 3rd method. Amount of memory allocated for variables: 980
# The most economical memory consumption: 884, in the second method of solving the problem.
