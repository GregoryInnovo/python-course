def make_repeater_of(n):
    def repeater(string):
        assert type(string) == str, "Only use strings"
        return string * n
    return repeater


def make_division_by(divider):
    def division(dividend):
        return dividend / divider
    return division


def mayus(func):
    def wrapper(text):
        return func(text).upper()
    return wrapper


@mayus
def message(name):
    return f'{name}, you received a message!'


print(message('Greg'))

def run():
    division_by_3 = make_division_by(3)
    print(division_by_3(18))

    division_by_5 = make_division_by(5)
    print(division_by_5(100))
    
    division_by_18 = make_division_by(18)
    print(division_by_18(54))
    # repeat_5 = make_repeater_of(5)
    # repeat_10 = make_repeater_of(10)
    # print(repeat_5("Hey pal"))
    # print(repeat_10("Foodhy"))




if __name__ == "__main__":
    run()