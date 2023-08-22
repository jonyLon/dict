import requests
import json
def checkExchangeRate():
    result = requests.get("https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=5")
    obj =  json.loads(result.content)
    return obj

def euroToHryvnia(euro):
  object = checkExchangeRate()
  for i in object:
    for value in i.values():
        if value == "EUR":
          rate = i["sale"]
          return float(rate)*euro

def hryvniaToEuro(hryvnia):
  object = checkExchangeRate()
  for i in object:
    for value in i.values():
        if value == "EUR":
          rate = i["buy"]
          return hryvnia / float(rate)

print(hryvniaToEuro(400))

def usdToHryvnia(usd):
  object = checkExchangeRate()
  for i in object:
    for value in i.values():
        if value == "USD":
          rate = i["sale"]
          return float(rate)*usd

def hryvniaToUSD(hryvnia):
  object = checkExchangeRate()
  for i in object:
    for value in i.values():
        if value == "USD":
          rate = i["buy"]
          return hryvnia / float(rate)
        

while True:
  option = int(input("1 - euro to hryvnia\n2 - hryvnia to euro\n3 - USD to hryvnia\n4 - hryvnia to USD\n0 - exit\nChoose option: "))
  match option:
    case 0:
        break
    case 1:
        amount = float(input("Enter the amount in EUR: "))
        print(f'You will get {euroToHryvnia(amount)} hryvnias')
    case 2:
        amount = float(input("Enter the amount in hryvnias: "))
        print(f'You will get {hryvniaToEuro(amount)} EUR')
    case 3:
        amount = float(input("Enter the amount in USD: "))
        print(f'You will get {usdToHryvnia(amount)} hryvnias')
    case 4:
        amount = float(input("Enter the amount in hryvnias: "))
        print(f'You will get {hryvniaToEuro(amount)} USD')
    case _:
        print("Invalid input. Try again")