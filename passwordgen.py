#passwordgenerator_01 
#passwordgenerator_01 

####################################################


#Import
import random
import time
import os
from colorama import Fore, init
from progress.bar import Bar 
from docx import Document 
import datetime

#variblen:
password = ""
chars2 = "abcdefghijklmnopqrstuvwxyziABCDEFGHIJKLMNOPQRSTUVWXYZ"
chars1 = "1234567890"
chars3 = "abcdefghijklmnopqrstuvwxyziABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890?!$%&/=*+~,.;:<>-_abcdefghijklmnopqrstuvwxyziABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890?!$%&/=*+~,.;:<>-_"
chars4 = "10"
Datum = datetime.datetime.now()
Readme = "\Readme.txt"
File_Destination = "C:/Users/twore/Desktop/Python/Password_Gen/Passsword.txt"
#Start
init()

#Letters
#nLength_max = 257

#Start screen
print   (Fore.RED)
print 	('##################################################################')
print	(' __          __  _                           ' )
print	(' \ \        / / | |                          ' )
print	('  \ \  /\  / /__| | ___ ___  _ __ ___   ___  ' )
print	('   \ \/  \/ / _ \ |/ __/ _ \|  _ ` _ \ / _ \ ' )
print	('    \  /\  /  __/ | (_| (_) | | | | | |  __/ ' )
print	('     \/  \/ \___|_|\___\___/|_| |_| |_|\___| ' )
print 	('##################################################################')
print 	(Fore.WHITE)
print 	('1		Create Passwort')
print 	('2		Open Readme ')
print 	('Your choice')
Start = raw_input(':')
if Start == "2":
	print (os.system(Readme))

elif Start == "1":
	print ('##################################################################')
	print ('How many characters should it have?')
	Length = int(raw_input(':'))
	print("Input a specific start if you want")
	Anfang = raw_input(":")

	print	('Which combination do you want ?')
	print	(Fore.RED+'1. Easy			PW:		only numbers')
	print	(Fore.YELLOW+'2. Medium		PW:		only etters')
	print	(Fore.GREEN+'3. Strong		PW:		letters,numbers,special characters')
	print	(Fore.WHITE+'4. Binary		PW:		only 0 and 1')
	Letters = raw_input(':')
	print("")
	if Letters == "1":
		print("Your characters = \n \n"+ Fore.RED + chars1)
		print(Fore.WHITE)
		while len(password) != Length:
			bar = Bar('will generate', max=Length)
			for i in range(Length):

				password = password + random.choice(chars1)
				bar.next()
				if len(password) == Length:	
					print("\n \n Password: ")
					print("")
					print(Fore.RED+Anfang + password)	
					print(Fore.WHITE)

	
	
	if Letters == "2":
		print("Your characters = \n \n"+ Fore.RED + chars2)
		print(Fore.WHITE)
		while len(password) != Length:
			bar = Bar('will generate', max=Length)
			for i in range(Length):

				password = password + random.choice(chars2)
				bar.next()
				if len(password) == Length:	
					print("\n \n Password: ")
					print("")
					print(Fore.RED+Anfang + password)	
					print(Fore.WHITE)

	if Letters == "3":
		print("Your characters = \n \n"+ Fore.RED + chars3)
		print(Fore.WHITE)
		while len(password) != Length:
			bar = Bar('will generate', max=Length)
			for i in range(Length):

				password = password + random.choice(chars3)
				bar.next()
				if len(password) == Length:	
					print("\n \n Password: ")
					print("")
					print(Fore.RED+Anfang + password)	
					print(Fore.WHITE)

	if Letters == "4":
		print("Your characters = \n \n"+ Fore.RED + chars4)
		print(Fore.WHITE)
		while len(password) != Length:
			bar = Bar('will generate', max=Length)
			for i in range(Length):

				password = password + random.choice(chars4)
				bar.next()
				if len(password) == Length:	
					print("\n \n Password: ")
					print("")
					print(Fore.RED+Anfang + password)	
					print(Fore.WHITE)

	file = open(File_Destination,"w")
	print("Do you want to save it ? \n "+Fore.GREEN+"yes = yes"+Fore.RED+" \n no = no input"+Fore.WHITE)
	Speicher= raw_input(":")
	if Speicher == "yes":
		file.write(Anfang+password)
		time.sleep(0.5)
		print("\n Password was saves corectly ! \n ")
	print	("")
	print	('To exit the programm press '+Fore.GREEN+'ENTER'+Fore.WHITE)
	Ende = raw_input()
#Fertig

