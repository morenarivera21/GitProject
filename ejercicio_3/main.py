import requests

url_cooktails = 'https://www.thecocktaildb.com/api/json/v1/1/search.php'

http_rsp = requests.get(url_cooktails, params={'s': 'Margarita'})

rsp_json = http_rsp.json()


class Drinks:

    def __init__(self, title, strAlcoholic, strInstructions):
        self.title = title
        self.strAlcoholic = strAlcoholic
        self.strInstructions = strInstructions

    def __str__(self):
        return f"{self.title}, {self.strInstructions}, {self.strAlcoholic}"


drink_type = input('Drink >> ')
req_params = {'s': drink_type}

http_rsp = requests.get(url_cooktails, params=req_params)

print(http_rsp)
