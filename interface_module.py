from lexer_module import get_lexeme_list
from parser_module import parse

def test_parsing(file_name):
    parse(get_lexeme_list(file_name))
