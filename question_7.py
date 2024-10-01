"""
DISCLAIMER ==> Bon, j'avoue je me suis aidé de ChatGPT pour ce problème. Par acquis de conscience, j'ai bien lu tous le programme
pour bien comprendre ce que je voulais

"""

import requests
from bs4 import BeautifulSoup
from collections import defaultdict

# URL de base pour le site
base_url = "https://quotes.toscrape.com"

# HTML initial ou faire une requête pour le récupérer
page = requests.get("https://quotes.toscrape.com/tableful/")
html_content = page.content

# Utiliser BeautifulSoup pour analyser le HTML de la page principale
soup = BeautifulSoup(html_content, 'html.parser')

# Dictionnaire pour stocker les tags et leur nombre d'occurrences
tag_counts = defaultdict(int)

# 1. Récupérer les tags de la page principale, en excluant la section "Top Ten tags"
main_tags = soup.select("table tr td a[href*='/tag/']")

# Ajouter les tags au dictionnaire et compter les occurrences
for tag in main_tags:
    tag_text = tag.get_text()
    tag_counts[tag_text] += 1

# 2. Récupérer les liens des "Top Ten tags"
top_ten_tags = soup.select("h3 + a[href*='/tag/']")

# Parcourir chaque lien de tag du "Top Ten tags"
for top_tag in top_ten_tags:
    tag_text = top_tag.get_text()
    tag_link = base_url + top_tag['href']

    # Faire une requête pour accéder à la page du tag
    response = requests.get(tag_link)

    if response.status_code == 200:
        # Analyser la page liée à ce "Top Ten tag"
        tag_soup = BeautifulSoup(response.content, 'html.parser')

        # Récupérer les tags sur cette page en excluant la section "Top Ten tags"
        page_tags = tag_soup.select("table tr td a[href*='/tag/']")

        # Ajouter les tags au dictionnaire et compter les occurrences
        for tag in page_tags:
            tag_text = tag.get_text()
            tag_counts[tag_text] += 1
    else:
        print(f"Erreur lors de l'accès à la page de tag: {tag_text}")

# Trouver le tag le plus répétitif
most_repeated_tag = max(tag_counts, key=tag_counts.get)
most_repeated_count = tag_counts[most_repeated_tag]

# Afficher le tag le plus répétitif et son nombre d'occurrences
print(f"Le tag le plus répétitif est '{most_repeated_tag}' avec {most_repeated_count} occurrences.")

