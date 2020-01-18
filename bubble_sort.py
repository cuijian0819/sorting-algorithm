def bubble_sort(input_list):
	while(1):
		swapped = False
		for i in range(len(input_list)-1):
			if input_list[i] > input_list[i+1]:
				input_list[i], input_list[i+1] = input_list[i+1], input_list[i]
				swapped = True
		if not swapped:
			break



if __name__ == '__main__':

	input_list = [1, 3, 5, 2, 4, 6, 7]

	bubble_sort(input_list)

	print(input_list)