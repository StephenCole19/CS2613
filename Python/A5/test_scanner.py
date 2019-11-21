from Assignment5 import *
import pytest


def test_scan_currency():
    scanner=Scanner("100 100.00 100.42 -123.45")
    assert list(scanner) == [Token(Type.CURRENCY,10000),
                             Token(Type.CURRENCY,10000),
                             Token(Type.CURRENCY,10042),
                             Token(Type.CURRENCY,-12345)]

def test_scan_bad():
    scanner=Scanner("&crash")
    with pytest.raises(ValueError, match="&crash"):
        next(scanner)


def test_scan_transfer():
    scanner=Scanner('''TRANsfer transfer''')
    tokens = [Token(Type.TRANSFER,"TRANsfer"), Token(Type.TRANSFER,"transfer")]

    assert [token for token in scanner] == tokens

def test_scan_open():
    scanner=Scanner('''OPEN open''')
    tokens = [Token(Type.OPEN,"OPEN"), Token(Type.OPEN,"open")]

    assert [token for token in scanner] == tokens

def test_scan_balance():
    scanner=Scanner('''BaLaNcE balance BALANCE''')
    tokens = [Token(Type.BALANCE,"BaLaNcE"), Token(Type.BALANCE,"balance"), Token(Type.BALANCE,"BALANCE")]

    assert [token for token in scanner] == tokens

def test_scan_ident():
    scanner=Scanner("shares chequing")
    assert list(scanner) == [Token(Type.IDENT,"shares"),
                            Token(Type.IDENT,"chequing")]