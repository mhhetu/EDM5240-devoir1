# coding:utf-8

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
