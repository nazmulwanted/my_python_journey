year=input("Enter a year to check: ")
year=int(year)

if year % 100 != 0 and year % 4 == 0:
  print("Entered year is a leap year!")
elif year % 100 == 0 and year % 400 == 0:
  print("Enteted year is a leap year!")
else:
  print("Entered year is not a leap year!")

print("Program terminated!")
