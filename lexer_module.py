import re

keyword_list = ["program", "var", "integer", "real", "end", "begin", "input", "output"]


def get_lexeme_list(file_name):
     return __file_to_lexemes(__read_file(file_name))

def __read_file(file_name):
    contents = 0
    try:
        f = open(file_name,"r")
        contents = f.read()
        f.close()
    except IOError as e:
      print(e)
    except ValueError as e:
      print(e)
    except EOFError as e:
      print(e)
    except:
        print("Unkown error")
    finally:
        return contents

def __file_to_lexemes(file_string):
    lexeme_list = file_string.split(' ')
    lexeme_list.append('$')
    return lexeme_list

def __is_keyword(input):
    if input in keyword_list:
        return input
    else:
         return "ID"

def associate_token(input):

    identifier = re.search(r"^[^\d\W]\w*\Z", input)
    if identifier is not None:
        return __is_keyword(input)

    integer_number = re.search(r"^[-+]?([1-9]\d*|0)$", input)
    if integer_number is not None:
        return "Integer"

    real_number = re.search(r"[-+]?\d*\.\d+|\d+", input)
    if integer_number is not None:
        return "Real"


    return input
