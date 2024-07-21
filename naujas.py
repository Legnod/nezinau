import random

#num = random.random()
#print(num)

#num = random.randint(1, 11)
#print(num)

#Pradzia
taskai = 0
zaidimas = True

#Sveikinimasir sunkumo pasirinkimas
print("Tu turesi atspeti koks yra slaptas skaicius, jai atspesi skaiciu, gausi 1 taska, ji pabaigsi zaidima tavo taskai bus surasyti, bdt jai tu nepabaigsi zaidimo ir pralaimesi, tavo taskai bus istrinti ir tu busi be tasku!")
sunkumas = int(input("Kokiu sunkumu nori Zaisti?(1-lengviausias, 5-sunkiausias)"))
at_pr = sunkumas+1
print("Tavo sunkumas yra", sunkumas)

#Zaidimas
while zaidimas == True:
	skaicius = random.randint(1, 10)
	at = skaicius - at_pr
	pr = skaicius + at_pr
	print("Skaicius kuri tu turesi atspeti yra tarp", at, "ir", pr)
	spejimas = int(input("Koks manai yra skaicius?"))
	if spejimas == skaicius:
		print("atspejai skaiciu!")
		taskai = taskai + 1
		print(taskai)
		testi = int(input("Ar nori testi zaidima?(1/0)"))
		if testi == 1:
			print("puiku!")
			zaidimas = True
		elif testi == 0:
			print("Gerai!, tu surinkai", taskai, "tasku")
			zaidimas = False
		else:
			print("Suvedei neteisingas instrukcijas")
			zaidimas = False
	elif spejimas != skaicius:
		print("Netspejai skaiciaus! Praradai visus taskus :(")
		zaidimas = False
	else:
		print("Neteisingai suvedei nurodymus!")
		zaidimas = False
