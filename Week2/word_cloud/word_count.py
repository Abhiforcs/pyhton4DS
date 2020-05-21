import string
fhand = open("98-0.txt")

stopwords = set (ln.strip()  for ln in open('stopwords'))

d = dict()

for ln in fhand:
    ln = ln.rstrip()
    ln = ln.lower()
    ln = ln.translate(ln.maketrans('','',string.punctuation))
    ln = ln.translate(ln.maketrans('','',string.digits))
    ln = ln.translate(ln.maketrans('','',"”"))
    ln = ln.translate(ln.maketrans('','',"“"))
    ln = ln.translate(ln.maketrans('','',"’"))
    words = ln.split()
    for word in words:
        if word in stopwords:continue
        d[word] = d.get(word,0) + 1

words_list = list()

for key,val in d.items():
    words_list.append((val,key))
words_list.sort(reverse = True)

most_common = list()
for i in range(0,11):
    most_common.append(words_list[i])
for val,key in most_common:
    print(key,':',val)
