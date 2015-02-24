palindromes = []

print "calculating..."

# Get them
for i in range(0, 999):
  for j in range(0, 999):
    result = str(i * j)
    if len(result) > 1:
      reverse = result[::-1]
      if result == reverse:
        palindromes.append(int(result))
        # print str(i) + " * " + str(j) + " = " + result

# The largest
print "total: " + str(len(palindromes))
print "largest: " + str(max(palindromes))
