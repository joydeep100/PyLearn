def compareFriends(frndsList):

    uniq_list=[]

    for item in frndsList:
        arr=item.split(',')
        if '{},{}'.format(arr[0], arr[1]) not in uniq_list and '{},{}'.format(arr[1], arr[0]) not in uniq_list:
            uniq_list.append(item)


    print(uniq_list)


compareFriends(['u1,u2','u3,u4','u2,u1','u2,u1'])
# o/p ['u1,u2', 'u3,u4']