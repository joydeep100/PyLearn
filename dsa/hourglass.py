def Hourglass(arr):
    #   0         #this pattern is called as hour glass
    # 1 2 3
    #   9
    # want to find the maximum hourglass sum of 6 * 6 2D Array.
    # minimum hourglass sum = -9 * 7 = -63
    maxSum = -63
   
    for i in range(4):
        for j in range(4):
            # sum of top 3 elements
            top = sum(arr[i][j:j+3])  # will print 3 items i i'th array

            # mid element
            mid = arr[i+1][j+1]

            # # sum of bottom 3 elements
            bottom = sum(arr[i+2][j:j+3])
            
            # print(top,mid,bottom)
            hourglass = top + mid + bottom
            # print(hourglass)
            if hourglass > maxSum:
                maxSum = hourglass
                
    return maxSum

arr = [ [1,1,1,0,0,0],
        [1,7,1,0,0,3],
        [1,1,1,0,0,2],
        [1,1,1,0,0,0],
        [1,1,1,0,0,0],
        [1,1,1,0,0,0]]

maxsum = Hourglass(arr)
print(maxsum)

#upper 4 hour glass indexes for first line (we can have totally 16 hourglasses)
# a[0][0]+a[0][1]+a[0][2] +a[1][1] +a[2][0]+a[2][1]+a[2][2]
# a[0][1]+a[0][2]+a[0][3] +a[1][2] +a[2][1]+a[2][2]+a[2][3]
# a[0][2]+a[0][3]+a[0][4] +a[1][3] +a[2][2]+a[2][3]+a[2][4]
# a[0][3]+a[0][4]+a[0][5] +a[1][4] +a[2][3]+a[2][4]+a[2][5]
