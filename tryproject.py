lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
secret = "I hear the gooseberries are doing well this year, and so are the mangoes."
cipher = 7

   #encoded  = (secret + 7)%26
encoded = ''
for symbol in secret.lower():
    if symbol in lowercase_letters:
        num = lowercase_letters.find(symbol)
        num = (num+7) %26
        encoded = encoded + lowercase_letters[num]
    else:
       encoded= encoded + symbol
print(encoded)