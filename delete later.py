def change(astring):
    new_word = 'j'
    i = 1
    while (i < len(astring)):
        new_word = new_word + astring[i]
    return new_word

string = change('hello')
print(string)
