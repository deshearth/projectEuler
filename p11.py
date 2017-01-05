import operator
def findMaxP(i,j,matrix):
  maxRow = len(matrix)
  maxCol = len(matrix[0])
  d = {}
  #product in left direction
  d['left'] = 0 if j - 3 < 0 else \
		  matrix[i][i]*matrix[i][j-1]*matrix[i][j-2]*matrix[i][j-3]
  #product in right direction
  d['right'] = 0 if j + 3 > maxCol-1 else \
		  matrix[i][j]*matrix[i][j+1]*matrix[i][j+2]*matrix[i][j+3]
  #product in up direction
  d['up'] = 0 if i - 3 < 0 else \
		  matrix[i][j]*matrix[i-1][j]*matrix[i-2][j]*matrix[i-3][j]
  #product in down direction
  d['down'] = 0 if i + 3 > maxRow-1 else \
		  matrix[i][j]*matrix[i+1][j]*matrix[i+2][j]*matrix[i+3][j]
  #product in upleft direction
  d['upleft'] = 0 if i - 3 < 0 or j - 3 < 0 else \
		  matrix[i][j]*matrix[i-1][j-1]*matrix[i-2][j-2]*matrix[i-3][j-3]
  d['upright'] = 0 if i - 3 < 0 or j + 3 > maxCol - 1 else \
		  matrix[i][j]*matrix[i-1][j+1]*matrix[i-2][j+2]*matrix[i-3][j+3]
  #product in downleft direction 
  d['downleft'] = 0 if i + 3 > maxRow - 1 or j - 3 < 0 else \
		  matrix[i][j]*matrix[i+1][j-1]*matrix[i+2][j-2]*matrix[i+3][j-3]
  #product in downright direction
  d['downright'] = 0 if i + 3 > maxRow - 1 or j + 3 > maxCol - 1 else \
		  matrix[i][j]*matrix[i+1][j+1]*matrix[i+2][j+2]*matrix[i+3][j+3]
  print d 
  return max(d.iteritems(),key=operator.itemgetter(1)) # return value is a tuple 
                        #(d.key,d.value)
  

def readMatrix(filename):
  f = open(filename,'r')
  matrix = []
  for eachLine in f:
	matrix.append([int(i) for i in (eachLine.strip('\n')).split(' ')])
  f.close()
  return matrix

def largestProductinGrid():
  filename = 'textforp11.txt'
  matrix = readMatrix(filename)
  #print matrix[0]
  maxProd = 0
  for i in range(len(matrix)):
	for j in range(len(matrix[i])):
	  if matrix[i][j] == 0:
		continue
	  r = findMaxP(i,j,matrix)
	  if r[1] > maxProd:
		maxProd = r[1]
        print maxProd
    
        rowloc = i
        colloc = j
        direction = r[0]
  print '''\n%s\nmax Product is %d 
the location is %dth row %dth col, direction is %s
%s\n''' % ('-'*30,maxProd,rowloc,colloc,direction,'-'*30)

if __name__=='__main__':
  largestProductinGrid()
