def count_globe_volume(radius: float) -> float:
    """
    This function returns the volume of a globe.
    :param radius: The radius of the globe.
    :return: The volume of the globe.
    """
    #if radius > 0:
    #    return (4/3) * 3.14 * (radius ** 3)
    #return -1
    if radius <= 0:
        raise ValueError("Radius must be a positive number.")
    return (4/3) * 3.14 * radius ** 3
print(count_globe_volume(2))



