def palindrome(word):
    word = word.replace(" ", "")
    word = word.lower()
    invert_word = word[::-1]
    if word == invert_word:
        return True
    else:
        return False


def run():
    word = input("Write a word: ")
    is_palindrome = palindrome(word)
    if is_palindrome == True:
        print("Is palindrome")
    else:
        print("Is not palindrome")


if __name__ == '__main__':
    run()