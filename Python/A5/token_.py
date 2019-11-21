from type import Type

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

    
