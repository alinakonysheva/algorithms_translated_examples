# 2. Sort in ascending order using the merge method a one-dimensional real array,
# given by random numbers on the interval [0; fifty).
# Display the original and sorted arrays.

import random

array = [random.randint(0, 50) for _ in range(8)]
print(f'Input: {array}')


def merge_sort(lst):
    # the first step of the merge sort algorithm is to divide the array into arrays of lengths = 1:
    if len(lst) > 1:
        # so as long as there are pieces longer than one: divide in half and form lists of halves
        middle = len(lst) // 2
        lefthalf = lst[:middle]
        righthalf = lst[middle:]
        # which we divide in half again
        merge_sort(lefthalf)
        merge_sort(righthalf)
        # second step of the merge sort algorithm: compare nearest arrays and write to the resulting array
        # counter to iterate over the left half
        i = 0
        # counter to iterate over the right half
        j = 0
        # counter of places in the final array
        f = 0
        # as long as we don't go beyond array lengths:
        while i < len(lefthalf) and j < len(righthalf):
            # compare element by element:
            if lefthalf[i] < righthalf[j]:
                # and write the smaller element to the final array first:
                lst[f] = lefthalf[i]
                i = i + 1
            else:
                lst[f] = righthalf[j]
                j = j + 1
            f = f + 1
        # add the remaining large ones to the final array:
        while i < len(lefthalf):
            lst[f] = lefthalf[i]
            i = i + 1
            f = f + 1

        while j < len(righthalf):
            lst[f] = righthalf[j]
            j = j + 1
            f = f + 1
    return lst


print(f'Sorted array: {merge_sort(array)}')
