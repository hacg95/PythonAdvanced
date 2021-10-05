#Using generators function to create the Fibonacci Sequence

import time


def fibo_gen(max: int = None):
    n1, n2 = 0, 1
    counter = 0
    while True:
        if counter == 0:
            counter += 1
            yield n1
        elif counter == 1:
            counter += 1
            yield n2
        else:
            aux = n1 + n2
            if not max or aux<=max:
                n1, n2 = n2, aux
                counter += 1
                yield aux
            else:
                break


if __name__ == '__main__':
    max = int(input('Which is the max number you want: '))
    fibonacci = fibo_gen(max)
    for element in fibonacci:
        print(element)
        time.sleep(0.5)