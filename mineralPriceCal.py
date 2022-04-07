import ExcelDataExtracter
import formulaHandler

# DB에서 계산할 광물 이름 추출 후 화학식 검색 후 저장
# ExcelDataExtracter.saveChemicalFormula()
formulaList = ExcelDataExtracter.getFormulaList()
for i in formulaList:
    print("{} : {}".format(i, formulaHandler.findElemetnsFromFormula(i)))

# 광물마다 계산 (EN)
testFormula = "Zn4Si2O7(OH)2 · H2O"
# print(formulaHandler.findElemetnsFromFormula(testFormula))
