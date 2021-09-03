import random

number_of_times = 0
condition = True

while condition:

    for everything in range(3):
        
        first_generated_number = random.randint(10,99)
        second_generated_number = random.randint(10,99)
        number_of_times=number_of_times+1

        print(f"What is {first_generated_number} + {second_generated_number} ?")

        
        user_input = int(input("Your answer=> "))
        result = first_generated_number + second_generated_number

        if user_input != result:
            print("Incorrect. The expected answer is " + str(result))
            number_of_times = 0
            

        else:
            print("Correct! You have gotten " + str(number_of_times) + " in a row")
            if number_of_times == 3:
                print("Congratulations! You mastered addition")
                condition = False
        if condition == False:
            break