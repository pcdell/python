def triplet(atuple):
    if len(atuple) < 3:
        return "Need more integers"
    length = len(atuple)
    for i in range(length):
        for j in range(i + 1, length):
            for k in range(j + 1, length):
                if sum((atuple[i], atuple[j], atuple[k])) == 0:
                    return ((atuple[i], atuple[j], atuple[k]))


def triplet2(atuple):
    return next(((a, b, c) for i, a in enumerate(atuple) for j, b in enumerate(atuple[i + 1:]) for c in atuple[i + j + 2:] if a + b + c == 0), "Need more integers")