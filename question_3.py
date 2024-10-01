import requests
from bs4 import BeautifulSoup

# URLs pour la connexion et la navigation
URL_login = "https://quotes.toscrape.com/login"
URL_base = "https://quotes.toscrape.com"

# Créer une session pour conserver les cookies et maintenir l'authentification
session = requests.Session()

# Récupérer la page de login
login_page = session.get(URL_login)
soup = BeautifulSoup(login_page.content, "html.parser")

# Extraire le token CSRF
csrf_token = soup.find('input', {'name': 'csrf_token'})['value']

# Informations d'identification pour la connexion
DATA_login = {
    'username': 'patoche',  # Nom du champ 'username'
    'password': '**secret**',  # Nom du champ 'password'
    'csrf_token': csrf_token  # Token CSRF
}

# Envoyer la requête POST pour se connecter
login_response = session.post(URL_login, data=DATA_login)

# Vérifier si la connexion a réussi
if login_response.status_code == 200:
    print("Connexion réussie")

    nb_pages = 1
    current_page = session.get(URL_base)

    while current_page.status_code == 200:
        soup = BeautifulSoup(current_page.content, "html.parser")
        print(f"Analyse de la page {nb_pages}...")

        next_element = soup.find("li", class_="next")

        if next_element is not None:
            next_url = URL_base + next_element.find("a")["href"]
            current_page = session.get(next_url)
            nb_pages += 1
        else:
            break

    print(f"Le nombre total de pages analysées est : {nb_pages}")

else:
    print("Échec de la connexion")