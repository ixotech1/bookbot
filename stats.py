def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
def get_num_words(filepath):
    num_words=len(get_book_text(filepath).split())
    return f"Found {num_words} total words"

def get_num_chars(filepath):
    res={}
    for x in get_book_text(filepath).lower():
        if x in res:
            res[x]+=1
        else:
            res[x]=1
    return res

def sorted_num_chars(char_dict):
    res=[]
    for key,value in char_dict.items():
        res.append({"char":key,"num":value})
    res.sort(reverse=True, key=lambda items: items["num"])
    return res
