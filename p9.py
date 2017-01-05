'''this problem is special. Mathematical derivation will
helps reduce the computation cost to a large extent.
  First, it actually asks for the integer solutions to
  pythagorean theorem. The derivation is following:
	a^2 + b^2 = c^2
	divided by c^2 on both sides, we get
	(a/c)^2 + (b/c)^2 = 1
	From here, we can see that if we can find rational
	solution, then after scaling, we can get the integer
	solution.
	So we construct a unit circle and a straight line with
	the line going through point (-1,0). If we denote the 
	slope of line as q/p, we line expression would be
	y = (q/p)(x+1), p, q are integers. In this case, we
	guarantee that another crossing point's coordinate
	must be rational. Since if it's not, the slope would
	not be rational.Then we compose two functions
	we can get the solution x = (p^2-q^2)/(p^2+q^2)
							y = 2pq/(p^2+q^2)
							1 = (p^2+q^2)/(p^2+q^2)
	after scaling,			a = (p^2-q^2)
							b = 2pq
							c = (p^2+q^2)
	Then a+b+c=1000 and a<b
	so   x+y+z=p(p+q)=500 and p>5*sqrt(10) and p<10*sqrt(5)
	if p belongs to [16,22]
	use a loop can easily determine that p = 20,q=5
	and a = 375, b = 200, c = 425
'''
print 375*200*425
