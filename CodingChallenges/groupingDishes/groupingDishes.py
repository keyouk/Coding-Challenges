dishes = [["Salad", "Tomato", "Cucumber", "Salad", "Sauce"],
            ["Pizza", "Tomato", "Sausage", "Sauce", "Dough"],
            ["Quesadilla", "Chicken", "Cheese", "Sauce"],
            ["Sandwich", "Salad", "Bread", "Tomato", "Cheese"]]

def main():
	#initialize values in hash-table
	myDict = {}
	answer = []
	for dish in dishes:
		for i in dish[1:]:
			myDict[i] = []
	for dish in dishes:
		for ingredient in dish[1:]:
			myDict[ingredient].append(dish[0])
	#insert main ingredient into zero index of ingredient list and append to answer[]
	for ingredient in myDict:
		myDict[ingredient].insert(0, ingredient)
		if len(myDict[ingredient]) > 2:
			answer.append(myDict[ingredient])
	#sort lexiographicallys
	print sorted(answer)


if __name__ == '__main__':
	main()