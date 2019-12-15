class FizzBuzz:
    def __init__(self, max=100):
        self.n=1; self.max=max

    def __next__(self):
        if self.n > self.max:
            raise StopIteration

        num = self.n

        if (((num % 5) == 0) and ((num % 3) == 0)):
            self.n += 1
            return "FizzBuzz"
        elif((num % 5) == 0):
            self.n += 1
            return "Buzz"
        elif((num % 3) == 0):
            self.n += 1
            return "Fizz"
        else:
            self.n += 1
            return num
    
    def __iter__(self):
        return self


def test_fizzbuzz_next():
    fb=FizzBuzz(15)
    assert (list(fb) == [1,2,'Fizz',4,'Buzz','Fizz',7,8,'Fizz',
                        'Buzz', 11, 'Fizz', 13, 14,'FizzBuzz'])