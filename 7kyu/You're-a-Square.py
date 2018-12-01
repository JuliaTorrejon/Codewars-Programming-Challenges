import math
def is_square(n):
    return n > -1 and math.sqrt(n) % 1 == 0;
    
# Notes: The method sqrt() returns the square root of x for x > 0. This function is not accessible directly, so we need to import math module and then we need to call this function using math static object.
