import random

attempts = 0

random_number = random.randint(1,1000)

while True:
    input_number = input("Guess a number between 1 and 1000: ")
    input_number = int(input_number)

    attempts += 1

    if input_number == random_number:
        print("Yes! Your guess is correct!")
        break
    if input_number > random_number:
        print("wrong! Please try to guess a smaller number.")
    else:
        print("Wrong! Please try to guess a larger number.")
print("You tried",attempts," times to guess the correct number.")
