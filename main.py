import random
from replit import clear as cl

g = False
t = 0

def start():
	global pwd
	pwd = input("Enter a number less than 100000000 = ")
	if len(pwd) > 8 or pwd == "" or not pwd.isdigit():
		return False
	else:
		return True

def guess():
	global g, t, pwd
	l = len(pwd)

	while g == False:
		cl()
		
		gu = random.randint((l - 1) * 10, int(l * "9"))
		t += 1
		cl()
		print(pwd)
		print(gu)
		if gu == int(pwd):
			cl()
			print("Your password was " + str(gu) + "\nIt took the computer " + str(t) + " tries only")
			g = True
			break 

while not g:
	g = start()
	cl()
g = False
guess()
