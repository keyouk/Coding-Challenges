def sortByHeight(a):
	order = [x for x in a if x != -1]
	order.sort()
	for tree in range(a.count(-1)):
		order.insert(a.index(-1), -1)
		del a[a.index(-1)]

	return order