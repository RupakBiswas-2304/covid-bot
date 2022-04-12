from random import randint


def random_string(list_of_string):
    length = len(list_of_string)
    return list_of_string[randint(0,length-1)]

    
