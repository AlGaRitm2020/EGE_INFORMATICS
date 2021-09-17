def f(n):
	if n % 2 == 0:
		n = n * 4
		n = n + 1
	else:
		n = n * 4
		n = n + 2
	return n

for i in range(1000):
	if f(i) > 138:
		print(i)
		break