import sys
from stats import get_num_words
from stats import get_num_chars
from stats import sorted_num_chars

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main():
    filepath=sys.argv[1]
    print("Word Count")
    print(get_num_words(filepath))
    chars=get_num_chars(filepath)
    print("Character Count")
    for x in sorted_num_chars(chars):
        if x["char"].isalpha():
            print(f"{x["char"]}: {x["num"]}")

main()
