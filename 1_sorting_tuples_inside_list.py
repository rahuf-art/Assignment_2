# Get the size of tuples from the user
size_of_tuples = int(input("Enter the number of tuples: "))

# Initialize empty lists to store the tuples
tuples_list = []
swap_list=[]


# Get user input for each tuple
for i in range(size_of_tuples):
    element1 = input(f"Enter the first element for tuple {i + 1}: ")
    element2 = input(f"Enter the second element for tuple {i + 1}: ")
    # Create a tuple and append it to the list
    tuples_list.append((element1, element2))
    swap_list.append((element2,element1))

print("Entered list is :",tuples_list)
sorted_swap_list=sorted(swap_list)

# Swap tuple elements in list of tuples

result = []
for i in sorted_swap_list:
	x, y = i
	result.append((y, x))
		
# printing result
print("The sorted tuple list is : " + str(result))

