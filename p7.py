from p3 import isprime
def main():
  count = 0
  number = 2
  while True:
	if isprime(number):
	  count += 1
	  if count == 10001:
		print number
		break
	number += 1

if __name__ == '__main__':
  main()
