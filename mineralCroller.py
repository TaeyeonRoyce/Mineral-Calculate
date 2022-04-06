import requests
import userPrivateInfo as info
from bs4 import BeautifulSoup


searchBaseURL = info.SEARCH_BASE_URL


def getChemicalFormulaBy(mineralName):
    res = requests.get(searchBaseURL + mineralName)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "html.parser")
    chemicalFormula = soup.select_one(info.CHEMICAL_FORMULA_INDEX)
    return chemicalFormula.get_text()
