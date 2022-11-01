def sort_dictionary(dict):
	sortedByAgeList = sorted(dict.items(), key = lambda x: x[1][1])
	finalListofTup = []

	for a, b, in sortedByAgeList:
		finalListofTup.append((a, b[0]))
	return finalListofTup
