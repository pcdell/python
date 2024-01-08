def fizz_buzz(n):
    
    n = int(n)
    sequence_n = []
    result = ""

    for i in range(1, n+1):
        sequence_n.append(i)

    for x in sequence_n:
        if x % 3 == 0:
            result += "Fizz "
        elif x % 5 == 0:
            result += "Buzz "
        else:
            result += str(x) + " "

    return result.strip()   # .strip Remove trailing space 