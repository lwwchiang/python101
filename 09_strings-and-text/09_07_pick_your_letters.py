# Use string indexing and string concatenation
# to write the sentence "we see trees" only by picking
# the necessary letters from the given string.

word = "tweezers "
word1 = word[1:3]
word2 = word[-2]
word3 = word[2:4]
word4 = word[0]+word[-3]+word3+word[-2]

print(word1+" "+word2+word3+" "+word4)
