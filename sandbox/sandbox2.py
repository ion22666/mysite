def find_var_name(var_name):
    for objname, oid in globals().items():
        if oid is var_name:
            return True
    
    return False

class Class1:

    def __init__(self,atr1):
        self.atr1 = atr1
        self.print_name()
        
    def print_name(self):
        print(find_var_name(str(self)))

test = Class1("abc")
