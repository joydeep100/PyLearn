def stockBuySell(price,len):
	if len == 1:
		return

	i=0
	while(i < len-1):

		# finding local minimal
		while((i < len -1) and (price[i+1] <= price[i])):	
			
		#the two while loops assist in outer while loop to get over so it's O(N)

			# i can go till len -1 
			i+=1

		if i == len - 1:   #Can't buy
			break

		loc_min = i
		i+=1

		#finding local maxima
		while((i < len) and  (price[i] >= price[i-1])):
			# i has to go till the end, i.e. len
			i+=1

		loc_max = i - 1

		print(f'buy at {loc_min} and sell at {loc_max}')


price = [100, 180, 260, 310, 40, 535, 695] 
n = len(price) 
  
# Function call 
stockBuySell(price, n)