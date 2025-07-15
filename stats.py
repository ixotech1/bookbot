def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
def get_num_words(filepath):
    num_words=len(get_book_text(filepath).split())
    return f"{num_words} words found in the document"

def get_num_chars(filepath):
    res={}
    for x in get_book_text(filepath).lower():
        if x in res:
            res[x]+=1
        else:
            res[x]=1
    return res
