def issymmetric(p):
  s = str(p)
  for i in range(int(len(s)/2)):
	if s[i] != s[len(s)-1-i]:
	  return False
  return True

def main():
  m = 0
  for i in range(999,99,-1):
	for j in range(999,99,-1):
	  p = i * j
	  if issymmetric(p) and p > m:
		m = p
  print m

				
if __name__== '__main__':
  main()

