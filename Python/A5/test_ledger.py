from Assignment5 import *

def test_empty():
    assert list(ledger("")) == []

def test_balance():
    assert list(ledger('''
                    balance cash
                    balance stock
                    ''')) == [("cash",0),("stock",0)]

def test_open():
    assert list(ledger('''
                        open cash 100
                        balance cash
    ''')) == [("cash",10000)]
    
def test_transfer_open():
    assert list(ledger('''
                        open cash 100
                        open expenses 0
                        transfer cash expenses 50
                        balance cash
                        balance expenses
                        ''')) == [("cash",5000),("expenses",5000)]