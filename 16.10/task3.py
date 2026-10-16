import string
a = open('/home/student/LICENSE.txt', 'r')
text = a.read().lower()
a.close()
for znak in string.punctuation:
    text = text.replace(znak, ' ')
words = text.split()
b = {}
for word in words:
    if word in b:
        b[word] += 1
    else:
        b[word] = 1
for i in range(10):
    maxword = max(b, key=b.get)
    print(maxword, b[maxword])
    del b[maxword]

