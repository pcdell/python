def translate(astring, table):
    for x in range(len(table)):
        astring = astring.replace(str(table[x][0]), str(table[x][1]))
    return astring