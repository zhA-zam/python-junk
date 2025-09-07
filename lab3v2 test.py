txt = "Hello, welcome to my world."
print(txt[0:3])
x = txt.startswith(txt[0:3])

print(x)

filename = 'klingon-english.txt'
mode = 'r'
file = open(filename, mode)

content = file.read()
print(content)

list_of_words = content.split('\n') 
print(list_of_words)

print("")

for word in list_of_words:
    klingon = word.split('|')
    x = klingon[0]
    print(klingon)
    print(x[0:2])