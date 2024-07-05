
def email_check(email):
    """
    A subroutine that accepts email address and checks wether it is a valid email address containing a domain name
    Args:
        email (str): an email entered by the user

    Returns:
        bool: True or False after evaluation
    """
    at = 0
    dot = 0
    if (email[0] == "." or email[len(email)-1] == ".") or (email[0] == "@" or email[len(email)-1] == "@") or (email[0] == "!" or email[len(email)-1] == "!") or (email[0] == "@" or email[len(email)-1] == "@"):
        print("Invalid Email")
    else:
        for index, char in enumerate(email):
            if char == "@":
                at = index+1
            if char == ".":
                dot = index
                break
    sliced = email[at:dot].lower()
    if sliced == "gmail" or sliced == "yahoo" or sliced == "hotmail" or sliced == "khwopa":
        return True
    else:
        print("\033[91mInvalid email\033[0m")
        return False
