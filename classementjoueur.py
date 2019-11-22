import json
import includes
import sys
import includes

moisAnnee = {"janvier":1,"février":2, "mars":3,"avril":4,"mai":5,"juin":6,
"juillet":7,"août":8,"septembre":9,"octobre":10,"novembre":11,"décembre":12}

def loadJson(name):
    with open('output/' + name + '.json') as json_file:
        return json.load(json_file)

person = loadJson("participants")
tournois = loadJson("tournois")

def getTournoisAn (anneeDebut):
    anDebut = str(anneeDebut)
    tournoisAn = []
    for id, desc in tournois.items():
        dates = disectDate(desc.get("Dates"))
        if (dates is not None):
            if ( dates["debut"]["annee"] == (anDebut) ):
                tournoisAn.append(id)
    return tournoisAn

def getTournoisMois (listTournois,moisDeb=1, moisFin=12):
    tournoiPeriode = []
    for tournoi in listTournois:
        tournoi_ = tournois.get(tournoi)
        dateTournoi = disectDate(tournoi_["Dates"])        
        #convertion en nombre
        if (dateTournoi is not None):
            dateDebutTournoi = moisAnnee[dateTournoi["debut"]["mois"]]
            if ( dateDebutTournoi >= moisDeb and dateDebutTournoi <= moisFin):
                tournoiPeriode.append(tournoi)            
    return tournoiPeriode

def disectDate (dates):
    # date has the format : "mercredi 05 mars 2014 - samedi 08 mars 2014"
    dates_=dates.split(" - ")
    debut = dates_[0].split(" ")
    fin = dates_[1].split(" ")
    if(len(fin)==4 and len(debut)== 4):
        return {"debut":{"jour":debut[0],"numJourDeb":debut[1],"mois":debut[2], "annee":debut[3]},"fin":{"jour":fin[0],"numJourDeb":fin[1],"mois":fin[2], "annee":fin[3]}}
    else :
        return None

def classement (listeTournois):
    tableauClassement={}
    for numTournoi in listeTournois:
        listeParticipants = person.get(numTournoi)
        if (listeParticipants is not None ):
            for id,personne in listeParticipants.items():
                if(personne["Nom"] in tableauClassement):
                    tableauClassement[personne["Nom"]] = tableauClassement[personne["Nom"]]+1
                else:
                    tableauClassement[personne["Nom"]] = 1
    return sorted(tableauClassement.items(), key=lambda t: t[1], reverse=True)

def programme (annee,moisDeb = 1,moisFin = 12):
    TournoisDelAnnee = getTournoisAn(annee)
    tournoisDelAnneePeriode = getTournoisMois(TournoisDelAnnee,moisDeb,moisFin)
    classement_json=json.dumps(classement(tournoisDelAnneePeriode))
    includes.saveInJSON(classement_json, "classement")

#### implémentation
annee=0
moisdebut = 1
moisfin = 12
if len (sys.argv) == 1:
    print("Veuillez entrer une date")
    exit()
if len(sys.argv) == 2:
    if not isinstance(int(sys.argv[1]), int):
        print("premier argument doit être une annee valide")
        exit()
    annee = int(sys.argv[1])
    
elif len(sys.argv) == 3:
    if not isinstance(int(sys.argv[1]), int)or not isinstance(int(sys.argv[2]), int):
        print("le premier argument est une année valide")
        print("le deuxième argument est le numéro du mois de début")
        exit()
    annee = int(sys.argv[1])
    moisdebut = int(sys.argv[2])
elif len(sys.argv) == 4:
    if not isinstance(int(sys.argv[1]), int)or not isinstance(int(sys.argv[2]), int):
        print("le premier argument est une année valide")
        print("le deuxième argument est le numéro du mois de début")
        exit()
    if not isinstance(int(sys.argv[1]), int):
        print("le deuxième argument est le numéro du mois de début")
        exit()
    annee = int(sys.argv[1])
    moisdebut = int(sys.argv[2])
    moisfin = int(sys.argv[3])


programme(annee,moisdebut,moisfin)
