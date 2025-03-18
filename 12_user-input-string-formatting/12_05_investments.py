# Take in the following three values from the user:
# 1. investment amount
# 2. interest rate in percentage
# 3. number of years to invest
#
# Calculate the future values and print them to the console.

invest = input("Enter investment amout: ")
rate = input("Enter interest rate: ")
year = input("Enter number of years to invest: ")

future_value = int(invest)*(float(rate)+1)*int(year)
print(future_value)