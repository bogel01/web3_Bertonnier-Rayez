import os
from bs4 import BeautifulSoup, Tag
import includes

directory = includes.getDir(includes.res)
files = os.listdir(directory)

def isLine(tr) :
    if not isinstance(tr, Tag):
        return False
    return tr.name == "tr" and tr.has_attr('class') and (tr['class'][0] == 'papi_small_f' or tr['class'][0] == 'papi_small_c' )


def parseGrille():
    res = {}

    for filename in files:
        id_tournois = filename.split("_")[1].split(".")[0]
        titre = []
        file = open(directory + filename, mode="r", encoding="utf-8")
        soup = BeautifulSoup(file, 'html.parser')

        Titrelist = soup.table.find(name="tr", class_="papi_small_t")
        if Titrelist is None:
            continue

        for subBalise in Titrelist:
            if (subBalise != "\n"):
                for element in subBalise.contents:
                    titre.append(element)

        voisin = Titrelist.find_next_sibling()
        res[id_tournois] = []
        while isinstance(voisin, Tag) and isLine(voisin):
            grille = {}
            i = 0
            for element in voisin.contents:
                if (element != "\n"):
                    grille[titre[i]] = element.text
                    i += 1
            res[id_tournois].append(grille)
            voisin = voisin.find_next_sibling()
    includes.saveInJSON(res, "result")


parseGrille()
