def formal(name):
    char_name = []
    all_name = name.split()
    substrings_to_remove = ["de", "e"]
    res = [i for i in all_name if i not in substrings_to_remove]
    char_name = ". ".join(res[i][0] for i in range(len(res)))
        
    print(all_name[-1]+ ", " + char_name + ".")


def formal2(name):
    all_name = name.split()
    substrings_to_remove = ["de", "e"]
    char_name = ". ".join(word[0] for word in all_name if word not in substrings_to_remove)
    print(all_name[-1] + ", " + char_name + ".")
