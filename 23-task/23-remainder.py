def f(a, b, comm):
	if comm > 5:
		return 0
	if a == b:
		return 1
	if a >b:
		return 0

	return int(any([f(a + 1, b, comm + 1), f(a * 2, b, comm + 1), f(a + a % 4, b, comm + 1)]))

ans = 0
for i in range(-10, 80):
	ans += f(i, 80, 0)

print(ans)