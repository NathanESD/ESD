#calculette
#Authentification

b = raw_input("nom : ")
c = raw_input("prenom : ")

#verification

a = {"nathan":"lol","jerome":"parisien","guillaume":"chti"}
for cle,valeur in a.items():
  if cle == b and valeur == c:
	#Valeurs
	nb1 = int(input('Premier nombre : '))
	nb2 = int(input('Deuxieme nombre : '))
	op = raw_input('operateur : ')



#calcul

if (op == '*'):
  print (nb1 * nb2)

elif (op == '-'):
  print (nb1 - nb2)

elif (op == '/'):
  print (nb1 / nb2)

elif (op == '+'):
  print (nb1 + nb2)


