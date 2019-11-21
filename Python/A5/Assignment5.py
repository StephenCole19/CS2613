from enum import Enum
import re

class Type(Enum):
    '''Type class that enumerates the values used in ledger'''
    BALANCE = "BALANCE"
    CURRENCY = "CURRENCY"
    IDENT = "IDENT"
    OPEN = "OPEN"
    TRANSFER = "TRANSFER"

    @classmethod
    def check_value_exists(cls, value):
        '''Used in ledger to check if a value in type exists'''
        return value in (val.value for val in cls.__members__.values())



class Token():
    def __init__(self, type_, value):
        '''Token constructor'''
        self.type = type_
        self.value = value
    
    def __str__(self):
        '''To string method for Token'''
        if(self.type.name == "CURRENCY"):
            money = '{0}'.format(self.value)
            money = money[:-2] + '.' + money[-2:]
            return '[{0}: {1}]'.format(self.type.name, money)
        else:  
            return '[{0}: {1}]'.format(self.type.name, self.value)


    def __eq__(self, other):
        '''Checks equality'''
        if(self.type.name == other.type.name and self.value == other.value):
            return True
        elif(self.type.name == "OPEN" or self.type.name == "BALANCE"):
            if(self.value.lower() == other.value.lower()):
                return True
            else:
                return False
        else:
            return False

import re

class Scanner:
    '''Scanner class is used to scan in data '''

    def __init__(self, data):
        '''Scanner constructor'''
        self.data = data.split()
        self.i = 0

    def __iter__(self):
        '''Scanner iterator'''
        self.i = 0
        return self

    def __next__(self):
        '''Used to move to next value in the Scanner'''
        ident = re.compile(r'([^A-Za-z0-9_])', re.IGNORECASE) # Checks idents
        currency = re.compile(r'(.*[0-9].*)') # Checks currencies

        if(self.i < len(self.data)):
            if(Type.check_value_exists(self.data[self.i].upper())):

                token = Token(Type[self.data[self.i].upper()], self.data[self.i])
                self.i += 1

                return token
            elif(currency.search(self.data[self.i]) != None):

                token = Token(Type.CURRENCY, float(self.data[self.i])*100)
                self.i += 1

                return token
            elif(ident.search(self.data[self.i]) == None):

                token = Token(Type.IDENT, self.data[self.i])
                self.i += 1
                
                return token
            else:
                raise ValueError(self.data[self.i])
        else:
            raise StopIteration

def ledger(input):
    """This function simulates a banking ledger used to do simple banking functions based on an input"""

    if(len(input) > 0): # if input is not empty fill scanner
        scan = Scanner(input)
    else: # else make null scanner
        scan = None 

    size = 0
    m = len(input.split())
    map = {}
    accounts = []

    if(scan == None): # if scan is empty return an empty scanner
        return []
    else:
        tokens = list(scan) # Tokenize input
        index = 0 

        while(index < m):
            signal = tokens[index]

            # Used for balances
            if signal.type == Type.BALANCE:
                identifier = tokens[index+1]

                if(identifier.value in [account['name'] for account in accounts]): # checks if there is an account
                    yield (identifier.value, accounts[map[identifier.value]]["balance"])
                else:
                    yield (identifier.value, 0)
                index += 2  # skip because the account doesn't exist

            # Used for open
            elif signal.type == Type.OPEN:
                ident = tokens[index+1]
                balance = tokens[index+2]
                accounts.append({"name": ident.value, "balance": int(balance.value)})
                map[ident.value] = size

                size += 1 # create new account
                index += 3

            #Used for transfer
            elif signal.type == Type.TRANSFER:
                fromAccounts = tokens[index+1]
                toAccounts = tokens[index+2]
                amount = tokens[index+3] 

                # changes the balance
                accounts[map[fromAccounts.value]]["balance"] -= amount.value
                accounts[map[toAccounts.value]]["balance"] += amount.value

                index += 4
            else:
                break