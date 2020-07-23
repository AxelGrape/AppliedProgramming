from lexer_module import associate_token, get_last_lexeme
from symbol_table_module import SymbolTable

parse_ok = 1
line = 1
output_log = ""
symb_table = SymbolTable([])


def __lookahead(lexeme_list, str):
    return associate_token(lexeme_list[0]) if associate_token(lexeme_list[0]) ==  str else False



#Error handling
def __expected_error(expected, found, line):
    global output_log
    output_log += f'\n\tExpected: {expected} found: {found} on line {line}<br>'
    global parse_ok
    parse_ok = 0

def __name_found_error(id):
    global parse_ok
    parse_ok = 0
    global output_log
    output_log += f'\n\tSEMANTIC: ID already declared: {id}\n'

def __name_not_found_error(id):
    global parse_ok
    parse_ok = 0
    global output_log
    output_log += f'\n\Semantic: ID NOT declared: {id}\n'


def __match_next(lexeme_list, expected):
    current_token = associate_token(lexeme_list.pop(0))
    while (current_token is None):
        global line
        line +=1
        current_token = associate_token(lexeme_list.pop(0))

    if(current_token != expected):
        print(f'Syntax error: Expected: {expected} found: {get_last_lexeme()} on line {line}')
        __expected_error(expected, current_token, line)
    else:
        print(f'Expected: {expected} found: {current_token}')



# Grammar rules

def __parse_program_header(lexeme_list):
    __match_next(lexeme_list, "program")
    __match_next(lexeme_list, "ID")
    __match_next(lexeme_list, "(")
    __match_next(lexeme_list, "input")
    __match_next(lexeme_list, ",")
    __match_next(lexeme_list, "output")
    __match_next(lexeme_list, ")")
    __match_next(lexeme_list, ";")

# Var part of grammar

def __parse_var_part(lexeme_list):
    __match_next(lexeme_list, "var")
    __var_dec_list(lexeme_list)



def __var_dec_list(lexeme_list):
    __var_dec(lexeme_list)
    if(__lookahead(lexeme_list, "ID")):
        __var_dec_list(lexeme_list)

def __var_dec(lexeme_list):
    __id_list(lexeme_list)
    __match_next(lexeme_list, ":")
    __type(lexeme_list)
    __match_next(lexeme_list, ";")

def __id_list(lexeme_list):
    lexeme_value = __lookahead(lexeme_list, "ID") #To update last_lexeme, will make this better later
    global symb_table
    if(symb_table.in_symbol_table(get_last_lexeme())):
        __name_found_error(get_last_lexeme())
    elif(lexeme_value == "ID"):
        symb_table.add_to_table(get_last_lexeme(), "var")

    __match_next(lexeme_list, "ID")
    if(__lookahead(lexeme_list, ",")):
        __match_next(lexeme_list, ",")
        __id_list(lexeme_list)

def __type(lexeme_list):
    type = "undefined"
    if __lookahead(lexeme_list, "integer"):
         __match_next(lexeme_list, "integer")
         type = "integer"
    if __lookahead(lexeme_list, "real"):
         __match_next(lexeme_list, "real")
         type = "real"
    if __lookahead(lexeme_list, "boolean"):
         __match_next(lexeme_list, "boolean")
         type = "boolean"
    global symb_table
    symb_table.update_types(type)

# Stat part of grammar


def __parse_stat_part(lexeme_list):
    __match_next(lexeme_list, "begin")
    __stat_list(lexeme_list)
    __match_next(lexeme_list, "end")
    __match_next(lexeme_list, ".")

def __stat_list(lexeme_list):
    __stat(lexeme_list)
    if __lookahead(lexeme_list, ";"):
        __match_next(lexeme_list, ";")
        __stat_list(lexeme_list)

def __stat(lexeme_list):
    __assign_stat(lexeme_list)

def __assign_stat(lexeme_list):
    if __lookahead(lexeme_list, "ID"):
        global symb_table
        if symb_table.in_symbol_table(get_last_lexeme()):
            __match_next(lexeme_list,"ID")
        else:
            __name_not_found_error(get_last_lexeme())
            __match_next(lexeme_list,"ID")

    __match_next(lexeme_list,":=")
    __expr(lexeme_list)

def __expr(lexeme_list):
    __term(lexeme_list)
    if __lookahead(lexeme_list, "+"):
        __match_next(lexeme_list, "+")
        __expr(lexeme_list)
    if __lookahead(lexeme_list, "-"):
        __match_next(lexeme_list, "-")
        __expr(lexeme_list)

def __term(lexeme_list):
    __factor(lexeme_list)
    if __lookahead(lexeme_list, "*"):
        __match_next(lexeme_list, "*")
        __term(lexeme_list)
    if __lookahead(lexeme_list, "/"):
        __match_next(lexeme_list, "/")
        __term(lexeme_list)


def __factor(lexeme_list):
    if __lookahead(lexeme_list, "("):
        __match_next(lexeme_list, "(")
        __expr(lexeme_list)
        __match_next(lexeme_list, ")")
    __operand(lexeme_list)

def __operand(lexeme_list):
    if __lookahead(lexeme_list, "ID"):
        __match_next(lexeme_list, "ID")
    if __lookahead(lexeme_list, "Integer"):
        __match_next(lexeme_list, "Integer")

# Public

def __init_parser():
    global output_log
    output_log = ""
    global line
    line = 0
    global symb_table
    symb_table = SymbolTable([])

def parse(lexeme_list):
    __init_parser()
    __parse_program_header(lexeme_list)
    __parse_var_part(lexeme_list)
    __parse_stat_part(lexeme_list)
    global symb_table
    symb_table.print_symbol_table()

    print(f'Rest: {lexeme_list} ')

    global output_log
    if len(output_log) < 1:
        output_log += f'\n\tParse Completed<br>'
    else:
        output_log += f'\n\tParse failed! See output log'
    return output_log
