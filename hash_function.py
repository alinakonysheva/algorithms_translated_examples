# Determining the number of distinct substrings using a hash function.
# Let a string S of length N be given, consisting only of small Latin letters.
# Required to find the number of different substrings in this string.

import hashlib


def count_substrings(s):
    # substrings will be stored in the set to avoid duplication
    h_subs = set()
    # iterate over all possible segments of the string
    for i in range(len(s)):
        for j in range(1, len(s) + 1):
            if s[i:j]:
                h_subs.add(hashlib.sha1(s[i:j].encode('utf-8')).hexdigest())
    # we return the value minus one, because the whole string also got into the set with a unique element
    return len(h_subs) - 1


s1 = input(f'Please enter a string consisting of Latin letters:   ')
print(f'Number of substrings in your string: {count_substrings(s1)}')
