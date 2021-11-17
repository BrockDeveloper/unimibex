# TechAle
# See LICENSE file.
#
# Developed by
# TechAle (https://github.com/TechAle)
#
# This source code is distributed under the CC BY-NC-SA 4.0 license:
# https://creativecommons.org/licenses/by-nc-sa/4.0/
# you are FREE to SHARE and ADAPT UNDER THE FOLLOWING TERMS:
#
# ATTRIBUTION You must give appropriate credit, provide a link to the
# license, and indicate if changes were made.
#
# NON COMMERCIAL You may not use the material for commercial purposes.
#
# SHARE ALIKE If you remix, transform, or build upon the material, you
# must distribute your contributions under the same license as the original.
#
#
# This source code is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY.

'''
    TODO:
    - Ricava l'orario
    - Trasforma l'orario in un dizionario
    - Salva il dizionario

    Ricorda:
    - La persona può scegliere più anni accademici e più giorni
'''

from jsonCreatorFiles.dataUtils import *

def requestFromKeys(keys):
    while True:
        for i, key in enumerate(keys.keys()):
            print("%s) %s" % (i + 1, key))

        choose = int(input("Choose: ")) - 1
        if -1 < choose < keys.__len__():
            return list(keys.keys())[choose]

def requestFromList(_list):
    while True:
        for i, key in enumerate(_list):
            print("%s) %s" % (i + 1, key["label"]))

        choose = int(input("Choose: ")) - 1
        if -1 < choose < _list.__len__():
            return _list[choose]

def getClassesFromSchool(dataset, school):
    return [x for x in dataset if x["scuola"] == school]

def requestKindOfStudy(classes):
    # classes[0]["valore"] + " - " + classes[0]["label"] + " (" + classes[0]["tipo"] + ")"
    while True:
        for i, key in enumerate(classes):
            print("%s) %s - %s (%s)" % (i+1, key["valore"], key["label"], key["tipo"]))

        choose = int(input("Choose: ")) - 1
        if -1 < choose < classes.__len__():
            return classes[choose]


if __name__ == "__main__":
    # Get every urls
    urls = json.load(open("./jsonCreatorFiles/urls.json", "r"))
    # Get every years and throw error if there is a problem
    years = getYears(urls["years"])
    if years.__len__() == 0:
        quit(-1)

    while True:

        year = requestFromKeys(years)

        informations = getUniversityInformations(urls["courses"], year)

        school = requestFromKeys(informations["schools"])

        classes = getClassesFromSchool(informations["classes"], informations["schools"][school])

        kindStudy = requestKindOfStudy(classes)

        yearStudy = requestFromList(kindStudy["elenco_anni"])

        a = 0


