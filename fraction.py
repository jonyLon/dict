# numerator denominator whole part

def fractionDict(numerator,denominator,whole=0):
    dict = {}
    i = 500
    while i > 1:
      if numerator % i == 0 and denominator % i == 0:
        numerator = numerator / i
        denominator = denominator / i
        break
      i -= 1
    if numerator == denominator or denominator == 1 or numerator % denominator == 0:
        whole = numerator / denominator
        numerator = 0
        denominator = 0
    if numerator > denominator:
        whole = numerator // denominator
        numerator = numerator % denominator
    dict["whole"] = int(whole)
    dict['numerator'] = int(numerator)
    dict['denominator'] = int(denominator)
    return dict


def fractionSum(first,second):
    numerator1 = int(first['numerator'])
    denominator1 = int(first['denominator'])
    numerator2 = int(second['numerator'])
    denominator2 = int(second['denominator'])
    if denominator1 == denominator2:
      numerator = numerator1 + numerator2
      denominator = denominator1
    else:
      numerator = numerator1 * denominator2 + numerator2 * denominator1
      denominator = denominator1 * denominator2
    return fractionDict(numerator,denominator,whole=0)

# sum = fractionSum({'numerator':16,'denominator':15},{'numerator':1,'denominator':6})
# print(sum)

def fractionSub(first,second):
    numerator1 = int(first['numerator'])
    denominator1 = int(first['denominator'])
    numerator2 = int(second['numerator'])
    denominator2 = int(second['denominator'])
    if denominator1 == denominator2:
      numerator = numerator1 - numerator2
      denominator = denominator1
    else:
      numerator = numerator1 * denominator2 - numerator2 * denominator1
      denominator = denominator1 * denominator2
    return fractionDict(numerator,denominator,whole=0)

# sub = fractionSub({'numerator':12,'denominator':10},{'numerator':1,'denominator':6})
# print(sub)

def fractionMult(first,second):
    numerator1 = int(first['numerator'])
    denominator1 = int(first['denominator'])
    numerator2 = int(second['numerator'])
    denominator2 = int(second['denominator'])
    numerator = numerator1 * numerator2
    denominator = denominator1 * denominator2
    return fractionDict(numerator,denominator,whole=0)

# mult = fractionMult({'numerator':12,'denominator':10},{'numerator':1,'denominator':6})
# print(mult)

def fractionDivision(first,second):
    numerator1 = int(first['numerator'])
    denominator1 = int(first['denominator'])
    numerator2 = int(second['numerator'])
    denominator2 = int(second['denominator'])
    numerator = numerator1 * denominator2
    denominator = denominator1 * numerator2
    return fractionDict(numerator,denominator,whole=0)

# division = fractionDivision({'numerator':12,'denominator':10},{'numerator':1,'denominator':6})
# print(division)

while True:
    fraction1 = input("Enter first fraction(numerator/denominator): ").split("/")
    fraction2 = input("Enter second fraction(numerator/denominator): ").split("/")
    firstFraction = {'numerator': fraction1[0],'denominator':fraction1[1]}
    secondFraction = {'numerator': fraction2[0],'denominator':fraction2[1]}
    option = int(input("1 - Addition\n2 - Subtraction\n3 - Division\n4 - Multiplication\n0 - Exit\nChoose option: "))
    match option:
      case 0:
        break
      case 1:
          sum = fractionSum(firstFraction,secondFraction)
          print(sum)
      case 2:
          sub = fractionSub(firstFraction,secondFraction)
          print(sub)
      case 3:
          mult = fractionMult(firstFraction,secondFraction)
          print(mult)
      case 4:
          division = fractionDivision(firstFraction,secondFraction)
          print(division)
