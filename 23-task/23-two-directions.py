def f(a, b, s):
	if a > 50 or a < 0:
		return 0, None
	if a == b:
		return (1, s)
	if a in s:
		return 0, None

	s.add(a)

	f1, s1 = f(a - 3, b, s)
	if f1 != 0:
		s = s1
	f2, s1 = f(a * 3, b, s)
	if f2 != 0:
		s = s1
	return (f1 + f2, s)

	
print(f(3, 30, set()))