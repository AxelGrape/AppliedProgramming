special_character_list = [",",".","-","+","*","/",";",":","=","(", ")"]

def __insert(source_str, insert_str, pos):
    return source_str[:pos]+insert_str+source_str[pos:]

def add_spaces(source_str):
    position = 0
    while(position < len(source_str)):
        global special_character_list
        if source_str[position] == ":" and source_str[position+1] == "=":
            position += 2
        else:
            if source_str[position] in special_character_list:
                source_str = __insert(source_str, " ", position+1) # blank after special character
                source_str = __insert(source_str, " ", position)  # blannk before special character
                position +=1
            position +=1
    return source_str
