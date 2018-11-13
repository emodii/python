loop = True

while loop == True:

	print("------------")
	answer = input("Zahl in Hexadezimal, Binär oder Octal ausgeben? [Hex, Bin, Oct] ")
	
	if answer == "Hex" or answer  == "Hexadezimal":
		wert = int(input('Zahl in Hex umwandeln:'))
		x = hex(wert)
		print("  Hex-Wert: " + x)
		
		skip = input("Zum Weitermachen [Enter] drücken, andere Taste zum aufhören. ")
		if skip == "":
			loop = True
		else:
			break
			
	if answer == "Bin" or answer == "Binär":
		wert2 = int(input('Zahl in Bin umwandeln:'))
		y = bin(wert2)
		print("  Bin-Wert: " + y)
		
		skip = input("Zum Weitermachen [Enter] drücken, andere Taste zum aufhören. ")
		if skip == "":
			loop = True
		else:
			break
			
	if answer == "Oct" or answer == "Octal":
		wert3 = int(input('Zahl in Oct umwandeln:'))
		z = oct(wert3)
		print("  Oct-Wert: " + z)
		
		skip = input("Zum Weitermachen [Enter] drücken, andere Taste zum aufhören. ")
		if skip == "":
			loop = True
		else:
			break 
