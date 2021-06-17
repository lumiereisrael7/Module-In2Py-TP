#Calcul de moyenne
print('Exo de moyenne')
israel = {'Python': [19, 20, 20], 'Java': [18, 11, 16], 'C': [19, 15, 17], 'Structures de données': [19, 20, 16], "Systeme d'exploitation": [17, 19, 19.75], 'uml': [10, 14, 19], 'web': [19, 20, 15]}

moyenne_matiere = {'Python': sum(israel['Python']) / len(israel['Python']), 'Java': sum(israel['Java']) / len(israel['Java']), 'C': sum(israel['C']) / len(israel['C']), 'Structures de données': sum(israel['Structures de données']) / len(israel['Structures de données']), "Systeme d'exploitation": sum(israel["Systeme d'exploitation"]) / len(israel["Systeme d'exploitation"]), 'uml': sum(israel['uml']) / len(israel['uml']), 'web': sum(israel['web'])/ len(israel['web'])}

liste_moyenne_matiere = list(moyenne_matiere.values())

#moyenne = (liste_moyenne_matiere[0] + liste_moyenne_matiere[1] + liste_moyenne_matiere[2] + liste_moyenne_matiere[3] + liste_moyenne_matiere[4] + liste_moyenne_matiere[5] + liste_moyenne_matiere[6]) / 7

moyenne = sum(liste_moyenne_matiere) / len(liste_moyenne_matiere) 

print(moyenne)
print("===========================================================================================")
#Exercice E0
print('Exo E0')
# 1- Creation de la liste L
L = list(range(1, 11))
print('L: ', L)

# 2- Ajout de 11
L[0] += 11
L[1] += 11
L[2] += 11
L[3] += 11
L[4] += 11
L[5] += 11
L[6] += 11
L[7] += 11
L[8] += 11
L[9] += 11
print('L vaut maintenant apres ajout de 11 a chacun de ses elements: ', L)

# 3- Ajout de 22 en fin de liste
L.append(22)
print('L vaut apres ajout de 22 en fin de liste: ', L)

# 4- Ajout simultané de 23 et 24 en fin de liste 
L.extend([23, 24])
print('L vaut maintenant apres ajout simultané de 23 et 24: ', L)

# 5- Extraction des deux sous listes
L1 = L[::2]
print('L1 vaut: ', L1)

L2 = L[1::2]
print('L2 vaut: ', L2)
print("===========================================================================================")

#Exo E1
print('Exo E1')
d = {'nom': 'Dupuis', 'prenom': 'Jacque', 'age': 30}

# a- correction de l'erreur
d['prenom'] = 'Jacques'

# b- Afficher la liste des clés du dictionnaire
print(d.keys())

# c- Afficher la liste des valeurs du dictionnaire
print(d.values())

# d- La liste les paires clé/valeur du dictionnaire
print(d)

# e- La phrase "Jacques Dupuis a 30 ans"

print(d['prenom'] + ' ' + d['nom'] + ' a ' + str(d['age']) + ' ans')

# 6- suppression de l'entree d'indice 3
L.pop(3)
print("L vaut enfin apres suppression de l'entree d'indice 3: ", L)

print("===========================================================================================")
