class ArithSeq:
    def __init__(self, start, inc, max):
        self.start=start
        self.inc=inc 
        self.max=max
        self.origin=start

    def __next__(self):
        if self.start > self.max:
            raise StopIteration
        elif self.start == self.origin:
            self.start += self.inc
            return self.origin

        num = self.start
        self.start += self.inc
        return num
        
    
    def __iter__(self):
        return self

def test_evens():
    assert [ x for x in ArithSeq(0,2,10) ] == [0,2,4,6,8,10]

def test_odds():
    assert [ x for x in ArithSeq(1,2,10) ] == [1,3,5,7,9]

def test_wow():
    assert [ x for x in ArithSeq(0,3,10) ] == [0,3,6,9]

def test_wow2():
    assert [ x for x in ArithSeq(5,5,20) ] == [5,10,15,20]
