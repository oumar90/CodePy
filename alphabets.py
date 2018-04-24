#calcul d'entropie
def entropie(n):
	return (math.log2(n))
		
#cacul de longueur minimum		
def longueurmin(entropie):
	return entropie/math.log2(n)

#calcul de rendement
def rendement(longueurmin, longueurmoy):
	return longueurmin/longueurmoy	
	
#pour stocker l'alphabet
alphabet = ""


alphabet1 = input("entrer l'alphabet :")
alphabet = alphabet1
#le code est composé d'un ensemble de mot separer par un space
code = input("entrer une serie de mot separer par un space : ")

#on transforme l'ensemble de code en une liste
nouveau_code = code.split()
print(nouveau_code)

drapeau = 1 #on declare un boolean pour test

for i in nouveau_code: #on parcours toute la liste nouveau_code 
	for j in i:        #on parcours chaque element du mot de la liste
		if j not in alphabet: #on verifie est-ce que l'element n'appartient pas à l'alphabet
			drapeau = 0	 #si oui on met drapeau à 0
	for l in nouveau_code: #on parcours toute la liste nouveau_code
		if i.startswith(l): #on determine si j est prefixé de i
			if i == l: #Lorsque i=j on contine
				continue
			drapeau = 0

if drapeau == 1: #si oui alors c'est un code 
	print("Le mot {} est un code".format(nouveau_code))
			
else: #sinon ce n'est pas un code
	print("Le mot {} n'est un alphabet desolé !!! ".format(nouveau_code))
	

