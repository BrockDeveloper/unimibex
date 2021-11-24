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

import json

from utils import dataUtils, chatUtils

if __name__ == "__main__":
    # Get every urls
    urls = json.load(open("utils/urls.json", "r"))
    # Get every years and throw error if there is a problem
    years = dataUtils.getYears(urls["years"])
    if years.__len__() == 0:
        quit(-1)

    # List we are going to use for saving every urls
    toSave = []

    while True:

        # Get year
        year = chatUtils.requestFromKeys(years)
        chatUtils.clear()
        if year.__len__() == 0:
            continue

        # Get informations from the website
        informations = dataUtils.getUniversityInformations(urls["courses"], year)
        chatUtils.clear()
        if informations.__len__() == 0:
            continue

        # Get the school
        school = chatUtils.requestFromKeys(informations["schools"])
        chatUtils.clear()
        if school.__len__() == 0:
            continue

        # Get the classes
        classes = chatUtils.getClassesFromSchool(informations["classes"], informations["schools"][school])
        chatUtils.clear()
        if classes.__len__() == 0:
            continue

        # Get the kind of study
        kindStudy = chatUtils.requestKindOfStudy(classes)
        chatUtils.clear()
        if kindStudy.__len__() == 0:
            continue

        # Get the list of years
        listCourses = chatUtils.requestFromList(kindStudy["elenco_anni"])
        chatUtils.clear()
        if listCourses.__len__() == 0:
            continue

        # Get every informations that are going to be saved
        subjects = dataUtils.getSubjects(urls["classes"], urls["params"], year, listCourses,
                                         informations["schools"][school], kindStudy["valore"])
        chatUtils.clear()
        if subjects.__len__() == 0:
            continue

        # Get links
        subjectsWithLink = chatUtils.askLinks(subjects)
        chatUtils.clear()
        if subjectsWithLink.__len__() == 0:
            continue

        # Option for saving
        toSave.extend(subjectsWithLink)
        choose = input("Save or continue? (Save/Continue)")
        chatUtils.clear()

        if choose.lower() == "save":
            print("Saving in progress..")
            dataUtils.save(toSave)
            toSave.clear()
            chatUtils.clear()
