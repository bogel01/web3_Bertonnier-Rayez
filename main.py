import json
import includes


def loadJson(name):
    with open('output/' + name + '.json') as json_file:
        return json.load(json_file)


res = loadJson("result")
person = loadJson("participants")
stats = loadJson("stats")
tournois = loadJson("tournois")


##### REQUEST : clubs les plus actifs  #####
def getClubCounter():
    club_stat = {}
    for id, stat in stats.items():
        for club_name in stat["clubs"]:
            club_name = club_name.replace(" ", "_")
            counter = club_stat.get(club_name)
            if counter == None:
                club_stat[club_name] = {"count": 1}
            else:
                counter = counter.get("count")
                club_stat[club_name]["count"] = int(counter) + 1
    return club_stat


def sortClub(desc=True):
    club = getClubCounter().items()
    return sorted(club, key=lambda t: t[1]["count"], reverse=desc)


def getClub(nb_club=0):
    parsed_club = []
    clubs = sortClub()
    if nb_club == 0:
        nb_club = len(clubs)
    for key, val in clubs[:nb_club]:
        parsed_club.append((key, val["count"]))
    return parsed_club

##### REQUEST :  tournois auquel un joueur a participe  #####

def hasParticipate(name, list_person):
    find = False
    index = 0
    while not find and index < len(list_person):
        current_name = list_person.get(str(index))
        if not current_name is None and name == current_name.get("Nom"):
            find = True
        index += 1
    return find


def getNameForTournoi(tournoi_ids):
    names = []
    for id in tournoi_ids:
        names.append(tournois[id]["Nom"])

    return names


def getTournoi(name):
    list_tournoi = []
    for id, participants in person.items():
        if hasParticipate(name, participants):
            list_tournoi.append(id)

    return getNameForTournoi(list_tournoi)




##### REQUEST :  classement des joueurs par rapport `a leur nombre de tournois gagn´es  #####

def getPlayerCount():
    better_player = {}
    for id,grille in res.items():
        for val in grille:
            place = int(val.get("Pl"))
            name = val.get("Nom")
            if place == 1:
                counter = better_player.get(name)
                if counter is None:
                    better_player[name] = 1
                else:
                    better_player[name] = int(counter) +1

    return better_player


def sortPlayer(desc = True):
    players = getPlayerCount().items()
    return sorted(players, key=lambda t: t[1], reverse=desc)


def getBetterPlayer(nb_player = 0):
    better_players = sortPlayer()
    if nb_player == 0:
        nb_player = len(better_players)
    return better_players[:nb_player]


def printData():
    better_players = getBetterPlayer()
    better_players10 = better_players[:10]

    print("**** Requêtage des données ***.")
    print("\t\t Nombre de tournois Préparés : " + str(len(tournois)))
    print("\t\t Nombre de tournois effectués : " + str(len(res)))
    print("\t\t Nombre de joueurs qui ont pariticipés : " + str(len(better_players)))

    print("\n\t 2) 10 Meilleurs joueurs : ")
    print("\t\t" + str(getBetterPlayer(5)))

    print("\n\t 3) 10 Clubs les + actifs : ")
    print("\t\t" + str(getClub(10)))

    print("\n\t 4) Les tournois du joueur 'SOKOLOVITCH Thomas' : ")
    print("\t\t" + str(getTournoi("SOKOLOVITCH Thomas")))

    print("\n\t 5) Les joueur qui jouent le plus :")
    try :
        classement = loadJson("classement")
        print(classement)
    except:
        print('\t Vous devez appeler le script "classementjoueur.py" pour générer le fichier')


printData()
