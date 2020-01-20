def shell_sort(input_list):
	gap = len(input_list)//2
	while gap >= 1:
		for i in range(0, len(input_list) - gap):
			while input_list[i] > input_list[i+gap]:
				input_list[i], input_list[i+gap] = input_list[i+gap], input_list[i]
				if i - gap >= 0:
					i = i - gap
		gap = gap//2



if __name__ == '__main__':

	input_list = [1, 3, 5, 2, 4, 8, 14, 0, 6, 7]

	shell_sort(input_list)

	print(input_list)