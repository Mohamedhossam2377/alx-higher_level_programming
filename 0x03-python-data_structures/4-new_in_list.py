#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    elif idx >= len(my_list):
        return my_list
    co_my_list = my_list()
    co_my_list[idx] = element
    return co_my_list
