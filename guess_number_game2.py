import random

attempts = 0

random_number = random.randint(1,1000)
low = 1
high = 1000
while True:
    print("Guess a number between 1 and 1000: ")
    input_number = (low + high) // 2
    print("My guess is: ", input_number)

    attempts += 1

    if input_number == random_number:
        print("Yes! Your guess is correct!")
        break
    if input_number > random_number:
        print("wrong! Please try to guess a smaller number.")
        high = input_number -1
    else:
        print("Wrong! Please try to guess a larger number.")
        low = input_number + 1
print("You tried",attempts," times to guess the correct number.")
