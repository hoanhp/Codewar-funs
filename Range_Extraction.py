def solution(args):
    args.append(-999999)
    tmp_range = [str(args[0])]
    result = ''
    for i in range(1,len(args)):
        number = args[i]
        if (number != int(tmp_range[len(tmp_range)-1]) + 1):
            if len(tmp_range) >= 3:
                result += ("%s-%s,") % (tmp_range[0], tmp_range[-1])
            else:
                result += ("%s,") % (','.join(tmp_range))
            tmp_range = [str(number)]
        else:
            tmp_range.append((str(number)))
    args.remove(-999999)
    return result[:-1]

print solution([-88, -87, -84, -81, -78, -77, -76, -74, -73, -71, -68, -65, -62, -61, -59, -56, -55, -54, -52, -49, -47, -44, -41, -39, -36, -35, -33, -31, -28])