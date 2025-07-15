from stats import get_num_words
from stats import get_num_chars

def main():
    filepath="books/frankenstein.txt"
    print(get_num_words(filepath))
    print(get_num_chars(filepath))

main()
