
def swap_last_item(listInput):
    """
    Swaps the first and last element of the list

    This function basically takes in a list input 
    which is then modified where the first and the
    last elements are swapped.

    Parameters
    ----------
    listInput: List
        List that get's modified.
    
    Returns
    -------
    A new list where the first and the last elements 
    are swapped.

    Example
    -------
    >>> swap_last_item([12, 35, 5, 9, 56, 24])
    [24, 35, 5, 9, 56, 12]
    >>> swap_last_item([1, 8, 9, 2, 3])
    [3, 8, 9, 2, 1]
    """
    if len(listInput) == 0:  #in case the list is empty
        return listInput
    tempValue = listInput[0]
    listInput[0] = listInput[-1]
    listInput[-1] = tempValue
    return listInput


