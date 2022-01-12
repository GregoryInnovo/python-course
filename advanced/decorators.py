from datetime import datetime

def execution_time(func):
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        func(*args, **kwargs) # the solution to not or multiple arguments
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print(f'Passed execution time: {time_elapsed.total_seconds()} seconds')
    return wrapper


@execution_time
def random_func():
    for _ in range(1 , 100000000): # we dont care about the var in the loops _
        pass


@execution_time
def sum(a: int, b: int) -> int:
    return a + b


@execution_time
def hey(name='Greg'):
    print(f'Hey {name}')


random_func()
sum(5, 5)
hey()