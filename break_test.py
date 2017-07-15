while True:
  n = input("Enter a number: [press '0' to exit]: ")
  n = int(n)
  if n<0:
    print("You entered negative number. Please enter positive number.")
    continue
  if n==0:
    break
  print("Square of",n,"is",n*n)


