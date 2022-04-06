import requests
from bs4 import BeautifulSoup


searchBaseURL = "https://www.mindat.org/search.php?search="


def getChemicalFormulaBy(mineralName):
    res = requests.get(searchBaseURL + mineralName)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "html.parser")
    chemicalFormula = soup.select_one("#introdata > div:nth-child(1) > div")
    return chemicalFormula.get_text()
