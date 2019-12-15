def arith_seq(start,inc,max):
    return [x for x in range(start, max +1) if ((x - start) % inc == 0)]

def test_evens():
    assert arith_seq(0,2,10) == [0,2,4,6,8,10]

def test_odds():
    assert arith_seq(1,2,10) == [1,3,5,7,9]

def test_wow():
    assert arith_seq(5,2,10) == [5,7,9]