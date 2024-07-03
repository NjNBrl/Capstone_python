def marks_check(marks):
    """
    A subroutine that checks if the entered marks is in range between 0 and 100

    Args:
        marks (float): Marks of the student entered by the teacher

    Returns:
        bool: Evaluates and returns True or False
    """
    if marks >= 0.0 and marks <= 100.0:
        return True
    else:
        print("\033[91mError: Marks should be between 0-100\033[0m")
        return False
