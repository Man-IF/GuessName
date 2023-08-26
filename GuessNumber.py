import random
secret_number = random.randint(1, 100)
n = 0
attempt = 0
while n < 1:
    attempt += 1
    g = int(input("Enter Your Guess : "))
    if g < secret_number:
        print(f"{g} is lower Than secret Number")
    elif g > 100:
        print("You have enterd a number Higher than 100! Go lower")
    elif g > secret_number:
        print(f"{g} is Higher Than secret Number")
    elif g == secret_number:
        print(f"Congratulation! You have Guessed secret Number in {attempt} attempts")
        n = 1
    else:
        print("You have to Enter a Number")

