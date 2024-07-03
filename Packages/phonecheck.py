def check_phone(phone):
    str_phone = str(phone)
    if len(str_phone) == 10:
        return True
    else:
        print("\033[91mInvalid phone: Should be 10 digits\033[0m")
        return False



    