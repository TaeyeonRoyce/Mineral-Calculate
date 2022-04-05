import pandas as pd


class ExcelDataExtracter:
    databaseSource = ""
    columnName = 0
    rowAmount = 0

    def __init__(self, databaseSource, columnName, rowAmount):
        self.databaseSource = databaseSource
        self.columnName = columnName
        self.rowAmount = rowAmount

    def getListFromDataBase(databaseSource):
        mineralNameDataFrame = pd.read_excel(
            ExcelDataExtracter.databaseSource, sheet_name="DB_1", header=3, usecols="B"
        )
        mineralNameList = mineralNameDataFrame.loc[0:15, "광물 이름"].tolist()
        return mineralNameList


# # Excel DB에서 광물 이름 추출(in English)
# databaseSource = "mineralDB.xlsx"
# mineralNameDataFrame = pd.read_excel(
#     databaseSource, sheet_name="DB_1", header=3, usecols="B"
# )
# mineralNameList = mineralNameDataFrame.loc[0:15, "광물 이름"].tolist()
# print(mineralNameList)
