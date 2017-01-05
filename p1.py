import timeit
### simplist way ###
start = timeit.default_timer()
sum = 0;
for i in range(1,1000):
  if i % 3 == 0 or i % 5 == 0:
	sum = sum + i
print sum
stop = timeit.default_timer()
print stop - start


''' using gcd algorithm would be quicker,
 but the time complexity is still O(n)
 here is one algorithm in adding the series
'''
import math
start = timeit.default_timer()
print (3 + 3* math.floor(999/3)) * int(999/3) / 2 + \
	  (5 + 5*math.floor(999/5)) * int(999/5) / 2 - \
	  (15 + 15* math.floor(999/15)) * int(999/15) / 2
stop = timeit.default_timer()
print stop - start
