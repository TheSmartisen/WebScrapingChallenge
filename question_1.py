# Création d'une class structuré le resultat de fin
class Question1Category:
    def __init__(self, name, nb = 0, price_avg = 0):
        self.name = name
        self.nb = nb
        self.price_avg = price_avg
    def __str__(self):
        return f"Category : {self.name}\nNombre de livres : {self.nb}\nPrix moyen : £{self.price_avg:.2f}"


import requests
from bs4 import BeautifulSoup

# Quel le nombre de livres et le prix moyen qu'on retrouve dans chacune des catégories de ce site web ?


# 00 - Récupération URL : https://books.toscrape.com/
URL = "https://books.toscrape.com/"
page = requests.get(URL)
# 01 - Analyse HTML
soup = BeautifulSoup(page.content, "html.parser")

# 02 - Récupérer toutes les catégories avec leurs noms
results_category = soup.find(class_="nav nav-list")
#print(results_category)
list_category_elements = results_category.find_all("li")
list_category = []
for category_element in list_category_elements:
    label_element = category_element.find("a")
    obj_category = Question1Category(label_element.text.strip())
    if obj_category.name != "Books":
        URL_category = URL + label_element["href"]
        page_category = requests.get(URL_category)
        base_category_url = URL_category.rsplit('/', 1)[0]
        soup_category = BeautifulSoup(page_category.content, "html.parser")
        obj_category.nb = int(soup_category.find(class_ = "form-horizontal").find_all("strong")[0].text.strip())
        isNextElement = soup_category.find("li", class_="next")
        price_sum = 0
        price_avg = 0
        isFirstPage = True

        while isFirstPage or isNextElement is not None:
            results_article = soup_category.find("section")
            book_elements = results_article.find_all("article")
            for book_element in book_elements:
                price_element = book_element.find("p", class_="price_color")
                price = float(price_element.text.strip()[1:])
                price_sum += price
            if isNextElement is not None:
                nextURL = base_category_url + "/" + isNextElement.find("a")["href"]
                page_category = requests.get(nextURL)
                soup = BeautifulSoup(page_category.content, "html.parser")
                isNextElement = soup.find("li", class_="next")
            isFirstPage = False
        obj_category.price_avg = price_sum / obj_category.nb
        print(obj_category)
        print()

#print(list_category_elements)
# 03 - Dans le parcours, récupérer le nombre de livres dans une balise en haut à gauche
# 04 - Faire un parcours de tous les prix
# 05 - (optionnel) Si il y a le bouton next allez à cette page
# 06 - Afficher le résultat de fin