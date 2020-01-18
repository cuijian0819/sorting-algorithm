def insertion_sort(input_list):
	for i in range(len(input_list)):
		for j in range(0,i):
			if input_list[i] > input_list[j]:
				continue
			else:
				input_list.insert(j, input_list[i])
				del input_list[i+1]




if __name__ == '__main__':

	input_list = [1, 3, 5, 2, 4, 6, 7]

	insertion_sort(input_list)

	print(input_list)