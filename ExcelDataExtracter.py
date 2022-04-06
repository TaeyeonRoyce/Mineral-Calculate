import pandas as pd


def getMineralNameList():
    # DB정보 명세
    databaseSource = "mineralDB.xlsx"
    sheetName = "DB_1"
    startRow = 3
    column = "B"

    # Excel DB에서 광물 이름 추출(in English)
    mineralNameDataFrame = pd.read_excel(
        databaseSource, sheet_name=sheetName, header=startRow, usecols=column
    )
    mineralNameList = mineralNameDataFrame.loc[0:15, "광물 이름"].tolist()
    return mineralNameList


def getElementGramPerMole(element):
    databaseSource = "mineralDB.xlsx"
    sheetName = "Elements"
    startRow = 3
    column = "B"
