# coding:utf-8

### BONJOUR, ICI JHR ###
### Mes notes et corrections sont précédées de trois dièses ###

### Il fallait conserver la variable «publications».
### Cela dit, on pouvait aussi s'en passer! :)
### Mais si on faisait ça, il fallait la laisser dans un autre fichier.
### J'ai appelé cet autre fichier «devoir1JHR.py» (et je l'ai rajouté à ton répertoire).
### Il était ensuite possible d'importer la variable «publications» avec le code suivant:

from devoir1JHR import publications ### Remarque: on ne met pas, ici, le «.py» au nom du fichier où se trouve le code qu'on importe

### Tes commentaires sont très bons et me permettent de bien comprendre ce que tu souhaitais faire

# print(publications[0][3])
#partages = publications[0][3]
#reactions = publications[0][4]
#commentaires = publications[0][5]

#n = 0

#for publication in publications:
"""Ici, j'ai essayé de reverse-engineer la phrase finale
en prenant le premier élément de la liste publications en exemple."""

varMedia = publications[0][0]
varPartages = publications[0][3]
varReactions = publications[0][4]
varCommentaires = publications[0][5]
varEngagement = varPartages + varReactions + varCommentaires

### Le code ci-dessus recueille les bonnes infos
### Mais pour la première ligne de la variable «publications» seulement

"""print(varMedia)
	#n += 1
	#if publications[0] = "104,7 Outaouais":
		#fr += 1
#print(fr/n)"""


# Ok, je comprend pas grand chose.
print(varPartages)
print(varReactions)
print(varCommentaires)
print(varEngagement)
# So far, ça marche.
#print(varPartages + varReactions + varCommentaires)

"""Source: https://www.tutorialspoint.com/python/python_lists.html
Source: https://www.tutorialspoint.com/python/python_strings.html
Source: https://journalistsresource.org/tip-sheets/research/python-scrape-website-data-criminal-justice
"""

# print str("Les publications du média " + varMedia + "ont été partagées " + varPartages + "fois, ont provoqué " + varReactions + "réactions et ont généré " + varCommentaires + "commentaires, pour un engagement total de " + varEngagement + "en 2017.")
# La ligne d'en haut ne fonctionne pas.
# print "Les publications du média %s ont été partagées %d fois, ont provoqué %d réactions et ont généré %d commentaires, pour un engagement total de %d en 2017." % (varMedia, varPartages, varReactions, varCommentaires, varEngagement)
# Celle-là non plus.
print("Les publications du média", varMedia, "ont été partagées", varPartages, "fois, ont provoqué", varReactions, "réactions et ont généré", varCommentaires, "commentaires, pour un engagement total de", varEngagement, "en 2017.")
# Ça, ça marche.

"""if publications[0] == "104,7 Outaouais":
	print"""

"""Un script qui additionne tout:"""

"""n = 0
for a in range("104, 7 Outaouais", "VICE Québec"): # boucle qui passe toutes les années
	for x in range(1001, 2000): # boucle qui passe les 1000 numéros de permis
		n += 1
		noPermis = "{}{}".format(str(a)[2:],str(x)[1:]) # confectionne
		# print("On recherche le {}e permis: {}".format(n,noPermis)) # A"""

"""x = 
if x = y:
	print([3] + [4] + [5])"""

"""for publication in publications:
	if x in inmate_races:
		inmate_races[inmate['race']] += 1
	else:
		inmate_races[inmate['race']] = 1"""

# Ok, je comprends rien. Je vais vraiment avoir besoin d'aide!

### Il y a deux façons de faire
###
### Recette ou algorithme 1
### Recueillir dans la variable «publications» tous les noms de médias différents possibles et les mettre dans une liste qu'on peut appeler «medias»
### Faire une boucle qui passe à travers cette liste
### Pour chacun des médias, on fait ensuite une autre boucle qui passe à travers la variable «publications»
### Si le nom du média qu'on trouve dans «publications» correspond au média où on est rendu dans notre boucle qui passe à travers la liste «media»,
### on recueille les données qui nous intéressent
### Si le nom du média dans la variable «publications» n'est plus le bon, on imprime la ligne avec toutes les infos
###
### Recette ou algorithme 2
### Plus difficile à expliquer
### On va le voir en classe, mais tu peux aussi consulter mon code ici: https://github.com/jhroy/syllabus-EDM5240-H2018/blob/master/devoir1-corrige.py
