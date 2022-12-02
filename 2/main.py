dic = {"X": "A", "Y": "B", "Z": "C"}
def solve(data):
	total = 0
	for item in data:
		temp = 0
		x, y = item.split()
		y = dic[y]
		a, b = ord(x), ord(y)
		t = (a - b) % 3

		match t:
			case 0:
				temp += 3
			case 1:
				temp += 0
			case 2:
				temp += 6

		temp += b - ord("A") + 1
		total += temp
	return total


if __name__ == '__main__':
	with open("input.txt", "r") as f:
		data = f.read().splitlines()
		print(solve(data))