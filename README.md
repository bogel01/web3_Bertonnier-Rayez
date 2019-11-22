# EchecParser
Présentations des différents scripts.

Le projet contient des déjà des fichiers de output générer à partir des données scraper de l'index 30000 à 30500.

## Web scrapping 

Pour récupérer les données web, il faut exécuter le script suivant: `extractFromWeb.py`

La commande suivante permet de récupérer les données de l'index 30000 à 30500 en supprimant les données préalablement déjà enregistrées :
`python extractFromWeb.py 30000 30500 True`
 
Le script possède trois arguments :
 1) L'index de début de scrap (par défaut 1).
 2) L'index de fin de scrap (par défaut, début +10).
 3) Boolean permettant de supprimer les données préalablement enregistrées.

## Parser les données 

Le formatage des données dans les fichiers json sont réalisés par les scripts suivant : 
***     
* Description des tournois : `desc.json` ==> `parseDesc.py`
* Les statistiques des tournois : `stats.json` ==> `parseStats.py`
* Les participants aux tournois : `participants.json` ==> `parsePerson.json`
* Les résultats des tournois : `result.json` ==> `parseGrille.json`
***

Dans un primier temps, il faut récupérer les données grâce au script présenté dans la section précédente.

Il faut ensuite exécuter chaque script précédent pour générer les fichiers parsé.

## Requêtage
Le recueil  des informations sont basé sur les script présentés  dans la section 'parsage de données', il faut alors générer ces fichiers avant de passer au requêtage.

Il suffit d'appeler le script `main.py` pour générer le requêtage des données.

Cependant, il vous faudra préalablement générer le fichier de classement si vous souhaitez voir les données des joueurs les plus actifs sur une  période.
Pour ce faire, vous devez appeler le script `classementjoueur.py` avec comme paramètres:
1) L'année (ex: 2014)
2) Le mois de départ (1: pour janvier)
3) Le mois de fin (12 : pour décembre)

## Authors
* **Florian Bertonnier** 
* **Laurent Rayez**
