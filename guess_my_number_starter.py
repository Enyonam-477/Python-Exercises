#getting random library
import random
generated_random_number = random.randint(1,99)

print("I am thinking of a number between 1 and 99")
user_input = input("Enter a guess :  " )

# for user input validation

while True:
    if user_input.isdigit():
        user_input=int(user_input)
# comparing user's input to randomly generated number
        if user_input  == generated_random_number :
            print("Congrats!...The number was " + str(generated_random_number))
            break

        elif user_input < generated_random_number:
            print("Your guess is too low")
            user_input = input("Enter a new guess :  " )

        else:
            print("Your guess is too high")
            user_input = input("Enter a new guess :  " )

# (in case user does not enter an integer, another chance is given instead of blowing the program up)
    else:
        print("Enter a valid number please!")
        user_input = input("Enter a new guess :  ")

