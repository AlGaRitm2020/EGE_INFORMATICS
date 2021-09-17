with open('../src/24-s1.txt', 'r', encoding='utf-8') as f:
	strings = f.readlines()

print(strings[2])
cnt = 0
for s in strings:
	for i in range(len(s) - 2):
		if s[i] == 'A' and s[i + 2] == "R":
			cnt += 1

print(cnt)