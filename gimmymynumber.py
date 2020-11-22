userstring = input("Gimme a number that is greater than 100... ")
usernum = int(userstring, 10)
        
while usernum < 100: 
	userstring = input(str(usernum) + " is less than 100. Please try again. ")
	usernum = int(userstring, 10)
        
print("Congratulations! " + str(usernum) + " is greater than 100! Great Job!")

    