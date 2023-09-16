# source geeksforgeeks
# https://www.geeksforgeeks.org/python-lambda-anonymous-functions-filter-map-reduce/

List = [[2,3,4],[1, 16, 4, 64],[3, 12, 6, 9]]

# Sort each sublist
sortList = lambda x: (sorted(i) for i in x)

# Get the second largest element
secondLargest = lambda x, f : [y[len(y) - 1] for y in f(x)]
	# same as def func, after : = return value [] = list
	# f = function, x = parameter
	# y = y in sorted list
res = secondLargest(List, sortList)

print(res)
