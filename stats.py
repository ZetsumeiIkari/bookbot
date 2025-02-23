def get_num_words(text):
    words = text.split()
    return len(words)

def char_count(text):
    char_list = list(text.lower())
    char_set = set(char_list)
    output = {}
    for c in char_set:
        output.update({c : (char_list.count(c))})
    return output
