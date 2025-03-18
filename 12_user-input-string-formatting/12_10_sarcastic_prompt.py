# Create a sarcastic program that asks a user for their honest opinion,
# then prints the same sentence back to them in aLtErNaTiNg CaPs.

opinion = input("Enter opinion:")
res = ""

for i in range(len(opinion)):
    if not i % 2:
        res += opinion[i].lower()
    else:
        res += opinion[i].upper()
print(res)