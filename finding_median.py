# An array of size 2m + 1, where m is a natural number, is filled randomly.
# Find the median in the array.
# The problem can be solved without sorting the original array.
# But if it's too complicated, then use a sorting method that was not covered in the lessons

import random
from collections import Counter

m = 5
array = [random.randint(0, 15) for _ in range(2 * m + 1)]

print(f'Input: {array}')
min_element = min(array)
# all values of the list elements are in the range:
size_sorted = max(array) - min_element
#  an array of zeros with a size in the range of scatter of values
sort = [i * 0 for i in range(size_sorted + 1)]
# a dictionary in which we count the number of occurrences of list elements
value_weight = Counter(array)
# sort the resulting pairs (values - number of occurrences) by the value of the element of the original array
for key, value in value_weight.items():
    # for this, we normalize to the minimum element in order to fill the array starting from the zero index
    index = key - min_element
    sort[index] = (key, value)
# the array turned out with residual zeros, we remove the zeros:
sort = [i for i in sort if i != 0]

n = 0
median = array[0]
# in the sorted list of tuples, we calculate the index of the tuple where the median value lies:
for tuple_ in sort:
    n = n + tuple_[1]
    if n >= m:
        median = tuple_[0]
        break
print(f'Median of the array: {median}')
