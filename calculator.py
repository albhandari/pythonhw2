def calculator(number1, number2, operator):
    """
    Perform arithemtic of two numbers

    This function basically takes in three inputs, where
    two are numbers and the other is the arithemtic sign
    that is performed between the two numbers

    Parameters
    ----------
    number1
        First integer or float 
    number2
        Second integer or float
    operator
        String that contains addition (+), 
        subtraction(-), multiplication(*), 
        division(/), integer division (//) 
        or power(**).
    
    Returns
    -------
    Return the result of the operation 
    between the two inputs, but if the 
    operation was invalid return False

    Example
    -------
    >>> calculator(1,2,"+")
    3
    >>> calculator(12, 4.2, *)
    50.400000000000006
    """
    if operator == '**':
        return number1 ** number2
    elif operator == '/' and number2 != 0: #checking to make sure number does't get divided by 0
        return number1 / number2
    elif operator == '//' and number2 != 0: #checking to make sure number does't get divided by 0
        return number1 //number2
    elif operator == '*':
        return number1 * number2
    elif operator == '+':
        return number1 + number2
    elif operator == '-':
        return number1 - number2
    else:
        return False


