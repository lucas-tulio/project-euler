import time

start_time = time.time()

divisors = 20
limit = 10000000

def test_division(num, divisors):
  for i in range(1, divisors + 1):
    if num % i != 0:
      return False
  return True

print "numbers that divide by all numbers from 1 to " + str(divisors) + ", up to " + str(limit) + ":"

for i in range(1, limit):
  if test_division(i, divisors):
    print i

elapsed_time = time.time() - start_time
print "time to calc: " + str(elapsed_time)
