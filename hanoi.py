def move(f,t): #define move function
	print("Move disc from {} to {}!".format(f,t))
	
#move("A", "C") calls upon the function

#def moveVia(f, v, t): defines moveVia function
	#move(f, v) calls upon move function, move from step 1 (front position) to step 2 (out of 3)
	#at first, the destination is v
	#move(v, t) calls upon move function move from step 2 (helper position) to step 3 (target position)
	#now the origin is v, and the destination is t 
	
#moveVia("A", "B", "C") calls upon moveVia function




def hanoi(n, f, h, t): #define hanoi function
# n is the number of disks, f is the "front" position, h is the "helper",
#t is the "target" position
	if n == 0:
		pass #this is the BASE CASE!
	else:
		hanoi(n - 1, f, t, h) # function call WITHIN the function definition! (The recursion)
		move(f,t) #calls upon move function
		hanoi(n - 1, h, f, t) 
		
hanoi(4, "A", "B", "C") #calls
	

    