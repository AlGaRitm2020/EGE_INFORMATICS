def not_divide(n, list):
	for i in list:
		if n % i == 0:
			return False
	return True

p = range(1016, 7937)

not_div = [7, 17, 19, 27]
ans = []

for i in p:
	if i % 3 == 0 and not_divide(i, not_div):
		ans.append(i)
print(len(ans), max(ans))
