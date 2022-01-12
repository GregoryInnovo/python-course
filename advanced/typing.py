def is_palindrome(string: str) -> bool:
    string = string.replace(" ", "").lower()

    return string == string[::-1]


def is_prime(number: int) -> bool:
    list_number = [i for i  in range(2, number + 1) if number % i == 0]
    result = len(list_number)

    if result == 1:
        return True
    else:
        return False


def run():
    print(is_palindrome(1000))
    # user_input = input("Please enter number: ")
    # user_number: int = int(user_input)

    # result = is_prime(user_number)

    # if result:
    #     print("Is a prime number")
    # else:
    #     print("Is not a prime number")


if __name__ == "__main__":
    run()