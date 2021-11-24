#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sort_keys = list(sorted((a_dictionary.keys())))
    for k in sort_keys:
        print("{}: {}".format(k, a_dictionary[k]))
