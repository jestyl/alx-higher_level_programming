#!/usr/bin/python3
def uniq_add(my_list=[]):
    list_uniq = set(my_list)
    num = 0

    for i in list_uniq:
        num += i

    return (num)
