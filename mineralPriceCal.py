import pandas as pd

databaseSource = "mineralDB.xlsx"
mineralNameDataFrame = pd.read_excel(
    databaseSource, sheet_name="DB_1", header=3, usecols="B"
)
mineralList = mineralNameDataFrame["광물 이름"].tolist()
print(mineralList)
