from pip._vendor.distlib.compat import raw_input


def is_leap(inputedYear):
    if inputedYear % 4 == 0:
        if inputedYear % 100 == 0:
            if (year % 400) == 0:
                return True
            return False
        return True
    return False


year = int(raw_input())
print(is_leap(year))
