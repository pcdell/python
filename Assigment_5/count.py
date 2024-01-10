import re
def count (word, phrase):
    pattern = re.compile(r'\b' + re.escape(word.lower()) + r'\b')
    matches = pattern.findall(phrase.lower())
    count = len(matches)
    
    return count