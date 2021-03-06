def gcd(a, b):
    if a == 0:
        return b
    elif a % 2 == 0 and b % 2 == 0:
        return 2 * gcd(a / 2, b / 2)
    elif a % 2 == 0 and b % 2 != 0:
        return gcd(a / 2, b)
    elif a % 2 != 0 and b % 2 == 0:
        return gcd(a, b / 2)
    else:
        if a < b:
            a, b = b, a
        return gcd((a - b) / 2, b)
def getPrime(n):
    res = [1, n]
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            res.append(i)
            if int(n / i) != i:
                res.append(int(n / i))
    return sorted(res)
def primeRange(q, a, b):
    res = []
    for i in range(a, b + 1):
        if gcd(i, q) == 1:
            res.append(i)
    return res
modulo = 1000000007
n = int(input())
for i in range(n):
    q, a, b = list(map(int, input().strip().split()))
    s = 0
    for j in primeRange(q, a, b):
        s += j
    print(s % modulo)
