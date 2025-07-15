def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
def get_num_words(filepath):
    num_words=len(get_book_text(filepath).split())
    return f"{num_words} words found in the document"

