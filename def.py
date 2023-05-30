#!/usr/bin/python3
def print_list_integer(my_list=(1,2,3,4,4,1,5,7)):
    newset = set(my_list)
    print(sum(newset))
    print(newset.pop())
    print(newset.discard(5))
    print(newset)
print_list_integer()
