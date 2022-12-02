def solve(data):
	total = 0
	for item in data:
		temp = 0
		x, y = item.split()
		a, b = ord(x) - ord("A"), ord(y) - ord("X")
		temp += b * 3
		b2 = (a + b - 1) % 3
		temp += b2 + 1
		total += temp
	return total

if __name__ == '__main__':
	with open("input.txt", "r") as f:
		data = f.read().splitlines()
		print(solve(data))