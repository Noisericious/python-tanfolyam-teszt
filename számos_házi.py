def is_in_range(num: int, small_num: int, large_num: int) -> bool:
    """
    Check number is in range.
    :param num: The number to check.
    :param small_num: Range lowest value.
    :param large_num: Range highest value.
    :return: True, if number is in range.
    :raise: ValueError if small_num is bigger than large_num.
    """
    if small_num > large_num:
        raise ValueError (f"The small_num {small_num} is bigger than the large_num {large_num}")
    return small_num <= num <= large_num

def display_is_in_range(num: int, small_num: int, large_num: int) -> None:
    if is_in_range(num, small_num, large_num):
        print("{} szám benne van a tartományban: {} és a {} között".format(num, small_num, large_num))
    else:
        print("A tartományon kívül esik!")

display_is_in_range(5, 2, 7)
