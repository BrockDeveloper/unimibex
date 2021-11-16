from bs4 import BeautifulSoup
import requests
import json

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


def getWebsite(url):
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
