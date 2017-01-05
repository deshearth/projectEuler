def main():
  num = raw_input('input number= ')
  #print factorize(int(num))
  print max(factorize(int(num)).iteritems())[0]



def factorize(num):
  'the input must be larger than 1'
  prime = 2
  d = {2:0}
  while True: 
	if not num % prime:
	  num,d[prime]= mulDiv(num,prime)
	if num == 1:
	  return d
	prime = nextPrime(prime)

def nextPrime(prime):
  while True:
	prime = prime + 1
	if isprime(prime):
	  return prime

import math
def isprime(targ):
  for i in range(2,int(math.sqrt(targ))+1):
	if not targ % i:
	  return False
  return True

def mulDiv(numer,denom):
  power = 0
  while not numer % denom:
	numer = numer / denom
	power += 1
  return numer,power
  
if __name__=='__main__':
  main()
