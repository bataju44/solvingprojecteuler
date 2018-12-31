#12/30/2018
#Problem 2 


import time

t0= time.time()
def sum_even(V):
	
	b = sum([i for i in V if i%2==0])
	return b

memo = {0:1, 1:2}
def fib(n):
	if not n in memo:
		memo[n] = fib(n-1) + fib(n-2)
	return memo[n]

l = 400
fib_seq = [fib(i) for i in xrange(l) if fib(i) <4000000]
#n = len(fib_seq)
print sum_even(fib_seq)
t1 = time.time()
print "Time to excute code",  t1-t0,"s"
