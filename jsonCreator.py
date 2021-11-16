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
    - Ricava anno accademico, corso di studio, anno di studio
    - Ricava l'orario
    - Trasforma l'orario in un dizionario
    - Salva il dizionario

    Ricorda:
    - La persona può scegliere più anni accademici e più giorni
'''

from jsonCreatorFiles.dataUtils import *

if __name__ == "__main__":
    # Get every urls
    urls = json.load(open("./jsonCreatorFiles/urls.json", "r"))
    # Get every years and throw error if there is a problem
    years = getYears(urls["years"])
    if years.__len__() == 0:
        quit(-1)

    informations = getUniversityInformations(urls["courses"], "2021")


'''
view=easycourse&form-type=corso&include=corso&txtcurr=1+-+PERCORSO+COMUNE+T1&anno=2021&scuola=AreaScientifica-Informatica&corso=E3101Q&anno2%5B%5D=GGG_T1%7C1&date=16-11-2021&periodo_didattico=&_lang=it&list=0&week_grid_type=-1&ar_codes_=&ar_select_=&col_cells=0&empty_box=0&only_grid=0&highlighted_date=0&all_events=0&faculty_group=0&_lang=it&all_events=0&txtcurr=1 - PERCORSO COMUNE T1
'''
