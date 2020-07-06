from lexer_module import get_lexeme_list, get_lexemes_list_with_string
from parser_module import parse

def test_parsing(file_name):
    parse(get_lexeme_list(file_name))


def __parse_file_output(file_name):
    return parse(get_lexeme_list(file_name))


def parse_file_string(file_string):
    return parse(get_lexemes_list_with_string(file_string))

def parse_file(file_name):
    return __parse_file_output(file_name)
