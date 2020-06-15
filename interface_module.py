from lexer_module import get_lexeme_list
from parser_module import parse

def test_parsing(file_name):
    parse(get_lexeme_list(file_name))


def __parse_file_output(file_name):
    return parse(get_lexeme_list(file_name))

def parse_file(file_name):
    return __parse_file_output(file_name)
