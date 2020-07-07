import re

keyword_list = ["program", "var", "integer", "real", "end", "begin", "input", "output"]
last_lexeme = ""


# Public functions

#Pre: input is a single String
#Post: returns the token corresponding to the string
def associate_token(input):
    return __assoc_token(input)

#Pre: file_name is a filename
#Post: returns a list of lexemes if sucessful
def get_lexeme_list(file_name):
     return __file_to_lexemes(__read_file(file_name))

#Before real file handling, this is most likely temporary
def get_lexemes_list_with_string(file_string):
    return __file_to_lexemes(file_string)


def get_last_lexeme():
    global last_lexeme
    return last_lexeme

#Private functions

#Pre: file_name is a filename
#Post: Returns 0 if failed, String with the file contents if succesull
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

#Pre: file_string is a string
#Post: Splits the incoming string to lexemes and returns them in a list
def __file_to_lexemes(file_string):
    lexeme_list = re.split('\n| +', file_string)
    lexeme_list.append('$')
    return lexeme_list

def __is_keyword(input):
    if input in keyword_list:
        return input
    else:
         return "ID"

def __assoc_token(input):

    if input is None:
        return ''

    global last_lexeme
    last_lexeme = input

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
