import os
import random
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
RESET = '\033[0m'

archivo = open("palabras.txt", "r")
a = archivo.read().split("\n")
word_split = list(a[random.randint(0,len(a) - 1)])

print(word_split)

historial = []

for trys in range(5):
	os.system("clear")
	
	print("Intentos restantes: {}".format(5 - trys))
	
	for i in historial:
		for j in i:
			print(j, end="")
		print()

	input_word = list(input(RESET))

	correct_positions = []
	bad_positions = []
	used = word_split.copy()
	repetet = []

	for i in range(5):
		if word_split[i] == input_word[i]:
			correct_positions.append(i)
			used.remove(word_split[i])


	for i in range(5):
		if input_word[i] in word_split and i not in correct_positions and input_word[i] in used:
			bad_positions.append(i)
			used.remove(input_word[i])

	colored_result = []

	for i in range(5):
		if i in correct_positions:
			colored_result.append("{}{}".format(GREEN, input_word[i]))
		elif i in bad_positions:
			colored_result.append("{}{}".format(YELLOW, input_word[i]))
		else:
			colored_result.append("{}{}".format(RED, input_word[i]))

	historial.append(colored_result)

	
	if input_word == word_split:
		break

if input_word == word_split:
	os.system("clear")
	print("Has acertado")
	for i in historial:
		for j in i:
			print(j, end="")
		print()
else:
	print("Has perdido, la palabra era '{}'".format("".join(word_split)))


