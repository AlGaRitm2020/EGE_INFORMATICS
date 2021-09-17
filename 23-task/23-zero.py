def pow_2(n):
	for i in range(n):
		if 2 ** i == n:
			return False
		if 2 ** i > n:
			return i - 1

def to_zero(n, i):
	return 2 ** i


def f(a, b):
	if a == b:
		return 1
	if a < b:
		return 0
	power = pow_2(a)
	if not power:
		return f(a - 1, b)
	return f(a - 1, b) + f(to_zero(a, power), b)

# print(bin(to_zero(int('0b11111', 2), pow_2(int('0b11111', 2)))))
print(f(64, 8))