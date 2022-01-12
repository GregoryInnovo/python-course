import time

class FiboIter():

    def __init__(self, max=None):
        self.max = max


    # define elements to use in the iterator
    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.counter = 0
        return self


    def __next__(self):
        if self.counter == 0:
            self.counter += 1
            return self.n1
        elif self.counter == 1: 
            self.counter += 1
            return self.n2
        else:
            if self.counter <= self.max:
                self.aux = self.n1 + self.n2
                # self.n1 = self.n2
                # self.n2 = self.aux
                self.n1, self.n2 = self.n2, self.aux # swaping
                self.counter += 1
                return self.aux
            else:
                raise StopIteration


if __name__ == "__main__":
    user_input = int(input("Write a number: "))
    fibonacci = FiboIter(user_input)
    for element in fibonacci:
        print(element)
        time.sleep(1) # delay