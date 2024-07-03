def marks_check(marks):
    if marks >= 0.0 and marks <= 100.0:
        return True
    else:
        print("\033[91mError: Marks should be between 0-100\033[0m")
        return False