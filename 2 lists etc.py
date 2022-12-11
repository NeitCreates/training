numbers_list = [2, 6, 8, 17, 56]
names_list = ["Mud", "Muk", "Dick", "Ändy"]

print("Here are the names as a data structure", names_list)

print("Here are the names as a real list")
for i in names_list:
	print(i)

# names_list.append(input("Add a new name to existing list\n"))
# print(names_list)

print("Adding Sunny \n... \ndone!")
names_list.insert(1, "Sunny")
print(names_list)

print("Looking for Ändy and his index, it's", names_list.index("Ändy"))

newlist = numbers_list.copy()
newlist.extend(names_list)
print("New list created from two previous:\n", newlist)
