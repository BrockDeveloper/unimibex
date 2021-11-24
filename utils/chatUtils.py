# import call method from subprocess module
from subprocess import call
import os


# define clear function
def clear():
    # check and make call for specific operating system
    _ = call('clear' if os.name == 'posix' else 'cls')


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
        clear()
    return output
