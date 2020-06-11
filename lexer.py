import re

keyword_list = ["program", "var", "integer", "real", "end", "begin"]

def read_file(filename):
    contents = 0
    try:
        f = open(filename,"r")
        contents = f.read()
        contents = contents.split(' ')
        contents.append('$')
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

def is_keyword(input):
    if input in keyword_list:
        return input
    else:
        return "ID"

def get_token(input):

    identifier = re.compile(r"^[^\d\W]\w*\Z", re.UNICODE)
    if identifier is not None:
        return is_keyword(input)

    integer_number = re.compile(r"^[-+]?([1-9]\d*|0)$", re.UNICODE)
    if integer_number is not None:
        return "Integer"

    real_number = re.compile(r"[-+]?\d*\.\d+|\d+", re.UNICODE)
        if integer_number is not None:
            return "Real"


    return "hihi"
