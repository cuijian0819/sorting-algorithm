
def merge_sort(input_list):
	if len(input_list) <= 1:
		return input_list

	mid_point = len(input_list)//2

	left_list = merge_sort(input_list[:mid_point])
	right_list = merge_sort(input_list[mid_point:])

	left_len = len(left_list)
	right_len = len(right_list)

	left_index = 0
	right_index = 0
	return_index = 0

	while left_index < left_len and right_index < right_len:
		if left_list[left_index] < right_list[right_index]: 
			input_list[return_index] = left_list[left_index]
			left_index += 1
		else: 
			input_list[return_index] = right_list[right_index]
			right_index += 1
		return_index += 1

	while left_index < left_len:
		input_list[return_index] = left_list[left_index]
		left_index += 1
		return_index += 1

	while right_index < right_len:
		input_list[return_index] = right_list[right_index]
		right_index += 1
		return_index += 1

	return input_list



if __name__ == '__main__':

	input_list = [1, 3, 5, 2, 4, 6, 7]

	merge_sort(input_list)

	print(input_list)
