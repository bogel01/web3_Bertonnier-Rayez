import os

import sys
import wget
import logging
import includes

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO, filename="log_scrap.log")


def getData(map, id):
    dest = includes.getDest(map, id)
    url = includes.getUrl(map, id)
    try:
        wget.download(url, dest)
        mode = includes.getName(map, id).split("_")[0]
        logging.info("Ajout du fichier id: " + str(id) + " pour le mode: " + mode)
    except:
        logging.info("id{" + str(id) + "} n'a pas abouti, url{" + url + "}")


def getAll(id_start, id_end):
    maps = includes.getMaps()
    for id in range(id_start, id_end):
        for m in maps:
            getData(m, id)


def clearAllDir():
    maps = includes.getMaps()
    for m in maps:
        dir = includes.getDir(m)
        for filename in os.listdir(dir):
            os.remove(dir + filename)


if len(sys.argv) == 2:
    if not isinstance(int(sys.argv[1]), int):
        print("premier argument doit être un int >0")
        exit()
    start_id = int(sys.argv[1])
    end_id = int(start_id) + 10
    clear = False
elif len(sys.argv) == 3:
    if not isinstance(int(sys.argv[1]), int)or not isinstance(int(sys.argv[2]), int):
        print("le premier et le deuxième argument doit être un int >0")
        exit()
    start_id = int(sys.argv[1])
    end_id = int(sys.argv[2])
    clear = False
elif len(sys.argv) == 4:
    if not isinstance(int(sys.argv[1]), int)or not isinstance(int(sys.argv[2]), int):
        print("le premier et le deuxième argument doit être un int >0")
        exit()
    if not isinstance(bool(sys.argv[1]), bool):
        print("le troisème argument doit être un boolean")
        exit()
    start_id = int(sys.argv[1])
    end_id = int(sys.argv[2])
    clear = bool(sys.argv[3])
else:
    start_id = 1
    end_id = 10
    clear = False

## script ##
if clear:
    clearAllDir()
getAll(start_id, end_id)
