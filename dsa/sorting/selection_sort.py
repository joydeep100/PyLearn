''' 
In Selection sort, we go from starting index to the end
At each step we swap the i'th item with the minimum value in the remaining loop (n - i ; n = size)
'''
def selection_sort(arr,l):
    
    for i in range(l):
            
        min_index = arr.index(min(arr[i:l]))    #Can do a for loop also for this part
        
        if min_index != i:  #Nice to have
            arr[i],arr[min_index] = arr[min_index],arr[i]

    print(arr)

arr = [1,-3,-4,2,-99]
selection_sort(arr,len(arr))