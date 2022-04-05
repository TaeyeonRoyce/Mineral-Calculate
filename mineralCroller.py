import requests
from bs4 import BeautifulSoup


searchBaseURL = "https://en.wikipedia.org/wiki/"


def searchByName(mineralName):
    res = requests.get(searchBaseURL + mineralName)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "html.parser")
    chemicalFormula = soup.select_one("table.infobox > tbody > tr:nth-child(5) > td")
    print(chemicalFormula.get_text())
