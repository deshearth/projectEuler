import timeit
start = timeit.default_timer()
sum = 0
a,b = 0,1
while sum<=4000000:
  a = a + b
  if a % 2 == 0:
	sum = sum + a
  a,b = b,a
print sum
stop = timeit.default_timer()
print stop - start

