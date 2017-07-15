year=input("Please enter the year to check: ")
year=int(year)

if year % 4 != 0:
	print(year,"is not leap year!")
else:
	if year % 100 == 0:
		if year % 400==0:
			print(year,"is leap year!")
		else:
			print(year,"is not leap year!")
	else:
		print(year,"is leap year!")
print("Program terminated!")
