numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = list()
not_primes = list()

for j in numbers:

    k = 0
    for i in range(2, j // 2 + 1):
        if (j % i == 0):
            k = k + 1
    if (k <= 0):  # print("Число простое")
        primes.append(j)

    else:
        not_primes.append(j)

print("Primes: ",primes)
print("Not Primes: ",not_primes)
