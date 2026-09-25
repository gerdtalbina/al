#1/usr/bin/python3

def solve(a, b, c):

    d=b**2 - 4 * a * c
    if d == 0:
        return -b / 2 / a

    if d < 0:
        print("ERROR")
        return
    return ((-b + d**0.5) / 2 / a,
            (-b - d**0.5) / 2 / a )



a, b, c = map(int, input().split())
print(solve(a, b, c))
