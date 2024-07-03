def check_phone(phone):
    """
    A subroutine that checks if the entered phone number is 10 digit or not

    Args:
        phone (int): Integer entered by the user

    Returns:
        bool: Evaluates and returns True or False
    """
    str_phone = str(phone)
    if len(str_phone) == 10:
        return True
    else:
        print("\033[91mInvalid phone: Should be 10 digits\033[0m")
        return False



    
