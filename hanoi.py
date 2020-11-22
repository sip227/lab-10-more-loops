def move(f,t): #define move function
	print("Move disc from {} to {}!".format(f,t))
	
#move("A", "C") calls upon the function

#def moveVia(f, v, t): defines moveVia function
	#move(f, v) calls upon move function
	#move(v, t) calls upon move function
#moveVia("A", "B", "C") calls upon moveVia function



def hanoi(n, f, h, t): #define hanoi function
# n is the number of disks, f is the "from" position, h is the "helper",
#t is the "target" position
	if n == 0:
		pass
	else:
		hanoi(n - 1, f, t, h)
		move(f,t) #calls upon move function
		hanoi(n - 1, h, f, t)
		
hanoi(4, "A", "B", "C") #calls
	

    