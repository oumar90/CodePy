import math
#calcul d'entropie
def entropie(n):
	"Fonction qui calcule l'entropie"
	return (math.log2(n))

def longueurmoy(c, n):
	"Fonction qui calcule la longueur moyenne d'un  code"
	som = 0
	j =0
	while j < len(c):
		som=som+len(i)*(1/n)
		j+=1
	return som	

		
#cacul de longueur minimum		
def longueurmin(entropie, n):
	"La fonction qui calcule la longueur minimale d'un code"
	return entropie/math.log2(n)

#calcul de rendement
def rendement(longueurmin, longueurmoy):
	"fonction qui calcule le rendement"
	return longueurmin/longueurmoy	

	
def main():
	#pour stocker l'alphabet
	alphabet = ""


	alphabet1 = input("entrer l'alphabet :")
	print()
	alphabet = alphabet1
	#le code est composé d'un ensemble de mot separer par un space
	code = input("entrer une serie de mot separer par un space : ")
	print()

	#on transforme l'ensemble de code en une liste
	nouveau_code = code.split()
	print(nouveau_code)
	print()

	drapeau = 1 #on declare un boolean pour test
	global i
	for i in nouveau_code: #on parcours toute la liste nouveau_code 
		for j in i:        #on parcours chaque element du mot de la liste
			if j not in alphabet: #on verifie est-ce que l'element n'appartient pas à l'alphabet
				drapeau = 0	 #si oui on met drapeau à 0
		for l in nouveau_code: #on parcours toute la liste nouveau_code
			if i.startswith(l): #on determine si j est prefixé de i
				if i == l: #Lorsque i=j on contine
					continue
				drapeau = 0

	dim = len(alphabet)
	card = len(nouveau_code)
	ento = entropie(card)
	longMin = longueurmin(ento,card)
	longMoy = longueurmoy(nouveau_code, card)
	rend = rendement(longMin, longMoy)
	redon = 1 - rend
	if drapeau == 1: #si oui alors c'est un code 

		print("L'ensemble de mot {} est un code".format(nouveau_code))
		print("Les caracteristiques sont:")
		print("      |--*--> Entropie     : ", ento)
		print("      |--*--> Longueur min : ", longMin)
		print("      |--*--> Longueur moy : ", longMoy)
		print("      |--*--> Rendement    : ", rend)
		print("      |--*--> Redondance   : ", redon)
		print("      |--*--> Dimension    : ", dim)

		count=1
		for i in nouveau_code:
			if int(i) != 0:
				count=0
			else:
				count=1
		if count==1:		
			print("      |--*--> Ce code {} est linéaire puisqu'il contient au moins un mot nul.".format(nouveau_code))
		else:	
			print("      |--*--> Ce code {} n'est pas linéaire par ce qu'il ne contient aucun mot null.".format(nouveau_code))	

	else: #sinon ce n'est pas un code
		print("L'ensemble de mot {} n'est un code, desolé !!! ".format(nouveau_code))
		

#---------------------Programme principal---------------------
if __name__ == '__main__':
	main()