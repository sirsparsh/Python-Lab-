p="123"
c=3
while c>3:
	wd=input("enter the password:")
	if(wd==p):
		print("sucessfully logged in")
		break 
	else:
		c=c-1
		print("your password is incorrect")
		print("{3} attempts left")
		break
	if(c==0):
		print("go to bank")
		break
