import time


class FiboIter2():
    def __init__(self, max=13):
        self.max = max

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
                self.n1, self.n2 = self.n2, self.aux
                self.counter += 1
                return self.aux
            else:
                raise StopIteration


if __name__ == '__main__':
    fibonacci = FiboIter2(8)
    for element in fibonacci:
        print(element)
        time.sleep(1)
