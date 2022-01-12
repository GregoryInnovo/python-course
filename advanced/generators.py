import time

def fibo_gen(max: int):

    n1 = 0
    n2 = 1
    counter = 0

    while True:
        if counter == 0:
            counter += 1
            yield n1
        elif counter == 1:
            counter += 1
            yield n2
        else:
            if max < counter:
                break
            aux = n1 + n2
            n1, n2 = n2, aux
            counter += 1
            yield aux


if __name__ == "__main__":
    user_input = int(input("Write a number: "))
    fibonacci = fibo_gen(user_input)
    for element in fibonacci:
        print(element)
        time.sleep(1) # delay