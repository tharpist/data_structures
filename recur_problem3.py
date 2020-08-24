def word_split(a,b):
        return word_split([word for word in b if word.find(a)], b)



x = 'themanram'
y = ['the', 'ran', 'man']


print(word_split(x,y))