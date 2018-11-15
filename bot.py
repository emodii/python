import socket
import random
from weather import Weather, Unit
import webbrowser
import os
import time
import string

clear = lambda: os.system('cls')
clear()

# Daten für den Loop
def end():		
	skip = input()
	if skip == "":
		loop = True
	else:
		sys.exit()

# Anfang des Programmes, Definierung des User-Namens
print("Bot: Hallo, wie ist dein Name?")
n = input("Ich: " )
print ("Bot: Schön dich kennen zu lernen " + n + "! ")

# Loop Aktivierung
loop = True
while loop == True:

	
# Infos for random
	r = 0
	answ = ["Stell mir eine Frage.", "Hast du eine weitere Frage?", "Erzähl mir etwas oder frag mich etwas.", "Was interessiert dich?"]
	r = random.randint(0,3)
	answ2 = answ[r]

# Question and User Input
	print("Bot: " + "%s" % answ2)
	next = input(n + ": ")

# Different answers on different questions
	if next == "Wie geht es dir?" or next == "Wie gehts?" or next == "Wie gehts dir?":
		print("Bot: Mir geht es gut, danke der Nachfrage.")
		end()

	if next == "Magst du mich?" or next == "Wie findest du mich?":
		print("Bot: Ich kenne dich kaum, aber du wirkst sehr freundlich.")
		end()
			
	if next == "Wer ist dein Besitzer?" or next == "Wer hat dich produziert?":
		print("Bot: Mein Besitzer und Entwickler ist Josua G. auch "emodi" genannt. Er entwickelte mich als Experiment in 2018.")
		end()

	if next == "Wie spät ist es?" or next == "Uhrzeit":
		print("Bot: Es Ist " + time.strftime('%H:%M:%S') + " Uhr.")
		end()
			
	if next == "Wie funktionierst du?" or next == "In welcher Programmiersprache bist du geschrieben?" or next == "Was bist du?":
		print("Bot: Ich wurde mit Python geschrieben, das Konzept meiner künstlichen Intelligenz ist relativ simpel, da ich nur aus If-Funktionen bestehe. Dadurch überfordern mich bisher Komplexere fragen auch noch.")
		end()
			
	if next == "Kannst du mir eine IP einer Website nennen?" or next == "Ip Website":
		print("Bot: Gib mir einfach den Link, dann kann ich dir die IP zeigen!")
		host = input(n + ": ")
		ip = socket.gethostbyname(host)
		print("Bot: Die IP für " + host + " lautet " + ip)
		end()
			
	if next == "Kannst du für mich rechnen?" or next == "rechnen":
		print("Bot: Gib mir deine Rechnung und ich löse sie für dich.")
		erste = int(input("KI: Gib deine erste Zahl ein: "))
		oper = input("KI: Gib deinen Operator ein: ")
		zweite = int(input("KI: Gib deine zweite Zahl ein: "))
		print("Bot: Deine Lösung ist: ")
		if (oper == "-"):
			loesung =  erste - zweite
			print(loesung)
		elif (oper == "+"):
			loesung = erste + zweite
			print(loesung)
		elif (oper == "/"):
			loesung = erste / zweite
			print(loesung)
		elif (oper == "*"):
			loesung = erste * zweite
			print(loesung)
		else:
			print("Bot: Falscher Operator verwendet.")
		end()
	
	if next == "Gib mir eine Zahl in Hexadezimal an" or next == "Zahl in Hex" or next == "Hex" or next == "Gib mir eine Zahl in Hex":
		print("Bot: Gebe die Zahl ein, die du in Hexadezimal möchtest.")
		wert = int(input("Zahl: "))
		x = hex(wert)
		print("Bot: Der Hex-Wert ist " + x)
		end()
	
	if next == "Gib mir eine Zahl in Binär an" or next == "Zahl in Bin" or next == "Bin" or next == "Gib mir eine Zahl in Binär":
		print("Bot: Gebe die Zahl ein, die du in Binär möchtest.")
		wert = int(input("Zahl: "))
		x = bin(wert)
		print("Bot: Der Bin-Wert ist " + x)
		end()
	
	if next == "Gib mir eine Zahl in Octal an" or next == "Zahl in Octal" or next == "Oct" or next == "Gib mir eine Zahl in Octal":
		print("Bot: Gebe die Zahl ein, die du in Octal möchtest.")
		wert = int(input("Zahl: "))
		x = oct(wert)
		print("Bot: Der Oct-Wert ist " + x)
		end()
	
	if next == "Wie ist das Wetter?" or next == "Wetter":
		print("Bot: Für welche Stadt möchtest du diese Information?")
		stadt = input(n + ": ")
		weather = Weather(unit=Unit.CELSIUS)
		location = weather.lookup_by_location(stadt)
		condition = location.condition
		print("Bot: Es ist " + condition.text)
		end()
			
	if next == "Wie ist das Wetter in den nächsten Tagen?" or next == "Wie wird das Wetter die nächsten Tage sein?" or next == "Wetter nächste Tage":
		print("Bot: Für welche Stadt möchtest du diese Information?")
		stadt = input(n + ": ")
		weather = Weather(unit=Unit.CELSIUS)
		location = weather.lookup_by_location(stadt)
		forecasts = location.forecast
		print("KI: Das Wetter der nächsten Tage: ")
		for forecast in forecasts:
			print(forecast.text)
			print(forecast.date)
			print(forecast.high)
			print(forecast.low)
		end()
			
	if next == "Öffne mir eine Website" or next =="Website":
		print("Bot: Gib bitte eine Webadresse ein, die du öffnen möchtest.")
		new = 2 
		url = input(n + ": ")
		webbrowser.open(url,new=new)
		end()
	
	if next == "Text KI" or next == "Text herausfinden":	
		possibleCharacters = string.ascii_lowercase + string.digits + string.ascii_uppercase + ' .,!?;:'
		target = input("Gib deinen Zieltext ein: ")
		attemptThis = ''.join(random.choice(possibleCharacters) for i in range(len(target)))
		attemptNext = ''
		completed = False
		generation = 0
		while completed == False:
			print(attemptThis)
			attemptNext = ''
			completed = True
			for i in range(len(target)):
				if attemptThis[i] != target[i]:
					completed = False
					attemptNext += random.choice(possibleCharacters)
				else:
					attemptNext += target[i]
			generation += 1
			attemptThis = attemptNext
			time.sleep(0.05)
		print("Zielwort erreicht. Das hat " + str(generation) + " Generationen gebraucht")
		end()
			
	if next == "show command list" or next == "help":
		print("---------------------")
		print("KI: Hier sind meine Verfügbaren Commands, die du eingeben kannst:")
		thislist = thislist = ["Wie geht es dir?", "Wie gehts?", "Magst du mich?", "Wie findest du mich?", "Was bist du?", "Wer ist dein Besitzer?", "Wer hat dich produziert?", "Wie funktionierst du?", "In welcher Programmiersprache bist du geschrieben?", "Wie spät ist es?", "Uhrzeit", "Öffne mir eine Website", "Website", "Wie ist das Wetter in den nächsten Tagen?", "Wetter nächste Tage", "Wie ist das Wetter?", "Wetter", "Kannst du für mich rechnen?", "rechnen", "Kannst du mir eine IP einer Website nennen?", "Ip Website", "Text KI", "Text herausfinden", "Gib mir eine Zahl in Octal an", "Zahl in Octal", "Oct", "Gib mir eine Zahl in Octal", "Gib mir eine Zahl in Binär an", "Zahl in Bin", "Bin", "Gib mir eine Zahl in Binär", "Gib mir eine Zahl in Hexadezimal an", "Zahl in Hex", "Hex", "Gib mir eine Zahl in Hex", "Ende", "beenden", "exit"]
		for x in thislist:
		  print(x)
		end()
				
	if next == "Ende" or next == "beenden" or next == "exit" or next == "Tschüss":
		print("KI: einen schönen Tag dir noch.")
		break
		
