def find_largest_in_row_smallest_in_column_element_in_matrix(matrix):

    t=[]
 
    l=len(matrix)
    for i in range(l):
        c=0       
        max_val=max(matrix[i])
        index=matrix[i].index(max_val)
        print(max_val,index)

        for j in range(l):
            print(matrix[j][index],max_val)
            if matrix[j][index] >= max_val:
                c+=1

        if c==len(matrix[0]):
            return max_val

    return -1

print(find_largest_in_row_smallest_in_column_element_in_matrix([[1, 44],[2,66]]))