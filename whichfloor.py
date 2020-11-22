maximum_stories = 25
userstring = input("On what floor of the building is your office? ")
usernum = int(userstring, 10)
    	
while usernum > maximum_stories:
	userstring = input("You entered: " + str(usernum) + " but there are only " + str(maximum_stories) + " floors in this building. ")
	usernum = int(userstring, 10)
    	
    	
    	
print("Congratulations! You work on: " + str(usernum))
