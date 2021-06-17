israel = {'Python': [19, 20, 20], 'Java': [18, 11, 16], 'C': [19, 15, 17], 'Structures de données': [19, 20, 16], "Systeme d'exploitation": [17, 19, 19.75], 'uml': [10, 14, 19], 'web': [19, 20, 15]}

moyenne_matiere = {'Python': (israel['Python'][0] + israel['Python'][1] + israel['Python'][2]) / 3, 'Java': (israel['Java'][0] + israel['Java'][1] + israel['Java'][2]) / 3, 'C': (israel['C'][0] + israel['C'][1] + israel['C'][2]) / 3, 'Structures de données': (israel['Structures de données'][0] + israel['Structures de données'][1] + israel['Structures de données'][2]) / 3, "Systeme d'exploitation": (israel["Systeme d'exploitation"][0] + israel["Systeme d'exploitation"][1] + israel["Systeme d'exploitation"][2]) / 3, 'uml': (israel['uml'][0] + israel['uml'][1] + israel['uml'][2]) / 3, 'web': (israel['web'][0] + israel['web'][1] + israel['web'][2]) / 3}

liste_moyenne_matiere = list(moyenne_matiere.values())

moyenne = (liste_moyenne_matiere[0] + liste_moyenne_matiere[1] + liste_moyenne_matiere[2] + liste_moyenne_matiere[3] + liste_moyenne_matiere[4] + liste_moyenne_matiere[5] + liste_moyenne_matiere[6]) / 7

print(moyenne)
