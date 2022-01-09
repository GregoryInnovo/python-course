import random


def run():
    number_random = random.randint(1, 100)
    user_number = int(input('Enter a number from 1 to 100: '))
    while user_number != number_random:
        if user_number < number_random:
            print("Choose a bigger number")
        else: 
            print("Choose a lower number")
        user_number = int(input('Choose another number: '))

    print("You win!")


    


if __name__ == '__main__':
    run()