import random

def quick_sort(input_list):
	greater = []
	less = []
	if len(input_list) <= 1:
		return input_list
	else: 
		pivot = random.choice(input_list);
		for element in input_list:
			if element == pivot:
				continue
		
			if element > pivot:
				greater.append(element)
			else:
				less.append(element)
		
		return quick_sort(less) + [pivot] + quick_sort(greater)




if __name__ == '__main__':

	input_list = [1, 3, 5, 2, 4, 6, 7]

	sorted_list = quick_sort(input_list)

	print(sorted_list)
