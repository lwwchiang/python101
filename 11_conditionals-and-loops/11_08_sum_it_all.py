# Using a loop, sum all numbers from the `start` to the `stop` number.
# The sequence should consist only of integers from 1 to 100.
# The output of your calculation should look like this:
#
#      The sum is: 5050

start = 1
stop = 100

sum = 1
for i in range(start,stop+1):
    sum += i
print(sum)  

mul=1
for i in range(start,stop+1):
    mul*=i
print(mul)