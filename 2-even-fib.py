def fib(x, y, total):
  print x
  if x % 2 == 0:
    total = total + x
  if x > 4000000:
    print "sum of evens = " + str(total)
    return
  else:
    return fib(y, y+x, total)

total = 0
fib(1, 1, total)
