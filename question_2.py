import requests
from bs4 import BeautifulSoup

URL_login = "https://quotes.toscrape.com/login"
URL_base = "https://quotes.toscrape.com/"
page = requests.get(URL_login)
soup = BeautifulSoup(page.content, "html.parser")

# Créer une session pour conserver les cookies
session = requests.Session()

username = 'test'
password = 'test'
csrf_token = soup.find('input', {'name': 'csrf_token'})['value']

# Informations d'identification pour la connexion
DATA_login = {
    'username': 'patoche',  # Nom du champ 'username' à ajuster selon le formulaire réel
    'password': '**secret**',  # Nom du champ 'password'
    'csrf_token': csrf_token       # Ajouter un token CSRF si nécessaire (souvent requis pour les formulaires sécurisés)
}

# Envoyer la requête POST pour se connecter
response = session.post(URL_login, data=DATA_login)
print("POST :", URL_login)
print("username :", username)
print("password :", password)
print("csrf_token :", csrf_token)
print()

# Vérifier si la connexion est réussie
if response.status_code == 200:

    print("Connexion réussie")
else:
    print("Échec de la connexion")


