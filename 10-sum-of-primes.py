import time
import math

def is_prime(num):

  if num == 2: return True
  if num % 2 == 0: return False

  limit = int(math.ceil(math.sqrt(num)))
  for i in xrange(3, limit + 1, 2):
    if num % i == 0:
      return False
  return True

def sum_primes(max):

  result = 0
  for i in range(2, max):
    if is_prime(i):
      result = result + i

  return result

start = time.time()
print sum_primes(2000000)
end = time.time()
print "Time to calc: " + str(end - start)
