def capicua (num):

    original_num = num
    invert_num = 0

    while num > 0:
        number = num % 10
        invert_num = invert_num * 10 + number
        num //= 10 

    if original_num == invert_num:
        print(f"{original_num} is a palindrome.")
    else:
        print(f"{original_num} is not a palindrome.")


    