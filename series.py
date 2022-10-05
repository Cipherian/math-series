# Create a function called fibonacci. The function should have one parameter n. The function should return the nth value in the fibonacci series. You may implement the function using recursion or iteration. If you are feeling particularly frisky, do both as separate functions.

#thanks grepper
def fibonacci(number):
    """
    This function has the parameter number.
    The function will return the nth value in the fibonacci series using recursion.
    """
    if number == 0 or number == 1:
        return number
    return fibonacci(number - 1) + fibonacci(number - 2)

#https://www.geeksforgeeks.org/lucas-numbers/
def lucas(number):
    """
    This function has the parameter n.
    The function will return the nth value in the lucas series using recursion.
    """
    if number == 0:
        return 2
    if number == 1:
        return 1

    return lucas(number - 1) + lucas(number - 2)

""" 
    Iterative way of generating lucas series
    
def lucas(n) :
 
    # declaring base values
    # for positions 0 and 1
    a = 2
    b = 1
     
    if (n == 0) :
        return a
  
    # generating number
    for i in range(2, n + 1) :
        c = a + b
        a = b
        b = c
     
    return b
    """

def sum_series(number, x = 0, y = 1):
    """
    This function has the required parameter(number).
    There are two optional parameters x and y
    if x is 0 and y = 1 then it will return the fibonacci number
    Likewise if x is 2 and y is 1 then it will return the lucas number
    """

    if x == 0 and y == 1:
        return fibonacci(number)
    elif x == 2 and y == 1:
        return lucas(number)
    else:
        return 'This is neither a fibonacci nor a lucas series'
