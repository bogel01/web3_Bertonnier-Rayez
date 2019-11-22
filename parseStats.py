from bs4 import BeautifulSoup, Tag
import os
import includes


def getId(filename):
    return filename.split("_")[1].split(".")[0]


def getCategory(text):
    split_text = text.split("Répartition par")
    if len(split_text) > 1:
        text = split_text[1][1:]
        text = text.replace("de", "")
        text = text.replace("d'", "")
        text = text.replace(" ", "_")
    else:
        text = split_text[0]
    return text


def isACategory(tr):
    if not isinstance(tr, Tag):
        return False
    return tr.name == "tr" and tr.has_attr('class') and tr['class'][0] == 'papi_liste_t'


def parseStats():
    files = os.listdir(includes.getDir(includes.stat))
    if len(files) == 0:
        print(
            "Il n'y a pas de fichiers dans le dossier 'webContent/stats'.\nVeuillez le peupler avec le script 'extractFromWeb'"
        )
        return

    stats = {}
    for filename in files:
        file = open(includes.getDir(includes.stat) + filename, mode="r", encoding="utf-8", errors="replace")
        id = getId(filename)
        soup = BeautifulSoup(file, 'html.parser')

        table = soup.find("table", {"id": "TablePage"}).find("table")
        if table == None:
            continue
        flag_two_tr = False
        current_stat = {}
        for tr in table.find_all("tr", {"class": "papi_liste_t"}):
            category = getCategory(tr.find("td").text)
            voisin = tr.find_next_sibling()
            if flag_two_tr:
                flag_two_tr = False
                continue
            if isACategory(voisin):
                flag_two_tr = True
                voisin = voisin.find_next_sibling()
            current_stat[category] = {}
            while isinstance(voisin, Tag) and not isACategory(voisin):
                td_sous_cat = voisin.find("td", {"class": "papi_liste_c"})
                if td_sous_cat == None:
                    break
                td_value = td_sous_cat.find_next_sibling()
                sous_cat = td_sous_cat.text.split(" :")[0]
                value = td_value.text.split(" ")[0]
                current_stat[category][sous_cat] = value
                voisin = voisin.find_next_sibling()

        stats[id] = current_stat

    includes.saveInJSON(stats, "stats")

parseStats()