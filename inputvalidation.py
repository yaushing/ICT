#input  validation
def parse_int(inputgiven, msg, Max = 10000000, Min = 0, forbid = 0, exceptions = []):
    try:
        if inputgiven in exceptions:
            return inputgiven
        int(inputgiven)
        if int(inputgiven) > Max or int(inputgiven) < Min:
            raise ValueError()
        if int(inputgiven) == forbid:
            raise ValueError()
        return int(inputgiven)
    except:
        return parse_int(input(msg), msg)

def parse_float(inputgiven, msg, Max = 10000000, Min = 0, forbid = 0, exceptions = []):
    try:
        if inputgiven in exceptions:
            return inputgiven
        float(inputgiven)
        if float(inputgiven) > Max or float(inputgiven) < Min:
            raise ValueError()
        if float(inputgiven) == forbid:
            raise ValueError()
        return float(inputgiven)
    except:
        return parse_float(input(msg), msg)