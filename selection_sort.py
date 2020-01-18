
def selection_sort(input_list):
	for i in range(len(input_list)):
		least = i
		for j in range(i+1, len(input_list)):
			if input_list[j] < input_list[i]:
				least = j
		input_list.insert(i, input_list[least])
		del input_list[least+1]




if __name__ == '__main__':

	input_list = [1, 3, 5, 2, 4, 6, 7]

	selection_sort(input_list)

	print(input_list)