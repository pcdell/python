def concatenate(n1, n2):
    # Find the number of digits in n2
    num_digits_n2 = 0
    temp_n2 = n2
    while temp_n2 > 0:
        temp_n2 //= 10
        num_digits_n2 += 1

    # Multiply n1 by 10^(number of digits in n2) and add n2
    result = n1 * (10 ** num_digits_n2) + n2

    return result