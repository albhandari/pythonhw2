import time

def calculate_time(aFunc):
    """
    Calculates time for a function to run

    This decorator takes in another function as
    an input and using the time library, it takes
    the time as the function starts and at the 
    end is subtracted with the time the function
    ends. This returns the total time it took 
    for the function to run (in seconds).

    Parameters
    ----------
    aFunc: Function
        Function that is chekd for run-time
    
    Returns
    -------
    Prints the time in second it takes to run 
    the aFunc  
    """
    def wrapper():
        startTime = time.time()
        aFunc()
        print('Total time ' + str(time.time() - startTime))
    wrapper()




