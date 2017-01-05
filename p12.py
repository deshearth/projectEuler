import p3
def main():
  n = 1
  while True:
	triNum = n*(n+1)/2
	divNum = reduce(lambda x,y=1:x*y,[i+1 for i in p3.factorize(triNum).values()])  
	#print divNum
	if divNum > 500:
	  print '%dth triangular number: %d)' % (n,triNum)
	  break
	
	n += 1
if __name__=='__main__':
  main()
