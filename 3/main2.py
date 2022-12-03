def get_priority(letter):
	num = ord(letter)
	if num <= ord("Z"):
		return num - ord("A") + 27
	elif num <= ord("z"):
		return num - ord ("a") + 1

def solve(data):
	total = 0
	for i in range(0, len(data)//3, 1):
		badge = set(data[3*i]).intersection(data[3*i+1]).intersection(data[3*i+2])
		assert len(badge) == 1
		total += get_priority(list(badge)[0])
	return total

if __name__ == '__main__':
	with open("input.txt", "r") as f:
		data = f.read().splitlines()
		print(solve(data))