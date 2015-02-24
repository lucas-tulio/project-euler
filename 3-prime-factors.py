num = 600851475143
primes = []

for i in range(2, num):
  if num % i == 0:
    primes.append(i)
  result = 1
  for j in primes:
    result = result * j
  if result == num:
    break

print primes[-1]
