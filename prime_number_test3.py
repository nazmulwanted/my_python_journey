import math

def is_prime(number):
    if number == 2:
        return True
    if number < 2:
        return False
    if (number % 2) == 0:
        return False
    prime = True
    m = math.sqrt(number)
    m = int(m) + 1
    for x in range(3,m,2):
        if number % x == 0:
            prime = False
            return prime
    return prime
while True:
    print("Please enter '0' two times to exit.")
    print("Please enter 2 numbers and first number should be less than second number.")
    print("")
    number1 = input("Input first number to determine: ")
    number1 = int(number1)
    number2 = input("Input second number to determine: ")
    number2 = int(number2)
    if number1 == 0 and number2 == 0:
        break
    if number1 > number2:
        print("First number is bigger. Please enter number again.")
        print("")
        continue
    for n in range(number1,number2+1):
        prime = is_prime(n)
        if prime is True:
            print(n)
