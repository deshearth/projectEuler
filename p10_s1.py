from p3 import isprime

def main():
  'this algorithm is very stupid'
  sum = 0
  for i in range(2,2000000):
	if isprime(i):
	  sum += i
  print sum

if __name__ == '__main__':
  main()
