def run():
    # for counter in range(1000):
    #     if counter % 2 != 0:
    #         continue # if the condition is True the loop  skip line 5
    #     print(counter)

    # for i in range(10000):
    #     print(i)
    #     if i == 5672:
    #         break # exit from loop if condition is True
    
    text = input('Write a text: ')

    for letter in text:
        if letter == 'o':
            break # exit from loop if condition is True
        print(letter)


if __name__ == '__main__':
    run()