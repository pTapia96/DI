def resistivity  (r: float, a: float, l: float) -> float:
    """Return the electrical resistivity of a specimen with r electrical resistance,
    l length and a cross-sectional area

    Preconditions:
    r > 0
    a > 0
    l > 0

    >>> resistivity(5, 5, 5)
    5.0
    >>> resistivity(240, 30.31, 14.3)
    508.7
    """
    return round(r*(a/l), 2)


import doctest
doctest.testfile("doctest.txt")
