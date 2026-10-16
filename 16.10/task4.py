f = open('en-ru.txt', 'r')
d = {}
for line in f:
    if '-' in line:
        a, b = line.strip().split(' - ')
        d[a] = b
f.close()
f = open('input.txt', 'r')
text = f.read()
f.close()
words = text.split()
result = []
for word in words:
    clean = word.lower().strip('.,!?')
    if clean in d:
        new = d[clean]
        if word[0].isupper():
            new = new.capitalize()
        if word[-1] in '.,!?':
            new += word[-1]
        result.append(new)
    else:
        result.append(word)
f = open('output.txt', 'w')
f.write(' '.join(result))
f.close()
