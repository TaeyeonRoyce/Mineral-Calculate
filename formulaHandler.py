import ExcelDataExtracter
import re

# formula examples
# Zn4Si2O7(OH)2 · H2O
# As4S4
# α-Fe3+O(OH)
# Pb5(VO4)3Cl
# Fe2+Fe3+2O4
# PbS
testFprm = "Zn4Si2O7(O2H)4"
testFormula = "Ca2[Al2Si4O12]2 · (H2O)12"

# [Zn, Si, P]
# [3 ,  8, 1]
# => {Zn : 3, Si : 8, P : 1}
def toDictionary(symbols, amounts):
    formDict = {}
    for i in range(len(symbols)):
        if symbols[i] in formDict:
            formDict[symbols[i]] += amounts[i]
            continue
        formDict[symbols[i]] = amounts[i]
    return formDict


# Zn4Si2O7H2O
# => {Zn : 4, Si : 2, O : 8, H : 2}
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
    return toDictionary(symbols, amounts)


# Zn4Fe3+O7[OH]2 · H2O
# => Zn4FeO7(OH)2H2O
def removeNoiseChar(formula):
    removeRegex = "([0-9]\+)| · |α-| "
    leftRegex = "\{|\["
    rightRegex = "\}|\]"
    formula = re.sub(removeRegex, "", formula)
    # formula = re.sub(followingRemove, "", formula)
    formula = re.sub(leftRegex, "(", formula)
    formula = re.sub(rightRegex, ")", formula)
    return formula


# H2O, 2
# => {O : 2, H: 4}
def mutipleCount(subFormula, num):
    countDict = countElement(subFormula)
    for key in countDict:
        countDict[key] *= int(num)
    return countDict


def containBracket(formula):
    if "(" in formula:
        return True
    return False


# {Zn : 1, O : 3}
# {O : 4, H : 2}
# => {Zn : 1, O : 7, H : 2}
def sumTwoDictionary(toDict, fromDict):
    for key in fromDict:
        if key in toDict:
            toDict[key] += fromDict[key]
        else:
            toDict[key] = fromDict[key]


# Zn4Si2O7(O2H)4
# => {Zn : 4, Si : 2, O : 15, H : 4}
def findElemetnsFromFormula(formula):
    elementDict = {}
    formula = removeNoiseChar(formula)
    if containBracket(formula):
        formulaSize = len(formula)
        newFormula = ""
        cursor = 0
        while cursor < formulaSize:
            letter = formula[cursor]
            if letter == "(":
                cursor += 1
                subFormula = ""
                amount = ""
                while cursor < formulaSize and formula[cursor] != ")":
                    subFormula += formula[cursor]
                    cursor += 1
                cursor += 1
                while cursor < formulaSize and formula[cursor].isdecimal():
                    amount += formula[cursor]
                    cursor += 1
                if amount == "":
                    amount = "1"
                fromDict = mutipleCount(subFormula, amount)
                sumTwoDictionary(elementDict, fromDict)
                continue
            newFormula += letter
            cursor += 1
        formula = newFormula
    fromDict = countElement(formula)
    sumTwoDictionary(elementDict, fromDict)
    return elementDict


# {"Zn" : 4, "Si" : 2, "O" : 10, "H" : 4}
# => {'Zn': 542.89, 'Si': 116.61, 'O': 332.13, 'H': 8.37}
# Zn4Si2O7(OH)2 · H2O 에서 1Kg당 몰 함량
def calMoleAmount(formulaDict):
    massOfMineralPerMole = 0
    for element in formulaDict:
        elementMass = ExcelDataExtracter.getElementMassPerMole(element)
        elementMass *= float(formulaDict[element])
        massOfMineralPerMole += elementMass
    perKGram = 1000 / massOfMineralPerMole

    elementPerKG = {}
    for element in formulaDict:
        massPerKG = (
            formulaDict[element]
            * ExcelDataExtracter.getElementMassPerMole(element)
            * perKGram
        )
        elementPerKG[element] = round(massPerKG, 2)
    return elementPerKG


def calPriceElementsDict(formulaDict):
    priceOfMineralPerKG = 0
    metalDict = ExcelDataExtracter.filterNoneMetal(formulaDict)
    for element in metalDict:
        price = ExcelDataExtracter.getElementPricePerKG(element)
        price *= float(metalDict[element])
        priceOfMineralPerKG += price
    return (priceOfMineralPerKG / 1000)


def toPricePerVolume(pricePerKg):
    return pricePerKg
