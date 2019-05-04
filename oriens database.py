#!/usr/bin/python
import os
clean = lambda: os.system("clear")
clean 
members = ["dk","ph","jack","mf","rudra","aron","smit","rahman","mahi","andy"]
permission = raw_input("I need to know who is trying to access may I? y/n ")
if permission == "y":
	user = raw_input("your name : ")
	print ("please wait let me check the data entry and verify you can enter")
	print (line)
	print ("###############################################################################################################")
	if user in members:
		print ("you are authenticated")
		print ("welcome " + user)
		print ("running user authentication 2 please hold on..............")
		print ("###########################################################################################################")
		passw = raw_input("enter the password please: ")
		if passw == "0r13N":
			print ("###############################################################################################################")
			print ("user authentication 2 successfull")
			print ("###############################################################################################################")
			entr = raw_input("type enter to continue ")
			if entr == "enter":
				clean()
				print ("1.show member list")
				print ("2.view your database")
				choice = input("enter your choice ")
				if choice == 1:
					print ("1.dk")
					print ("2.ph")
					print ("3.jack")
					print ("4.mf")
					print ("5.rudra")
					print ("6.aron")
					print ("7.smit")
					print ("8.mahi")
					print ("9.andy")
				else:
					if user == "dk":
						print ("##################################################")
						print ("founder and creater of me")
						print ("##################################################")
					elif user == "ph":
						print ("cofounder and an asshole")
					elif user == "jack":
						print ("DK's friend")
					elif user == "mf":
						print ("future scripter")
					elif user == "rudra":
						print ("younger one my bro")
					elif user == "aron":
						print ("dude from tamilnadu")
					elif user == "smit":
						print ("firsst one to be interviewed family guy")
					elif user == "mahi":
						print ("pretty active bird")
					elif user == "andy":
						print ("programmer")
					else:
						print ("you hacked me?")
					print ("MEMBERS LIST")
					print (members)
			else:
				print ("please type the write spelling of enter you idiot")
		
		else:
			print ("sorry you are not authenticated")
	else:
		print ("sorry not authenticated")
else:
	print("##############################")
	clean()
        print ("############3###############FUCK###############")
	print ("fuck you")
	print ("###########################FUCK##FUCK##FUCK##FUCK")
	exit
	
