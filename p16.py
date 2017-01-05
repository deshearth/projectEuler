def powerDigit(base,power):
  if base == 0:
	return 'Invalid input'
  elif base == 1:
	return '1'
  else:
	result = [1]
	carry = 0
	for p in range(power):
	  for i in range(len(result)-1,-1,-1):
		temp = result[i] * base + carry
		if temp < 10:
		  result[i] = temp
		  carry = 0
		else:
		  result[i] = temp % 10
		  carry = int(temp/10)
	  if carry:
		result = [carry] + result
		carry = 0
		#print result
	return ''.join(str(x) for x in result)

def main():
  base = int(raw_input('base(base is one digit) = '))
  power = int(raw_input('power = '))
  result = powerDigit(base,power)
  print result
  print sum((int(x) for x in result))
if __name__=='__main__':
  main()
