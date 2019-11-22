import os
from bs4 import BeautifulSoup
import json
import includes

directory = includes.getDir(includes.person)
filesName = os.listdir(directory)


def parsePerson():
    participants = {}
    personns = {}

    for fileIn in filesName:
        id_tournois = fileIn.split(".")[0]
        id_tournois = id_tournois.split("_")[1]

        titre = []
        fichierIn = open(directory + fileIn, mode="r", encoding="utf-8")
        soup = BeautifulSoup(fichierIn, 'html.parser')
        Titrelist = soup.table.find(name="tr", class_="papi_liste_t")
        person = {}

        if Titrelist is None:
            continue

        for subBalise in Titrelist:
            if (subBalise != "\n"):
                for element in subBalise.contents:
                    titre.append(element)
        dataPersonne = soup.table.findAll(name="tr", class_="papi_liste_f")
        i = 0
        for tr in dataPersonne:
            j = 0
            for element in tr.contents:
                if (element != "\n"):
                    person[titre[j]] = element.text
                    j += 1
            # print(person)
            personns[i] = person.copy()
            person.clear()
            i += 1
        dataPersonne = soup.table.findAll(name="tr", class_="papi_liste_c")
        for tr in dataPersonne:
            j = 0
            for td in tr.contents:
                if (td != "\n"):
                    person[titre[j]] = td.text
                    j += 1
            # print(person)
            personns[i] = person.copy()
            person.clear()
            i += 1
        participants[id_tournois] = personns.copy()
        personns.clear()

    includes.saveInJSON(participants, "participants")


parsePerson()
