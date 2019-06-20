spam = ['apples', 'bananas', 'tofu', 'cats']

def comma(spam):
    spam[-1] = 'and ' + spam[-1] 
    print(", ".join(spam))
comma(spam)
