a = int(input())
b = []

i = 2
while i * i <= a:
    if a % i == 0:
        b.append(i)
        a = a // i

    else:
        i += 1

if a > 1:
    b.append(a)

print(b)
