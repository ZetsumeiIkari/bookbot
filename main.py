def main():
    path_to_file = "books/frankenstein.txt"
    with open(path_to_file) as f:
        file_contents = f.read()
        #print(file_contents)
        count(file_contents)

def count(file_contents):
    words = file_contents.split()
    print (len(words))

main()