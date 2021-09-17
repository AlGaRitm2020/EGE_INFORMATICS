def f(n):
	n //= 2
	if n % 4 != 0:
		n = n * (16 + 10) * 16
		n = n * (16 * 15 + 1)
	else:
		n = n * (16 * 1 + 1) * (16 * 5) + 1
		n = n * 16 + 12
	return n

for i in range(1, 1000):
	if f(i) < 415030:
		print(i)

		