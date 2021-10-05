#This function uses typing for express the type of the values that comes from the user
#Like number has to be int, and the function is_prime return a boolean value

def is_prime(number: int) -> bool:
    #The function gets a number and divides that number between 1 and the number (i in range)
    #If the module of the number divided between any number of the range(i in this case) is zero
    #The function appends i to the list of divisors, and if the list divisors is equal 2, the number is prime
    divisors = [i for i in range(1,number+1) if number%i==0]
    if len(divisors) == 2:
        return f'{number} is a prime number'
    else:
        return f'{number} is not a prime number'


def run():
    number = int(input("Check if it is prime number: "))
    print(is_prime(number))


if __name__ == "__main__":
    run()