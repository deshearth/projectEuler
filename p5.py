def gcd(x,y):
  if not x:
	return y
  x,y = (x,y) if x<y else (y,x)
  y = y % x # after module operation, y<x
  r = gcd(y,x)
  return r

def lcm(x,y):
  return x*y/gcd(x,y)
  
def main():
  result = reduce(lcm,[i for i in range(1,21)]) 
  print result
if __name__=='__main__':
  main()
