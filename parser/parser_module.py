from lexer_module import associate_token

parse_ok = 1
line = 1
output_log = ""

def __lookahead(lexeme_list, str):
    return True if associate_token(lexeme_list[0]) ==  str else False




def __match_next(lexeme_list, expected):
    current_token = associate_token(lexeme_list.pop(0))
    while (current_token is None):
        global line
        line +=1
        current_token = associate_token(lexeme_list.pop(0))

    if(current_token != expected):
        global output_log
        output_log += f'\n\tExpected: {expected} found: {current_token} on line {line}'
        print(f'Syntax error: Expected: {expected} found: {current_token} on line {line}')
        parse_ok = 0
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
    __match_next(lexeme_list, "ID")
    if(__lookahead(lexeme_list, ",")):
        __match_next(lexeme_list, ",")
        __id_list(lexeme_list)

def __type(lexeme_list):
    if __lookahead(lexeme_list, "integer"):
         __match_next(lexeme_list, "integer")
    if __lookahead(lexeme_list, "real"):
         __match_next(lexeme_list, "real")
    if __lookahead(lexeme_list, "boolean"):
         __match_next(lexeme_list, "boolean")


# Public

def parse(lexeme_list):
    __parse_program_header(lexeme_list)
    __parse_var_part(lexeme_list)
    if len(output_log) < 1:
        print("Parse Completed!")
    else:
        print("Parse failed! See output log")
    return output_log