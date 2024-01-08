def triangle_form(a, b, c):
    if a + b < c or a + c < b or c + b < a:
        return "Not a triangle"
    elif a == b == c:
        return "Equilateral"
    elif a == b or a == c or c == b:
        return "Isosceles"
    else:
        return "Scalene"
    



def triangle_form_less_lines(a, b, c):
    return "Not a triangle" if a + b < c or a + c < b or c + b < a else \
           "Equilateral" if a == b == c else \
           "Isosceles" if a == b or a == c or c == b else "Scalene"