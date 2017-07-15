import math

def is_prime(number):
    if number == 2:
        return True
    if number < 2:
        return False
    if (number % 2) == 0:
        print(number,"is divisible by 2.")
        return False
    prime = True
    m = math.sqrt(number)
    m = int(m) + 1
    for x in range(3,m,2):
        if number % x == 0:
            print(number,"is divisible by",x)
            prime = False
            return prime
    return prime
while True:
    number = input("Input the number to determine (press '0' to exit): ")
    number = int(number)
    if number == 0:
        break
    prime = is_prime(number)
    if prime is True:
        print("The number is prime.")
    else:
        print("The number is not prime.")
