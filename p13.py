def main():
  f = open('textforp13.txt','r')
  print str(sum((int(eachLine.strip('\n')) for eachLine in f)))[:10]
  f.close()
if __name__=='__main__':
  main()

