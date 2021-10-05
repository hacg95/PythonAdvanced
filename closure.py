#This is a closure, it has three rules
# 1. It has a nested function
# 2. It has to save a value from the superior scope
# 3. It has to return the nested function

def make_division_by(n): #Main function
    def divider(x): #Nested function
        return x/n #Saves the value of n, that comes from the superior scope
    return divider #Return the nested function


def run():
    division5 = make_division_by(5) # n=5 for the main function
    print(division5(125)) # x=125 for the nested function
    division7 = make_division_by(7)
    print(division7(63))


if __name__ == "__main__":
    run()