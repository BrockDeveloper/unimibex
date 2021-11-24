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
from subprocess import call
import os


# define clear function
def clear():
    # check and make call for specific operating system
    _ = call('clear' if os.name == 'posix' else 'cls')


def requestFromKeys(keys):
    # Till he choose
    while True:
        # Print everything
        for i, key in enumerate(keys.keys()):
            print("%s) %s" % (i + 1, key))

        # Ask
        chooseKey = int(input("Choose: ")) - 1
        if -1 < chooseKey < keys.__len__():
            return list(keys.keys())[chooseKey]


def requestFromList(_list):
    # Till he choose
    while True:
        # Print
        for i, key in enumerate(_list):
            print("%s) %s" % (i + 1, key["label"]))

        # Ask
        chooseList = int(input("Choose: ")) - 1
        if -1 < chooseList < _list.__len__():
            return _list[chooseList]


def getClassesFromSchool(dataset, schoolDataset):
    # Get every schools from a specific dataset
    return [x for x in dataset if x["scuola"] == schoolDataset]


def requestKindOfStudy(classesDataset):
    # Till the end
    while True:
        # Print
        for i, key in enumerate(classesDataset):
            print("%s) %s - %s (%s)" % (i + 1, key["valore"], key["label"], key["tipo"]))

        # Ask
        chooseStudy = int(input("Choose: ")) - 1
        if -1 < chooseStudy < classesDataset.__len__():
            return classesDataset[chooseStudy]


def askLinks(subjectsDataset):

    '''
        Function that ask which of the links he before added he want
        Return:
            -1 if he want to insert a new link
            Or, the list he before added
    '''
    def iterateDuplicates(values):
        # Till the end
        while True:
            # Print
            for i, key in enumerate(values):
                print("%s) %s - %s" % (i + 1, key["teachers"], key["dayString"]))

            # Ask
            chooseWhile = input("Choose (no or nothing for inserting new links): ")
            # If it's not a number, then go away lol
            if not chooseWhile.isnumeric():
                return -1
            chooseWhile = int(chooseWhile) - 1
            if -1 < chooseWhile < values.__len__():
                return values[chooseWhile]

    '''
        Main Function that ask which of the links he before added he want
        Return:
            -1 if he want to insert a new link
            Or, the list he before added
    '''
    def isHere(dataset, now):
        values = [x for x in dataset if x["lesson"] == now["lesson"]]

        if values.__len__() > 0:
            print("\nFound previos servers")
            val = iterateDuplicates(values)
            if val != -1:
                return val

        return False

    # The output we want
    output = []
    # For every subjects
    for subject in subjectsDataset:
        # Print everything
        print("Lesson: %s\n Day: %s, start: %s, end: %s" % (
            subject["lesson"], subject["dayString"], subject["start"], subject["end"]
        ))
        print("Teachers: ", end='')
        for teacher in subject["teachers"]:
            print(teacher, end=', ')

        # Check if there is any duplicate
        skip = isHere(output, subject)

        # If not, ask the link
        if not skip:
            link = input("\nLink (no for skipping this): ")

        # noinspection PyUnboundLocalVariable
        # If skip is a list or the link we provided is enough
        if skip or link != "no" and link.__len__() > 0:
            # noinspection PyUnresolvedReferences
            # If we have a duplicate, set the duplciate, else the link
            subject["link"] = skip["link"] if skip else link

            # Get the password
            password = ""
            # If skip
            if skip:
                # noinspection PyUnresolvedReferences
                # If the list contains a password
                if skip.keys().__contains__("password"):
                    # noinspection PyUnresolvedReferences
                    password = skip["password"]
            else:
                # Ask
                password = input("Password (empty if nothing): ")

            # If it's more then 0, then we have a password
            if password.__len__() != 0:
                subject["password"] = password

            # Add everything to the list
            output.append(subject)
        clear()
    return output
