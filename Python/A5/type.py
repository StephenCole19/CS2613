from enum import Enum
import re

class Type(Enum):
    BALANCE = "BALANCE"
    CURRENCY = "CURRENCY"
    IDENT = "IDENT"
    OPEN = "OPEN"
    TRANSFER = "TRANSFER"

    @classmethod
    def check_value_exists(cls, value):
        return value in (val.value for val in cls.__members__.values())



class Token():
    def __init__(self, type_, value):
        self.type = type_
        self.value = value
    
    def __str__(self):
        if(self.type.name == "CURRENCY"):
            money = '{0}'.format(self.value)
            money = money[:-2] + '.' + money[-2:]
            return '[{0}: {1}]'.format(self.type.name, money)
        else:  
            return '[{0}: {1}]'.format(self.type.name, self.value)


    def __eq__(self, other):
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
    def __init__(self, input):
        self.input = input.split()
        self.i = 0

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        ident = re.compile(r'([^A-Za-z0-9_])', re.IGNORECASE) # Checks idents
        currency = re.compile(r'(.*[0-9].*)') # Checks currencies

        if(self.i < len(self.input)):
            if(Type.check_value_exists(self.input[self.i].upper())):

                token = Token(Type[self.input[self.i].upper()], self.input[self.i])
                self.i += 1

                return token
            elif(currency.search(self.input[self.i]) != None):

                token = Token(Type.CURRENCY, float(self.input[self.i])*100)
                self.i += 1

                return token
            elif(ident.search(self.input[self.i]) == None):

                token = Token(Type.IDENT, self.input[self.i])
                self.i += 1
                
                return token
            else:
                raise ValueError(self.input[self.i])
        else:
            raise StopIteration


