# 1. Write a function named sum_to() that takes a number parameter n and returns the sum of the numbers from 1 to n. 

# for i in range(3,10):
# 	print(i)

def sum_to(number):
	sum = 0
	for i in range(1, number + 1):
		sum += i
	return sum

print(sum_to(10))


		

# 2. Write a function named largest() that takes a list parameter and returns the largest element in that list. You can assume the list contents are all positive numbers. 

def largest(list):
	 print(max(list))




largest([1,2,88])



# 3. Write a function named occurances() that takes two string parameters and counts the number of occurrances of the second string inside the first string. For example:

