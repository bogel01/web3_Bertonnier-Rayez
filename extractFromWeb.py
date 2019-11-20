import os
import wget
import logging

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO, filename="log_scrap.log")

desc = {
    "url": "http://echecs.asso.fr/FicheTournoi.aspx?Ref=[id]",
    "dir": "webContent/desc/",
    "name": "desc_[id]"
}
stat = {
    "url": "http://echecs.asso.fr/Resultats.aspx?URL=Tournois/Id/[id]/[id]&Action=Stats",
    "dir": "webContent/stats/",
    "name": "stat_[id]"
}
person = {
    "url": "http://echecs.asso.fr/Resultats.aspx?URL=Tournois/Id/[id]/[id]&Action=Ls",
    "dir": "webContent/person/",
    "name": "person_[id]"
}
res = {
    "url": "http://echecs.asso.fr/Resultats.aspx?URL=Tournois/Id/[id]/[id]&Action=Ga",
    "dir": "webContent/res/",
    "name": "res_[id]"
}


def getDir(map):
    return map.get("dir")


def getName(map, id):
    return addId(map.get("name"), id)


def getUrl(map, id):
    return addId(map.get("url"), id)


# Ajoute l'id à l'ur en remplaçant [id] par id
def addId(mystr, id):
    return mystr.replace("[id]", str(id))


def getDest(map, id):
    return getDir(map) + getName(map, id) + ".html"


def getData(map, id):
    dest = getDest(map, id)
    url = getUrl(map, id)
    try:
        wget.download(url, dest)
        mode = getName(map, id).split("_")[0]
        logging.info("Ajout du fichier id: "+str(id)+" pour le mode: "+mode)
    except:
        logging.info("id{" + str(id) + "} n'a pas abouti, url{" + url + "}")

def getAll(id_start, id_end):
    maps = [desc, stat, person, res]
    for id in range(id_start, id_end):
        for m in maps:
            getData(m, id)

def clearAllDir():
    maps = [desc, stat, person, res]
    for m in maps:
        dir = getDir(m)
        for filename in os.listdir(dir):
            os.remove(dir + filename)

clearAllDir()
getAll(1,5)