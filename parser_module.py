from lexer_module import associate_token

parse_ok = 1
output_log = "Start parse :"

def __match_next(lexeme_list, expected):
    current_token = associate_token(lexeme_list.pop(0))
    if(current_token != expected):
        global output_log
        output_log += f'\n\tExpected: {expected} found: {current_token}'
        #print(f'Syntax error: Expected: {expected} found: {current_token}')
        parse_ok = 0

def parse(lexeme_list):
    __parse_program_header(lexeme_list)
    return output_log

def __parse_program_header(lexeme_list):
    __match_next(lexeme_list, "program")
    __match_next(lexeme_list, "ID")
    __match_next(lexeme_list, "(")
    __match_next(lexeme_list, "input")
    __match_next(lexeme_list, ",")
    __match_next(lexeme_list, "output")
    __match_next(lexeme_list, ")")
    __match_next(lexeme_list, ";")
    print(output_log)
    return parse_ok
