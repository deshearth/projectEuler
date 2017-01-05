def sieve(factor,candidate):
  #print len(candidate)
  return [candidate[i] for i in range(len(candidate)) if candidate[i]%factor !=0]


def createVec(length):
  vec = []
  for i in range(length):
	vec.append(i)
  return vec
  


def sievePrime():
  length = 2000000
  candidate = createVec(length)[2:]
  #print 'initial',candidate
  primeList = []
  while True:
	primeList.append(candidate.pop(0))
	#print 'primeList',primeList
	candidate = sieve(primeList[-1],candidate)
	#print 'after one sieve',candidate
	
	if pow(primeList[-1],2)>candidate[-1]:
	  primeList = primeList + candidate
	  break
  print primeList,'\n',sum(primeList)

if __name__=='__main__':
  sievePrime()
  '''my implementation has large problems!!! Too slow!!'''
