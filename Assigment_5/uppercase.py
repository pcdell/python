def uppercase(astring):
    for x in range(3):
        if astring[x].isupper():
            astring = astring.upper()
    print (astring)   
    
    
def uppercase2(astring):
    if any(char.isalpha() and char.isupper() for char in astring[:3]):
        print(astring.upper())
    else:
        print(astring)