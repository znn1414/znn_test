def while_function(i):
    j = 0
    numbers =  []

    while j < i:
      numbers.append(j)
      j += 1
	
	
    return numbers
	
	
numbers = while_function(6)

print "The numbers is %r." % numbers

