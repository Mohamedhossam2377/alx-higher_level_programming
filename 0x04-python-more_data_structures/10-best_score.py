#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    max_v = 0
    max_k = None
    for key, value in a_dictionary.items():
        if value > max_v:
            max_v = value
            max_k = key
        return max_k
