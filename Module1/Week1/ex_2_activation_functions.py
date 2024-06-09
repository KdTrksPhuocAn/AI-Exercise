# Write a function to simulate three activation functions.

import math


def is_number(x):
    try:
        float(x)
        return True
    except ValueError:
        return False
    return True


def evaluate_activation_function(x, activation_function_name):
    if not is_number(x):
        print('x must be a number')
        return
    x = float(x)
    if activation_function_name not in ['sigmoid', 'relu', 'elu']:
        print(f'{activation_function_name} is not supported')
        return

    alpha = 0.01
    if activation_function_name == 'sigmoid':
        f_x = 1 / (1 + math.exp(-x))
    elif activation_function_name == 'relu':
        f_x = max(0, x)
    elif activation_function_name == 'elu':
        if x <= 0:
            f_x = alpha * (math.exp(x) - 1)
        else:
            f_x = x

    print(f'{activation_function_name}: f({x}) = {f_x}')


x = input('Enter a value for x: ')
if is_number(x):
    activation_function_name = input(
        'Enter the activation function name (sigmoid, relu, elu): ')
    evaluate_activation_function(x, activation_function_name)
else:
    print('x must be a number')
