#CORRECTIONS MADE
#1 - We only need to include preconditions to avoid execution errors (here, you can't divide by zero).
#2 - It is not necessary to call testmod() and testfile() from the module, just use the command line shortcut.

def rho  (r: float, a: float, l: float) -> float:
    """Returns electrical resistivity of a uniform specimen.
    
    Parameters:
    r: electrical resistance of the specimen
    a: cross-sectional area of the specimen
    l: lenght of the specimen
    
    Precondition: length must be a non-zero value
    
    Examples:
    >>> rho(5, 5, 5)
    5.0
    >>> rho(240, 30.31, 14.3)
    508.7
    """
    return round(r*(a/l), 2)

#I don't know why, but if you don't use this 'if', 
#testfile() will run into a failed example at 'from resistivity import resistivity'
#if __name__ == "__main__":
#    import doctest
#    doctest.testmod()
#    doctest.testfile("rho_test.txt")
