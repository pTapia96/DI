def resistivity  (r: float, a: float, l: float) -> float:
    """Calculates electrical resistivity of a uniform specimen.
    
    Parameters:
    r: electrical resistance of the specimen
    a: cross-sectional area of the specimen
    l: lenght of the specimen
    
    Preconditions:
    r > 0
    a > 0
    l > 0
    
    Examples:
    >>> resistivity(5, 5, 5)
    5.0
    >>> resistivity(240, 30.31, 14.3)
    508.7
    """
    return round(r*(a/l), 2)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    doctest.testfile("doctest.txt")
