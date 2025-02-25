# Decorators - powerful tool that allows us to modify a function without changing that functions code.

import time


def outer_func(func):  # Outer function that takes input from a function as an argument
    def wrapper():  # Inner function that wraps the original function
        pre_execution_time_stamp = time.time()
        func()
        post_execution_time_stamp = time.time() - pre_execution_time_stamp
        print(f"{func.__name__} took {post_execution_time_stamp} seconds to execute")

    return wrapper  # return from within the function without execution


@outer_func
def print_ed():
    time.sleep(1)
    print("ed")


def log_function_characteristic(func):
    def wrapper(*args, **kwargs):
        print(f"Call func: {func.__name__}, the input arguments were: {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} resulted in {result} ")

    return wrapper


@log_function_characteristic
def subtraction(x, y):
    return x - y


subtraction(5,2)
print_ed()