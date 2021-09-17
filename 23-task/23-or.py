def f1(a, b):
	if a == b:
		return 1
	if a == 23:
		return 0
	if a > b:
		return 0
	if a < b:
		return f1(a + 1, b) + f1(a + 2, b)


def f2(a, b):
	if a == b:
		return 1
	if a == 17:
		return 0
	if a > b:
		return 0
	if a < b:
		return f2(a + 1, b) + f2(a + 2, b)

def f3(a, b):
	if a == b:
		return 1

	if a > b:
		return 0
	if a < b:
		return f3(a + 1, b) + f3(a + 2, b)


print(f1(11, 17) * f1(17, 29) + f2(11, 23) * f2(23, 29) + f3(11, 17) * f3(17, 23) * f3(23, 29))