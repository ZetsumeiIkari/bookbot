from stats import get_num_words, get_chars_dict, sort

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    sorted = sort(chars_dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i in sorted:
        if str.isalpha(i["char"]):
            print (f"{i["char"]}: {i["num"]}")
        # formatted = format(num_words,chars_dict,sorted)
        # print(formatted)
    print("============= END ===============")

main()
