class Symbol:
    def __init__(self, name, role, type, size, address):
        self.name = name
        self.role = role
        self.type = type
        self.size = size
        self.address = address

    def print_symbol(self):
        print(f'{self.name}\t{self.role}\t{self.type}\t{self.size}\t{self.address}\n')
