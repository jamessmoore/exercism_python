def leap_year(year):

    if not (year % 100):
        if not (year % 400):
            return True
    else:
        if not (year % 4):
            return True

    return False
