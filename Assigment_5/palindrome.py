def palindrome(astring):
    total = 0
    comb = list(set([astring[i: j] for i in range(len(astring)) for j in range(i + 2, len(astring) + 1)]))
    for x in range (len(comb)):
        if comb[x] == comb[x][::-1]:
            total += 1
    print (comb)
    print (f"For string '{astring}': {total} palindrome substrings")



def palindrome2 (astring):
    total = sum(1 for s in set(astring[i: j] for i in range(len(astring)) for j in range(i + 2, len(astring) + 1)) if s == s[::-1])
    print(f"For string '{astring}': {total} palindrome substrings")