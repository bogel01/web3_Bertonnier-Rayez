import json

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


def getMaps():
    return [desc, stat, person, res]


def saveInJSON(map, filename):
    FileOutput = open("output/" + filename + ".json", mode="w", encoding="utf-8")
    FileOutput.write(json.dumps(map, ensure_ascii="false"))
