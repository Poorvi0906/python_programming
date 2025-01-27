
t = n 
rev =0 
while n != 0:
	print("Value of n is",n)
	r = n % 10 
	print("Value of r is",r)
	rev =rev*10+r 
	print("Value of rev is",rev)
	n = n//10
	print ("Value of n is", n)
	print ("Reverse of a number",t,"is:", rev)
