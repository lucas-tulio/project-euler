num = 13195
primes = []

print "num = " + str(num)

for i in range(2, num):
  if num % i == 0:
    print i
    primes.append(i)
  result = 1
  for j in primes:
    result = result * j
  if result == num:
    break

print "last: " + str(primes[-1])
