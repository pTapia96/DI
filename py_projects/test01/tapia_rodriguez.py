def toroid_area (R: float, r: float) -> float:
    """Returns the area of a toroid with a known radius of revolution and sectional radius.
    
    Parameters:
    R: Radius of revolution. Must be the same unit of measure as r.
    r: Radius of the circular section. Must be the same unit of measure as R.
    
    Examples:
    >>> toroid_area(5,1)
    197.39
    >>> toroid_area(155, 78)
    477294.07
    >>> toroid_area(34.78, 12.1)
    16614.02
    """	
    import math
    return round(4*pow(math.pi,2)*R*r,2)




