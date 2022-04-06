import ExcelDataExtracter

# formula examples
# Zn4Si2O7(OH)2 · H2O
# As4S4
# α-Fe3+O(OH)
# Pb5(VO4)3Cl
# Fe2+Fe3+2O4
# PbS
testFprm = "Zn4Si2O7H2O"  # => {"Zn" : 4, "Si" : 2}
testFormula = "Zn4Si2O7(OH)2 · H2O"


# testFormula = "Zn43Si2O7 · H2O"
def saveToDictionary(symbols, amounts):
    formDict = {}
    for i in range(len(symbols)):
        if symbols[i] in formDict:
            formDict[symbols[i]] += amounts[i]
            continue
        formDict[symbols[i]] = amounts[i]
    return formDict


# [Zn, Si, O, H, O]
# [4 ,  2, 7, 2, 1]


def countElement(subFormula):
    symbols = []
    amounts = []
    symbolMemory = ""
    for cursor in range(len(subFormula) + 1):
        if cursor == len(subFormula):
            letter = "LAST"
        else:
            letter = subFormula[cursor]
        if cursor > 0 and letter.isupper():
            symbolTmp = ""
            amountTmp = ""
            for i in symbolMemory:
                if i.isdecimal():
                    amountTmp += i
                else:
                    symbolTmp += i
            if amountTmp == "":
                amountTmp = "1"
            symbols.append(symbolTmp)
            amounts.append(int(amountTmp))
            symbolMemory = ""
        symbolMemory += letter
    return saveToDictionary(symbols, amounts)


print(countElement(testFprm))


def mutipleCount(subFormula, num):
    countDict = countElement(subFormula)
    for key, value in countDict:
        countDict[key] *= int(num)
    return num


def containBracket(formula):
    if "(" in formula:
        return True
    return False


def findElemetnsFromFormula(formula):
    elementDict = {}
    if containBracket(formula):
        formulaSize = len(formula)
        newFormula = ""
        cursor = 0
        while cursor < formulaSize:
            letter = formula[cursor]
            if letter != "(":
                cursor += 1
                subFormula = ""
                amount = ""
                while letter[cursor] != ")":
                    subFormula += letter[cursor]
                    cursor += 1
                cursor += 1
                while letter[cursor].isdecimal():
                    amount += letter[cursor]
                mutipleCount(subFormula, amount, elementDict)
                continue
            newFormula += letter
            cursor += 1


def calMineralPrice(metal):
    # {"Zn" : 4, "Si" : 2, "O" : 10, "H" : 4}
    ExcelDataExtracter.getElementGramPerMole()


# findElemetnsFromFormula(testFormula)
