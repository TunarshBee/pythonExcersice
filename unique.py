def uniq(list):
    """ Returns unique values of a list """
    u_list = []
    for item in list:
        if item not in u_list:
            u_list.append(item)
    # print(u_list)
    return u_list

uniq([2,4,1,2,5,7,6,3,2,9,8,4,2,4,6,2,3])

if __name__ == '__main__':
    import doctest
    doctest.testmod()