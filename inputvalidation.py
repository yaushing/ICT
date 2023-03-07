#input  validation
def parse_int(inputgiven, msg, Max = 10000000, forbid = 0, excepted = []):
    try:
        if inputgiven in excepted:
            return inputgiven
        int(inputgiven)
        if int(inputgiven) > Max:
            raise ValueError()
        if int(inputgiven) == forbid:
            raise ValueError()
        return int(inputgiven)
    except:
        return parse_int(input(msg), msg)

def parse_float(inputgiven, msg, Max = 10000000, forbid = 0, excepted = []):
    try:
        if inputgiven in excepted:
            return inputgiven
        float(inputgiven)
        if float(inputgiven) > Max:
            raise ValueError()
        if float(inputgiven) == forbid:
            raise ValueError()
        return float(inputgiven)
    except:
        return parse_int(input(msg), msg)