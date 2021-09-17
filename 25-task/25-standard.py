def is_prime(n):
	dividers = []
	for i in range(2, n // 2 + 1):
		if n % i == 0:
			dividers.append(i)

	if len(dividers) == 2:
		return dividers
	return False
	
res = []
for i in range(174457, 174505):
	f = is_prime(i)
	if f:
		res.append(f)


res.sort(key=lambda x: x[0] * x[1])
print(res)