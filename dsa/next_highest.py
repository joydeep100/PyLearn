def second_highest_num(n):
    num_list = list(map(int,n))
    l=len(num_list)
    i = 1
    j = i+1
    flag=0

    while(i < l):
        if num_list[-i] > num_list[-j]:
            num_list[-i],num_list[-j] = num_list[-j],num_list[-i]
            flag = 1
        else:
            j+=1    
            i+=1
        if (flag):
            break

    slice = num_list[:-j:-1][::-1]

    print(num_list[:-j+1]+sorted(slice))

n = '516'
second_highest_num(n)