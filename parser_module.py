from lexer_module import associate_token

parse_ok = 1

def __match_next(lexeme_list, expected):
    current_token = associate_token(lexeme_list.pop(0))
    if(current_token == expected):
        print(f'Expected: {expected} found: {current_token}')
    else:
        print(f'Syntax error: Expected: {expected} found: {current_token}')
        parse_ok = 0

def parse(lexeme_list):
    __parse_program_header(lexeme_list)

def __parse_program_header(lexeme_list):
    __match_next(lexeme_list, "program")
    __match_next(lexeme_list, "ID")
    __match_next(lexeme_list, "(")
    __match_next(lexeme_list, "input")
    __match_next(lexeme_list, ",")
    __match_next(lexeme_list, "output")
    __match_next(lexeme_list, ")")
    __match_next(lexeme_list, ";")
    return parse_ok
