from bs4 import BeautifulSoup
import os

tournois = {}
stat ={}

directory = os.listdir("tests/")
for fileIn in directory :
    id_tournois = fileIn.split(".")[0]
    tournoi = {}
    with open("Tests/"+fileIn) as fp:
        soup = BeautifulSoup(fp,'html.parser')
    data = soup.find_all("span")
    for child in data:
        id_element = child.attrs['id']
        if (id_element):
            id_element_split = id_element.split("_")
            nb_element = len(id_element_split)
            if (nb_element>0):
                tag = id_element_split[nb_element-1]
                if ( tag == "LabelNom") : 
                    tournoi[tag]=child.text
                #if (tag == "LabelLieu"):
                    
                #if (tag == "LabelDates"):
                #if (tag == "LabelEloRapide"):
                #if (tag == "LabelHomologuePar"):
                #if (tag == "LabelNbrRondes"):
                #if (tag == "LabelCadence"):
                #if (tag == "LabelAppariements"):
                #if (tag == "LabelOrganisateur"):
                #if (tag == "LabelArbitre"):
                #if (tag == "Labelseparator"):


        print(child.text)

    print(soup.text)