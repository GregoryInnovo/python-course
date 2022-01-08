

def run():
    LIMIT = 1000000 # this is a constant

    counter = 0
    pow_2 = 2**counter
    while pow_2 < LIMIT:
        print(f'2 raised to {counter} is equal to: {pow_2}')
        counter += 1
        pow_2 = 2**counter



if __name__ == '__main__':
    run()