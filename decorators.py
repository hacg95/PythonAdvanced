#The upper function receives another function and the upper modifies the given function

def upper(func):
    def wrapper(name_given):
        return func(name_given).upper()
    return wrapper


@upper #This is sugar syntax for decorators
def message(name):
    return f'{name}, you got a message'


def run():
    print(message('Harold')) #The parameter of this function is the name_given in the wrapped function


if __name__ == '__main__':
    run()