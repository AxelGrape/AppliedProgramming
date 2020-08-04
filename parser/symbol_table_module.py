from symbol_module import Symbol

class SymbolTable:
    def __init__(self, symbol_list):
        self.symbol_list = symbol_list

    #Post: If variable doesn't exist in the symbol table it is added and retur True, else return False
    def add_to_table(self, name, role):
        if(self.in_symbol_table(name)):
            return False
        else:
            #address = 0 if len(self.symbol_list) == 0 else  (self.symbol_list[-1].address + 0)
            address = 0
            self.symbol_list.append(Symbol(name, role, "", 0, address))
            return True

    #Post: Return -1 if variable type isn't defined
    def __get_var_size(self, var_type):
        if(var_type == "integer"):
            return 4
        elif(var_type == "real"):
            return 8
        elif(var_type == "boolean"):
            return 4
        else:
            return -1


    #Pre: variable_name is a string with variable name, e.g. var A :integer, here A is variable_name
    #Post: Return if the variable is in the symbol table, true or false
    def in_symbol_table(self, variable_name):
        counter = 0
        print(f'length of symbol list = {len(self.symbol_list)}')
        while(counter < len(self.symbol_list)):
            print(self.symbol_list[counter].name)
            if(self.symbol_list[counter].name == variable_name):
                return True
            counter +=1

        self.print_symbol_table()
        return False


    #Pre: var_type is an variable typ, e.g. Integer, Real, Boolean
    def update_types(self, var_type):
        i = 0
        print(len(self.symbol_list))
        while i < len(self.symbol_list):
            if((len(self.symbol_list[i].type) < 1)):
                self.symbol_list[i].type = var_type
                self.symbol_list[i].size = "undefined" if self.__get_var_size(var_type) == -1 else self.__get_var_size(var_type)
                if i > 0 and self.symbol_list[i].address == 0:
                    print(f'address for i-1 = [{self.symbol_list[i-1].address} and size for i = [{self.symbol_list[i].size}]\n')
                    self.symbol_list[i].address += self.symbol_list[i].size + self.symbol_list[i-1].address
            i += 1


    def print_symbol_table(self):
        print(f'Name\tRole\tType\tSize\tAddress\n')
        for s in self.symbol_list:
            s.print_symbol()
