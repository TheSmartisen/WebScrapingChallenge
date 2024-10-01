import requests

base_url = "https://quotes.toscrape.com/api/quotes"
page = 1
nb_quote = 0

load_data = True

while load_data:
    response = requests.get(base_url + f"?page={page}" )

    if response.status_code == 200:
        data = response.json()

        load_data = data["has_next"]
        if load_data:
            current_quotes = len(data["quotes"])
            print(f"Nombre de quotes récupérer sur page {page} : {current_quotes}")
            nb_quote += current_quotes
            page += 1
    else:
        print(f"Erreur lors de la récupération de la page {page}")
        load_data = False
        break

print()
print(f"Il y a {nb_quote} sur cette page")