''' 
Bubble Sort is a sorting algorithm which compares two adjacent elements and swap them if they are not in the right order. 

Pick one element, and push it to the right. (Either ascending or descending) * n times.

Introduced swapped variable for optimizing this algorithm.
'''

def optmized_bubble_Sort(array,l):
    for i in range(l):
      
        swapped = False		# for optimizing, if array is already sorted then break the main loop(i)
        for j in range(l - (i + 1)):

            if array[j] > array[j + 1]:

                # swap if greater is at the rear position
                (array[j], array[j + 1]) = (array[j + 1], array[j])
                swapped = True
                
        # if there is not a single swapping in the last iteration j loop
        if not swapped:
            break

    print(f'Bubble sorted array :: {array}')

arr = [-2, 45, 0, 11, -9]

optmized_bubble_Sort(arr,len(arr))

