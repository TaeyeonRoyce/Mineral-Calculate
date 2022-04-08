# import ExcelDataExtracter
import requests
import userPrivateInfo as info
from bs4 import BeautifulSoup


searchBaseURL = info.SEARCH_BASE_URL
searchBaseURLWiki = info.SEARCH_WIKI_URL


def getChemicalFormulaBy(mineralName):
    res = requests.get(searchBaseURL + mineralName)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "html.parser")
    chemicalFormula = soup.select_one(info.CHEMICAL_FORMULA_INDEX)
    return chemicalFormula.get_text()


def getGSBy(mineralName):
    res = requests.get(searchBaseURLWiki + mineralName)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "html.parser")
    infoBox = soup.find("table", attrs={"class": "infobox"})
    if infoBox == None:
        return "Null"
    infoBox = infoBox.next_element.next_element
    while infoBox:
        if infoBox.next_element.next_element.getText() == "Specific gravity":
            return infoBox.next_element.next_sibling.getText()
        infoBox = infoBox.next_sibling
    return "Null"
