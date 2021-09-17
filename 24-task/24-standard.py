with open('../src/24.txt', 'r', encoding='utf-8') as f:
	seq = f.read()

list = []
str = ''
for i in range(len(seq)):
	if seq[i].isdigit():
		str += seq[i]
	else:
		if str:
			list.append(str)
		str = ''
print(list)

list = [int(i) for i in list if int(i) % 2 == 0]
print(max(list))
