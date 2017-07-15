terminate_program = False

while not terminate_program:
  n1 = input("Enter first number: ")
  n1 = int(n1)
  n2 = input("Enter second number: ")
  n2 = int(n2)

  while True:
    operation = input("Enter add/sub or quit to exit: ")

    if operation == "quit":
      terminate_program= True
      break
    if operation not in ["add","sub"]:
      print("Unknown operation.")
      continue
    if operation == "add":
      print("Result is: ",n1+n2)
      break
    if operation == "sub":
      print("Result is: ",n1-n2)
      break
