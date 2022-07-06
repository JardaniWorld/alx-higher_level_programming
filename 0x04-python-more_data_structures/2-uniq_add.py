#!/usr/bin/python3
def uniq_add(my_list=[]):
    num_set = {x for x in my_list}
    add = 0
    for element in num_set:
        add += element
    return add
