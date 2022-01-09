import random

def generate_password():
    upper_case = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']

    lower_case = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']

    symbols = ['*', '+', '-', '/', '@', '_', '?', '!', '[', '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#', '"']

    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    characters = upper_case + lower_case + symbols + numbers

    password = []

    for i in range(15):
        random_char = random.choice(characters)
        password.append(random_char)

    password = ''.join(password)
    return password


def run():
    password = generate_password()
    print(f'Your new password is: {password}')



if __name__ == '__main__':
    run()