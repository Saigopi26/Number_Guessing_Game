import random
def guess(chances):

    print("Let's start the game!")
    num = random.randint(1, 100)
    count=1
    while chances>0:
        guess_num = int(input("Enter your choice number:"))
        if guess_num <= 0 or guess_num > 100:
            print("Please enter number between 1 and 100")
        else:
            if num==guess_num:
                return f"Congratulations! You guessed the correct number in {count} attempts."

            elif num<guess_num  and num in range(1,guess_num):
                print(f"Incorrect! The number is less than {guess_num}.")
            elif num>guess_num  and num not in range(1,guess_num):
                print(f"Incorrect! The number is greater than {guess_num}.")
        count+=1
        chances-=1

    return f"Game Over! The correct number was {num}"

print("Welcome to the Number Guessing Game! ")
print("Think of a number between 1 and 100.:")
print("Please select the difficulty level:")
print("1. Easy (10 chances)")
print("2. Medium (5 chances)")
print("3. Hard (3 chances)")

choice = int(input("Enter your difficulty choice (1/2/3): "))

if choice == 1:
    chances = 10
    print("You selected Easy level. You have 10 chances.")
elif choice == 2:
    chances = 5
    print("You selected Medium level. You have 5 chances.")
elif choice == 3:
    chances = 3
    print("You selected Hard level. You have 3 chances.")
else:
    print("Invalid choice")
    chances = 0

print(guess(chances))
