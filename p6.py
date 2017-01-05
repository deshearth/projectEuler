sumOfSquare = sum((i*i for i in range(1,101)))
squareOfSum = pow(sum((i for i in range(1,101))),2)
print squareOfSum-sumOfSquare
