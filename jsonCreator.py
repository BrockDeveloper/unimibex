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

"""
    Ricorda:
    - La persona può scegliere più anni accademici e più giorni
"""

from utils import dataUtils, cryptUtils, consoleUtils
import json


def requestFromKeys(keys):
    while True:
        for i, key in enumerate(keys.keys()):
            print("%s) %s" % (i + 1, key))

        chooseKey = int(input("Choose: ")) - 1
        if -1 < chooseKey < keys.__len__():
            return list(keys.keys())[chooseKey]


def requestFromList(_list):
    while True:
        for i, key in enumerate(_list):
            print("%s) %s" % (i + 1, key["label"]))

        chooseList = int(input("Choose: ")) - 1
        if -1 < chooseList < _list.__len__():
            return _list[chooseList]


def getClassesFromSchool(dataset, schoolDataset):
    return [x for x in dataset if x["scuola"] == schoolDataset]


def requestKindOfStudy(classesDataset):
    # classes[0]["valore"] + " - " + classes[0]["label"] + " (" + classes[0]["tipo"] + ")"
    while True:
        for i, key in enumerate(classesDataset):
            print("%s) %s - %s (%s)" % (i + 1, key["valore"], key["label"], key["tipo"]))

        chooseStudy = int(input("Choose: ")) - 1
        if -1 < chooseStudy < classesDataset.__len__():
            return classesDataset[chooseStudy]


def askLinks(subjectsDataset):
    def iterateDuplicates(values):
        while True:
            for i, key in enumerate(values):
                print("%s) %s - %s" % (i + 1, key["teachers"], key["dayString"]))

            chooseWhile = input("Choose (no or nothing for inserting new links): ")
            if not chooseWhile.isnumeric():
                return -1
            chooseWhile = int(chooseWhile) - 1
            if -1 < chooseWhile < values.__len__():
                return values[chooseWhile]

    def isHere(dataset, now):
        values = [x for x in dataset if x["lesson"] == now["lesson"]]

        if values.__len__() > 0:
            print("\nFound previos servers")
            val = iterateDuplicates(values)
            if val != -1:
                return val

        return False

    output = []
    for subject in subjectsDataset:
        print("Lesson: %s\n Day: %s, start: %s, end: %s" % (
            subject["lesson"], subject["dayString"], subject["start"], subject["end"]
        ))
        print("Teachers: ", end='')
        for teacher in subject["teachers"]:
            print(teacher, end=', ')

        skip = isHere(output, subject)

        if not skip:
            link = input("\nLink (no for skipping this): ")

        # noinspection PyUnboundLocalVariable
        if skip or link != "no" and link.__len__() > 0:
            # noinspection PyUnresolvedReferences
            subject["link"] = skip["link"] if skip else link

            password = ""

            if skip:
                # noinspection PyUnresolvedReferences
                if skip.keys().__contains__("password"):
                    # noinspection PyUnresolvedReferences
                    password = skip["password"]
            else:
                password = input("Password (empty if nothing): ")

            if password.__len__() != 0:
                subject["password"] = password

            output.append(subject)
        consoleUtils.clear()
    return output


# noinspection PyShadowingNames
def save(subjects):
    output = []
    for subject in subjects:
        newLesson = {"LESSON": subject["lesson"], "day": subject["day"],
                     "begin_at": subject["start"], "end_at": subject["end"],
                     "link": cryptUtils.cryptText(subject["link"], returnValue=True)}
        if list(subject.keys()).__contains__("password"):
            newLesson["pass"] = cryptUtils.cryptText(subject["password"], returnValue=True)
        output.append(newLesson)

    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(output, f, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    # Get every urls
    urls = json.load(open("utils/urls.json", "r"))
    # Get every years and throw error if there is a problem
    years = dataUtils.getYears(urls["years"])
    if years.__len__() == 0:
        quit(-1)

    toSave = []

    while True:

        year = requestFromKeys(years)
        consoleUtils.clear()
        if year.__len__() == 0:
            continue

        informations = dataUtils.getUniversityInformations(urls["courses"], year)
        consoleUtils.clear()
        if informations.__len__() == 0:
            continue

        school = requestFromKeys(informations["schools"])
        consoleUtils.clear()
        if school.__len__() == 0:
            continue

        classes = getClassesFromSchool(informations["classes"], informations["schools"][school])
        consoleUtils.clear()
        if classes.__len__() == 0:
            continue

        kindStudy = requestKindOfStudy(classes)
        consoleUtils.clear()
        if kindStudy.__len__() == 0:
            continue

        listCourses = requestFromList(kindStudy["elenco_anni"])
        consoleUtils.clear()
        if listCourses.__len__() == 0:
            continue

        subjects = dataUtils.getSubjects(urls["classes"], urls["params"], year, listCourses,
                                         informations["schools"][school], kindStudy["valore"])
        consoleUtils.clear()
        if subjects.__len__() == 0:
            continue

        subjectsWithLink = askLinks(subjects)
        consoleUtils.clear()
        if subjectsWithLink.__len__() == 0:
            continue

        toSave.extend(subjectsWithLink)
        choose = input("Save or continue? (Save/Continue)")
        consoleUtils.clear()

        if choose.lower() == "save":
            print("Saving in progress..")
            save(toSave)
            toSave.clear()
