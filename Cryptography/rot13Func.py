'''
This tool can be used to brute force rotational mono-alphabetical subsitution cipher
Meaning the rotation works from a-z and A-Z ignoring punctuation
This is most commonly seen with ROT13 but this tool will show the output from 
all rotation number values 1 to 25. This covers all transformation values as 26 would
transform to itself looping around the alphabet

For all character / ASCII transformation look at a ROT47 tool
'''

def rotFunc(inputChar, rotNumber, lowerBound, upperBound):
	modNum = upperBound - lowerBound + 1
	inputNum = ord(inputChar)
	x = inputNum - lowerBound
	x = (x - rotNumber) % modNum
	asciiNum = x + lowerBound
	return chr(asciiNum)

# Change value of messageString to your ROT cipher text
messageString = "Guvf vf zl rknzcyr grkg. N ybg bs PGSf hfr ebg13 be fbzr bgure ahzore naq guvf svyr pna uryc qrgrezvar gur bevtvany cynvag grkg"

for rotNumber in range(1,26):
	asciiString = []

	#Ascii upper 65:A - 90:Z
	#Asii lower 97:a - 122:z

	for cipherLetter in messageString:
		#Get Ascii number
		asciiNum = ord(cipherLetter)

		#Uppercase
		if asciiNum >= 65 and asciiNum <=90 :
			asciiLetter = rotFunc(cipherLetter, rotNumber, 65, 90)

		#lowercase
		elif asciiNum >= 97 and asciiNum <=122 :
			asciiLetter = rotFunc(cipherLetter, rotNumber, 97, 122)

		#Others no change
		else:
			asciiLetter = cipherLetter

		asciiString.append(asciiLetter)

	result = ''.join(asciiString)
	print(f'Result for rot{rotNumber}:\n{result}\n')