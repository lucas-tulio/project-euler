def is_prime(num, i):

  if num == 1:
    return True
  if num % 2 == 0:
    return False

  for i in xrange(3, num, 2):
    if num % i == 0:
      return False

  return True

def find_nth_prime(num):
  primes = 0
  i = 2
  while primes < num:
    if is_prime(i, 2):
      print i
      primes = primes + 1
    i = i + 1

find_nth_prime(10001)
