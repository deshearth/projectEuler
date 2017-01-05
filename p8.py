def prod(s):
  p = reduce(lambda x,y : int(x)*int(y),list(s))
  #print p,'*'
  return p

def getLocalMax(series,seriesLen):
  maxProd = 0
  for i in range(len(series)-seriesLen+1):
	maxProd = max(maxProd,prod(series[i:i+seriesLen]))
	#print seriesLen,'-digit series',series[i:i+seriesLen]
  return maxProd

import string

def readText():
  f = open('textforp8.txt','r')
  s = ''.join((eachLine.strip('\n') for eachLine in f))
  f.close()
  return s



def main():
  s = readText()
  seriesLen = 13
  globalMax = 0
  s = s.split('0')
  for i in range(len(s)):
	if len(s[i])<seriesLen:
	  continue
	else:
	  globalMax = max(globalMax,getLocalMax(s[i],seriesLen))
	 # print 'series containing 13 digits',s[i],'\n'*2
  print globalMax

if __name__ == '__main__':
  main()
