def sqInRect(lng, wdth):
    result = []
    if lng == wdth:
        return None
    while (True):
        if lng > wdth:
            print result
            result.append(wdth)
            lng = abs(lng-wdth)
        elif wdth > lng:
            print result
            result.append(lng)
            wdth = abs(lng-wdth)
        elif wdth == lng:
            result.append(lng)
            return result

print sqInRect(9, 3)