import pandas as pd
import openpyxl
import mineralCroller

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
    mineralNameList = mineralNameDataFrame.loc[0:15, "광물 이름"].tolist()
    return mineralNameList


elementsDataFrame = pd.read_excel(
    databaseSource, sheet_name="Elements", index_col="Symbol"
)


def getElementGramPerMole(element):
    massDataFrame = elementsDataFrame["Mass per mole"]
    print(massDataFrame)
    mass = massDataFrame.loc[[element]]
    return float(mass)


def saveChemicalFormula():
    wb = openpyxl.load_workbook(databaseSource)
    sheet = wb.active
    mineralList = getMineralNameList()
    for i in range(len(mineralList)):
        row = i + 5
        cell = "D" + str(row)
        if sheet[cell].value == None:
            sheet[cell].value = mineralCroller.getChemicalFormulaBy(mineralList[i])
            print(sheet[cell].value)
            wb.save(databaseSource)


saveChemicalFormula()
