def tripler(inputFunction):
    """
     Call an inputted three times

    This function basically takes takes in 
    a function as an input and calls it three
    times.

    Parameters
    ----------
    inputFunction: function
        Function that will get called three times.
    
    Returns
    -------
    Returns what inputFunction does three times
    """
    def wrapper():
        inputFunction()
        inputFunction()
        inputFunction()
    return wrapper
