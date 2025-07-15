from stats import get_num_words
from stats import get_num_chars
from stats import sorted_num_chars

def main():
    filepath="books/frankenstein.txt"
    print("Word Count")
    print(get_num_words(filepath))
    chars=get_num_chars(filepath)
    print("Character Count")
    for x in sorted_num_chars(chars):
        if x["char"].isalpha():
            print(f"{x["char"]}: {x["num"]}")

main()
