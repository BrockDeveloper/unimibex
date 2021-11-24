from bs4 import BeautifulSoup
import requests
import json
from datetime import datetime

from utils import cryptUtils

header = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:93.0) Gecko/20100101 Firefox/93.0",
          "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
          "Accept-Language": "it-IT,it;q=0.8,en-US;q=0.5,en;q=0.3",
          "Accept-Encoding": "gzip, deflate, br",
          "Referer": "https://gestioneorari.didattica.unimib.it/PortaleStudentiUnimib/index.php?view=homepage&include=&_lang=it&login=1",
          "DNT": "1",
          "Connection": "keep-alive",
          "Cookie": "",
          "Upgrade-Insecure-Requests": "1",
          "Sec-Fetch-Dest": "document",
          "Sec-Fetch-Mode": "navigate",
          "Sec-Fetch-Site": "same-origin",
          "Sec-Fetch-User": "?1"}

# idk why but they want a different header
headerCourses = {"Host": "gestioneorari.didattica.unimib.it",
                 "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:94.0) Gecko/20100101 Firefox/94.0",
                 "Accept": "application/json, text/javascript, */*; q=0.01",
                 "Accept-Language": "it-IT,it;q=0.8,en-US;q=0.5,en;q=0.3",
                 "Accept-Encoding": "gzip, deflate, br",
                 "Referer": "https://gestioneorari.didattica.unimib.it/PortaleStudentiUnimib/index.php?view=easycourse&form-type=corso&include=corso&txtcurr=1+-+PERCORSO+COMUNE+T1&anno=2021&scuola=AreaScientifica-Informatica&corso=E3101Q&anno2%5B%5D=GGG_T1%7C1&date=18-11-2021&periodo_didattico=&_lang=it&list=0&week_grid_type=-1&ar_codes_=&ar_select_=&col_cells=0&empty_box=0&only_grid=0&highlighted_date=0&all_events=0&faculty_group=0",
                 "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                 "X-Requested-With": "XMLHttpRequest",
                 "Content-Length": "386",
                 "Origin": "https://gestioneorari.didattica.unimib.it",
                 "DNT": "1",
                 "Connection": "keep-alive",
                 "Sec-Fetch-Dest": "empty",
                 "Sec-Fetch-Mode": "no-cors",
                 "Sec-Fetch-Site": "same-origin",
                 "Pragma": "no-cache",
                 "Cache-Control": "no-cache"}


def getFormattedWebsite(url):
    return BeautifulSoup(requests.get(url, headers=header).text, features="lxml")


def getYears(url):
    # Get source code
    sourceCode = requests.get(
        url,
        headers=header)

    # If we are fine
    if sourceCode.status_code == 200:
        # Return the json of it
        sourceCode = sourceCode.text
        return json.loads(sourceCode[sourceCode.index('{'):-1])
    # Print error and return nothing
    else:
        print(sourceCode.content)
        return ""


def getUniversityInformations(url, year):
    sourceCode = requests.get(
        url.replace("{YEAR}", year),
        headers=header)

    # If we are fine
    if sourceCode.status_code == 200:
        # What we are going to return
        output = {"schools": {}, "classes": []}
        '''
            Here we have a bounch of hard coded stuff.
            At the end we return "output" with everything we need inside
        '''
        sourceCode = sourceCode.text.split('\n')

        schools = sourceCode[-3]
        for school in schools.split('}')[:-1]:
            school = school[school.index('{'):] + '}'
            school = json.loads(school)
            output["schools"][school["label"]] = school["valore"]

        courses = sourceCode[0]
        for course in courses.split('"elenco_anni')[1:]:
            course = json.loads('{"elenco_anni' + course[:course.rindex('}') + 1])
            output["classes"].append(course)

        return output
    # Print error and return nothing
    else:
        print(sourceCode.content)
        return ""


def getSubjects(url, params, year, courses, school, idClasse):
    requestPost = params.replace("{COURSELABEL}", courses["label"].replace(" ", "+")) \
        .replace("{YEAR}", year) \
        .replace("{SCHOOL}", school) \
        .replace("{ID}", idClasse) \
        .replace("{COURSEVALORE}", courses["valore"].replace('|', "%7C")) \
        .replace("{DATE}", getDateToday())
    response = requests.post(url, headers=headerCourses, data=requestPost)
    if response.status_code != 200:
        print(response.content)
        return ""

    try:
        dataset = json.loads(response.text)
    except:
        print("Error when trying to analyze the content")
        return ""

    '''
        Structure of the output:
        Array of dictionary.
        - Teachers (array)
        - Day
        - Hour of start
        - Hour of end
        - Room
    '''

    a = 0

    output = []

    for course in dataset["celle"]:
        day = int(course["numero_giorno"]) - 1
        output.append({"teachers": course["docente"].strip().split(","),
                       "lesson": course["nome_insegnamento"],
                       "day": day,
                       "dayString": dataset["giorni"][day]["label"].split(" ")[0],
                       "start": course["ora_inizio"], "end": course["ora_fine"], "room": course["aula"]})

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

def getDateToday():
    return datetime.today().strftime('%d-%m-%Y')
