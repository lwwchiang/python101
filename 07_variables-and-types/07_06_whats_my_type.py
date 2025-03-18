# What data type is the variable `mystery` at the end of the script?
# What data types does it hold at certain points earlier in the script?

mystery = None
print(type(mystery))
mystery = "Sommerfeld"
mystery = 137
mystery = mystery + 0.0
print(type(mystery))

counter = 0
sum = 0
while (counter < 10):
	sum += counter
	counter += 3
print(counter)
print(sum)
