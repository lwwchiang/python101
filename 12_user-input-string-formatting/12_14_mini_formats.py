# Use Python's string mini-language to display the table
# that you've built before in a slightly better formatted manner:
#
#  0  1  2  3  4  5  6  7  8  9
# 10 11 12 13 14 15 16 17 18 19
# 20 21 22 23 24 25 26 27 28 29
# 30 31 32 33 34 35 36 37 38 39
# 40 41 42 43 44 45 46 47 48 49

for i in range(0,10):
    print(f"{i:>3}",end="")
print()
for i in range(10, 20):
    print(f"{i:3}",end="")
print()
for i in range(20,30):
    print(f"{i:3}",end="")
print()
for i in range(30,40):
    print(f"{i:3}",end="")
print()
for i in range(40,50):
    print(f"{i:3}",end="")
print()