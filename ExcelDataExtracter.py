import pandas as pd
import openpyxl
import mineralCroller
import formulaHandler
import json

databaseSource = "mineralDB.xlsx"


def getMineralNameList():
    # DB정보 명세
    sheetName = "DB_1"
    startRow = 3
    column = "B"

    # Excel DB에서 광물 이름 추출(in English)
    mineralNameDataFrame = pd.read_excel(
        databaseSource, sheet_name=sheetName, header=startRow, usecols=column
    )
    mineralNameList = mineralNameDataFrame.loc[0:55, "광물 이름"].tolist()
    return mineralNameList


elementsDataFrame = pd.read_excel(
    databaseSource, sheet_name="Elements", index_col="Symbol"
)
massDataFrame = elementsDataFrame["Mass per mole"]


def getElementMassPerMole(element):
    mass = massDataFrame.loc[[element]]
    return float(mass)


def getFormulaList():
    # DB정보 명세
    sheetName = "Result"
    startRow = 3
    column = "D"

    # Excel DB에서 광물 이름 추출(in English)
    mineralNameDataFrame = pd.read_excel(
        databaseSource, sheet_name=sheetName, header=startRow, usecols=column
    )
    formulaList = mineralNameDataFrame.loc[0:70, "화학식"].tolist()
    return formulaList


def saveChemicalFormula():
    wb = openpyxl.load_workbook(databaseSource)
    sheet = wb.active
    mineralList = getMineralNameList()
    column = "D"
    for i in range(len(mineralList)):
        row = i + 5
        cell = column + str(row)
        if sheet[cell].value == None:
            sheet[cell].value = mineralCroller.getChemicalFormulaBy(mineralList[i])
            print(sheet[cell].value)
            wb.save(databaseSource)


def saveComponentsDict():
    wb = openpyxl.load_workbook(databaseSource)
    sheet = wb.active
    formulaList = getFormulaList()
    column = "F"
    for i in range(len(formulaList)):
        row = i + 5
        cell = column + str(row)
        if sheet[cell].value == None:
            sheet[cell].value = json.dumps(
                formulaHandler.findElemetnsFromFormula(formulaList[i])
            )
            print("save : ", sheet[cell].value)
            wb.save(databaseSource)
