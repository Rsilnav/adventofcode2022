def get_priority(letter):
	num = ord(letter)
	if num <= ord("Z"):
		return num - ord("A") + 27
	elif num <= ord("z"):
		return num - ord ("a") + 1

def solve(data):
	total = 0
	for item in data:
		size = len(item)//2
		a, b = item[:size], item[size:]
		wrong = set(a).intersection(b)
		assert len(wrong) == 1
		total += get_priority(list(wrong)[0])
	return total

if __name__ == '__main__':
	with open("input.txt", "r") as f:
		data = f.read().splitlines()
		print(solve(data))