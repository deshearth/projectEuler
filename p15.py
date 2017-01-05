'''it's just select 20 from 40'''
def factorial(n):
  if not n:
	return 1
  return reduce(lambda x,y=1:x*y,(i for i in range(n,0,-1)))

def combination(m,n):
  'the formula is n!/((n-m)!*m!)'
  print factorial(n)/(factorial(n-m)*factorial(m))
def main():
  n = int(raw_input('n = '))
  m = int(raw_input('m = '))
  combination(m,n)
  

if __name__=='__main__':
  main()
