import time
import sys
import math

def is_prime(num):

  if num == 2: return True
  if num % 2 == 0: return False

  limit = int(math.ceil(math.sqrt(num)))
  for i in xrange(3, limit + 1, 2):
    if num % i == 0:
      return False
  return True

def find_nth_prime(num):
  primes = 0
  i = 2
  while primes < num:
    if is_prime(i):
      primes = primes + 1
    i = i + 1
  print str(num) + "th prime: " + str(i - 1)

if len(sys.argv) != 2:
  print "Example usage: python 7-nth-prime.py 10001"
  sys.exit()

start = time.time()
find_nth_prime(int(sys.argv[1]))
end = time.time()
print "Time to calc: " + str(end - start)
