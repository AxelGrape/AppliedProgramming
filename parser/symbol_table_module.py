from symbol_module import Symbol

class SymbolTable:
    def __init__(self, symbol_list):
        self.symbol_list = symbol_list

    #Post: If variable doesn't exist in the symbol table it is added and retur True, else return False
    def add_to_table(self, name, role, type, size):
        if(self.in_symbol_table(name)):
            return False
        else:
            address = 0 if len(self.symbol_list) == 0 else  (self.symbol_list[-1].address + size)
            self.symbol_list.append(Symbol(name, role, type, size, address))
            return True

    #Pre: variable_name is a string with variable name, e.g. var A :integer, here A is variable_name
    #Post: Return if the variable is in the symbol table, true or false
    def in_symbol_table(self, variable_name):
        for s in self.symbol_list:
            if(s.name == variable_name):
                return True
            return False


    def print_symbol_table(self):
        for s in self.symbol_list:
            s.print_symbol()
