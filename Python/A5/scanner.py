from token_ import Token
from type import Type
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
            if(self.input[self.i].upper() in Type._value2member_map_):

                token = Token(Type[self.input[self.i].upper()], self.input[self.i])
                return token

            elif(currency.search(self.input[self.i]) is not None):

                token = Token(Type.CURRENCY, float(self.input[self.i])*100)
                self.i += 1

                return token
            elif(ident.search(self.input[self.i]) is None):

                token = Token(Type.IDENT, self.input[self.i])
                self.i += 1
                
                return token
            else:
                raise ValueError(self.input[self.i])
        else:
            raise StopIteration
