def to_3(n):
	x = 0
	i = 0
	while n > 0:
		x += (n % 3) * 10 ** i 
		n //= 3
		i += 1
	return x

def f1(a, lvl, s):
	s.add(a)
	if lvl > 15:
		
		return s
	else:
		
		n = f1(to_3(a * 2), lvl + 1, s)
		s = n
		k = f1(to_3(a * 2 + 1),lvl + 1, s)
		s = k	
		return s



print(len(f1(1, 1, set())))