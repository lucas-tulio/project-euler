def get_sum_of_squares(num):
  result = 0
  for i in range(1, num + 1):
    result = result + i**2
  return result

def get_square_of_sum(num):
  result = 0
  for i in range(1, num + 1):
    result = result + i
  result = result**2
  return result

num = 100
sum_of_squares = get_sum_of_squares(num)
square_of_sum = get_square_of_sum(num)

print "sum of squares: " + str(sum_of_squares)
print "square of sum: " + str(square_of_sum)
print "difference: " + str(square_of_sum - sum_of_squares)
