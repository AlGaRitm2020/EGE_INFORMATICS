def f(a, b, s):
	if a >= b:
		return s
	if a % 2 ==0:
		s.add(a)

	n =  f(a + 3, b, s)
	k =  f(a * 3, b, n)
	s = k
	return s
print(len(f(3, 100, set())))