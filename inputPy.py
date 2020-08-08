#!/user/bin/env python3
name=input("Enter your name: ")
print("Hello "+name)
def toSec(h,m,s):
	return h*3600+m*60+s



cont= "y"
while cont=="y":
	hours = int(input("Enter the number of hours: "))
	minutes = int(input("Enter the number of minutes: "))
	seconds = int(input("Enter the number of seconds: "))
	print(toSec(hours,minutes,seconds))
	cont = input("Do you want to continue? [Press y to continue]")
	if cont !="y":
		print("Good bye!")
