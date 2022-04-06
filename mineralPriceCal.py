import mineralCroller
import ExcelDataExtracter
import formulaHandler

# DB에서 계산할 광물 이름 추출
mineralNameList = ExcelDataExtracter.getMineralNameList()
print(mineralNameList)

# 광물마다 계산 (EN)
for mineralName in mineralNameList:
    chemicalFormula = mineralCroller.getChemicalFormulaBy(mineralName)
    formulaHandler.findElemetnsFromFormula(chemicalFormula)
