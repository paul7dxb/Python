# Counts the frequency of lowercase letters occuring in a file
# Works with files where the words are seperated by spaces or new lines
# Prints frequency of each letter to console after counting
# Default filename is testnote.txt but you can change this at the commented line below

alphabet = list('abcdefghijklmnopqrstuvwxyz ')

alphaCounter = [0] * 27

print(alphaCounter)


f = open("testnote.txt", "r")  # Change file name here
lines = f.read()

for i, letter in enumerate(lines):
	if(letter != '\n'):
		pos = alphabet.index(letter)
		#print(pos)
		alphaCounter[pos] += 1


print(f'Finished:\n')
print(alphaCounter)

print("letter : frequency")
for i, letter in enumerate(alphabet):
	print(f'{letter} : {alphaCounter[i]}')