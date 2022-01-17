def divisor(num):
    divisors = []
    for i in range(1, num + 1 ):
        if num % i == 0:
            divisors.append(i)
    
    return divisors


def run():
    num = input("Write a number: ")
    assert num.isnumeric(), "Only numbers are allowed, please try again!"
    assert int(num) > 0 , "Only natural numbers are allowed"
    print(divisor(int(num)))
    print("program exit")
       

if __name__ == '__main__':
    run()