from powergen import *

def test_powergen_list():
    gen = powergen(3)
    threes = [next(gen) for n in range(9)]
    assert(threes == [1, 3, 9, 27, 81, 243, 729, 2187, 6561])