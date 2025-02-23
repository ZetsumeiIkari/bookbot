def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words (text)
    num_chars = char_count(text)
    
     
def get_book_text(path):
    with open(path) as f:
        return f.read()

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

main()