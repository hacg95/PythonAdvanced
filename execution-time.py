#This decorator will tell me how much time lasts a function to complete
from datetime import datetime

def execution_time(func):
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        time_elapse = final_time - initial_time
        print(f'The function lasts {time_elapse.total_seconds()} seconds to be completed')
    return wrapper


@execution_time
def random_func():
    for i in range(1000):
        for j in range(1000):
            i+j


@execution_time
def say_hello(name):
    print(f'Hello {name}')


def run():
    random_func()
    say_hello('Harold')


if __name__ == "__main__":
    run()