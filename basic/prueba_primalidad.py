def is_prime(num):
    counter = 0

    for i in range(1, num + 1):
        if i == 1 or i == num:
            continue
        if num % i == 0:
            counter += 1

    if counter == 0:
        return True
    else:
        return False
        


def run():
    number = int(input('Write a number: '))
    if is_prime(number):
        print("Is a prime number")
    else:
        print("Is not a prime number") 


if __name__ == '__main__':
    run()