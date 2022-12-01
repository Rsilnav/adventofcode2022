def solve(data):
	calories = []
	temp = 0
	for item in data:
		if item == '':
			calories.append(temp)
			temp = 0
		else:
			temp += int(item)
	return sum(sorted(calories)[::-1][:3])


if __name__ == '__main__':
	with open("input.txt", "r") as f:
		data = f.read().splitlines()
		print(solve(data))