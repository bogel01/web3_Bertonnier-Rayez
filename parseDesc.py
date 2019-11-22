from bs4 import BeautifulSoup
import os
import includes


def parseDesc():
    tournois = {}

    directory = os.listdir("webContent/desc/")
    for fileIn in directory:
        id_tournois = fileIn.split(".")[0]
        id_tournois = id_tournois.split("_")[1]
        tournoi = {}
        with open("webContent/desc/" + fileIn,mode='r',encoding='utf-8') as fp:
            soup = BeautifulSoup(fp, 'html.parser',)
        data = soup.find_all("span")
        for child in data:
            id_element = child.attrs['id']
            if (id_element):
                id_element_split = id_element.split("_")
                nb_element = len(id_element_split)
                if (nb_element > 0):
                    tag = id_element_split[nb_element - 1]
                    if (tag != "LabelTitre"):
                        tournoi[tag[5:]] = child.text
        tournois[id_tournois] = tournoi

    includes.saveInJSON(tournois, "tournois")

parseDesc()