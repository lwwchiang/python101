lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
secret = "I hear the gooseberries are doing well this year, and so are the mangoes."
cipher = 7


   #for key in range(len(lowercase_letters)):
translated = ''
for symbol in secret.lower():
    if symbol in lowercase_letters:
        num = lowercase_letters.find(symbol)
        num = num - cipher
        if num < 0:
           num = num + len(lowercase_letters)
        translated = translated + lowercase_letters[num]
    else:
        translated = translated + symbol
print(translated)