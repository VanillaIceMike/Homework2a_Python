def swap_list(list):
	n = len(list)
	m = n / 2
	p = round(m)
	middle = int(p)
	list[middle - 1], list[n - 1] = list[n - 1], list[middle - 1]
	return list
