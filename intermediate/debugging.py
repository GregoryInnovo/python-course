def divisor(num):
    try: 
        if num < 0:
            raise ValueError("Only natural numbers are allowed")
        divisors = []
        for i in range(1, num + 1 ):
            if num % i == 0:
                divisors.append(i)
        
        return divisors
    except ValueError as e:
        print(e)
        return False


def run():
    try:
        num = int(input("Write a number: "))
        print(divisor(num))
        print("program exit")
       
    except ValueError:
        print("Only numbers are allowed, please try again!")


if __name__ == '__main__':
    run()