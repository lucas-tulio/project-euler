for i in range(1, 15000000):
  equals = i**2 + (i+1)**2 == (i+2)**2
  if equals:
    print(str(i) + "**2 = " + str(i**2) + " + " + str(i+1) + "**2 = " + str((i+1)**2) + " -> " + str(i**2 + (i+1)**2) + " == " + str((i+2)**2) + "? " + str(equals))
