#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    max_v = 0
    max_k = None
    for k, val in a_dictionary.items():
        if val > max_v:
            max_v = val
            max_k = k
    return max_k
