"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(cooktime):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - cooktime

def preparation_time_in_minutes(number_of_layers):
    """Calculate the preperation time remaining in minutes.

    :param number_of_layers: int - number of layers to prepare in the lasagna.
    :return: int - total preparation time per layer (in minutes) multiplied 
    by 'EXPECTED_BAKE_TIME'.

    Function that takes the number of layers in the lasagna as an argument and returns 
    how many minutes are requied to prepare the lasagna.
    """
    return number_of_layers * PREPARATION_TIME

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the total elapsed time in minutes.

    :param number_of_layers: int - number of layers to prepare in the lasagna.
    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - total elapsed time (in minutes).

    Function that takes the number of layers in the lasagna and the elapsed bake time
    as arguments and returns the total elapsed time in preparing and cookinh the 
    lasagna.
    """
    ptim = preparation_time_in_minutes(number_of_layers)
    return elapsed_bake_time + ptim



