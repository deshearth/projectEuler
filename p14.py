def even(num):
  return not num % 2
def seqLen(n):
  seq = [n]
  while True:
	n = n / 2 if even(n) else 3 * n + 1
	seq.append(n)
	if n == 1:
	  break
  return len(seq)
   
def main():
  length = 0
  number = 1
  for n in range(1,1000000):
	if seqLen(n) > lengthm
  print length

if __name__=='__main__':
  main()
