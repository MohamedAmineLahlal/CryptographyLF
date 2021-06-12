import time

Letters = {
	"A":0,
	"B":1,
	"C":2,
	"D":3,
	"E":4,
	"F":5,
	"G":6,
	"H":7,
	"I":8,
	"J":9,
	"K":10,
	"L":11,
	"M":12,
	"N":13,
	"O":14,
	"P":15,
	"Q":16,
	"R":17,
	"S":18,
	"T":19,
	"U":20,
	"V":21,
	"W":22,
	"X":23,
	"Y":24,
	"Z":25,
}


def fun_cryp_remainder(letter):
	x = Letters[letter]
	return ((17*int(x))+7)%26

def fun_decryp_remainder(letter):
	y = Letters[letter]
	return (21-(3*y)%26)

def GetLetter(val):
   for key, value in Letters.items():
      if val == value:
         return key

Word_to_crypt = input("Word to crypt : ")
Word_to_crypt = Word_to_crypt.upper()

Encryption_Restes = []

for i in Word_to_crypt:
	Encryption_Restes.append(fun_cryp_remainder(i))

Encryption_result = []

print("Crypting...")
time.sleep(0.5)
print("Result : ", end="")

for i in Encryption_Restes:
	print(GetLetter(int(i)), end="")
	Encryption_result.append(GetLetter(int(i)))


Decryption_Restes = []

for i in Encryption_result:
	Decryption_Restes.append(fun_decryp_remainder(str(i)))

print("\nDecrypting...")
time.sleep(1.5)
print("Result : ", end="")


for i in Decryption_Restes:
	print(GetLetter(int(i)), end="")





