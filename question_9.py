from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import datetime

# Initialisation du navigateur Selenium
driver = webdriver.Chrome()

# URL cible
url = 'https://quotes.toscrape.com/random'

# Stocker les citations uniques
unique_quotes = set()

# Définir le temps de début
start_time = datetime.datetime.now()

# Nombre maximum de rechargements sans nouvelle citation pour arrêter
max_no_new_quote_iterations = 10
no_new_quote_count = 0

while no_new_quote_count < max_no_new_quote_iterations:
    # Charger la page
    driver.get(url)

    # Attendre que la page soit chargée
    time.sleep(2)

    # Extraire la citation et l'auteur
    try:
        quote_element = driver.find_element(By.CLASS_NAME, 'text')
        author_element = driver.find_element(By.CLASS_NAME, 'author')

        # Construire la citation complète (texte + auteur)
        quote = f"{quote_element.text} - {author_element.text}"

        # Vérifier si la citation est déjà collectée
        if quote not in unique_quotes:
            unique_quotes.add(quote)
            no_new_quote_count = 0  # Réinitialiser le compteur si une nouvelle citation est trouvée
            print(f"Nouvelle citation trouvée : {quote}")
        else:
            no_new_quote_count += 1
    except Exception as e:
        print(f"Erreur lors de l'extraction de la citation : {e}")
        no_new_quote_count += 1

# Fermer le navigateur
driver.quit()

# Définir le temps de fin
end_time = datetime.datetime.now()

# Calculer la durée totale
duration = end_time - start_time

# Afficher les résultats
print(f"Nombre total de citations uniques : {len(unique_quotes)}")
print(f"Durée totale pour scraper toutes les citations différentes : {duration}")

# Optionnel : Afficher toutes les citations uniques
for quote in unique_quotes:
    print(quote)