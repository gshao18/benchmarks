#Source: https://github.com/attractivechaos/plb2/blob/master/src/python/nqueen.py

#!/usr/bin/env python

import time

def nq_solve(n):
	m = 0
	a = [-1] * n
	l = [0] * n
	c = [0] * n
	r = [0] * n
	y0 = (1<<n) - 1
	k = 0
	while k >= 0:
		y = (l[k] | c[k] | r[k]) & y0;
		if (y ^ y0) >> (a[k] + 1):
			i = a[k] + 1
			while i < n:
				if (y & 1<<i) == 0: break
				i += 1
			if k < n - 1:
				z = 1<<i
				a[k] = i
				k += 1
				l[k] = (l[k-1]|z)<<1
				c[k] = c[k-1]|z
				r[k] = (r[k-1]|z)>>1
			else:
				m += 1
				k -= 1
		else:
			a[k] = -1
			k -= 1
	return m

def main():
	for i in range (4):
		start = time.time()
		print(nq_solve(15))
		end = time.time()
		execution_time = end - start
		print(str(round(execution_time, 4)).replace(".",","))

if __name__ == '__main__': main()
