def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
def main():
    print("{num_words} words found in the document".format(num_words=len(get_book_text("books/frankenstein.txt").split()))
        )

main()
