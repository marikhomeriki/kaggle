def is_late(arrivals, name):

    half = len(arrivals)/2
    if (arrivals.index(name) >= half) and (arrivals.index(name) != (len(arrivals) - 1)):
        return True
    else:
        return False
