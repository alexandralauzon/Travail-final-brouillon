# coding : utf-8

import requests, csv
from bs4 import BeautifulSoup

url = "https://www.saq.com/fr/produits"

entetes = {
    "User-Agent": "Alexandra Lauzon, étudiante journalisme UQAM"
}


pages = list(range(1,147))

n=0

for page in pages:
    # print(page)
    urlproduits = url + "?p=" + str(page) + "&product_list_limit=96"
    # print(urlproduits)

    site = requests.get(urlproduits, headers=entetes)
    # print(site.status_code) #Je vérifie ainsi si tout fonctionne bien. J'ai mon 200, je continue.
    p = BeautifulSoup(site.text, "html.parser")

    # print(p)

    lienproduits = p.find_all("a", class_="product-item-link")

    # print(lienproduits)

    for lienproduit in lienproduits:
        lien = lienproduit["href"]
        # print(lien)

        siteA = requests.get(lien, headers=entetes)
        pageA = BeautifulSoup(siteA.text,"html.parser")
    
    # # print(pageA)

        titre = pageA.find("meta",property="og:title")["content"]
        # print(titre)

        prix = pageA.find("meta",property="product:price:amount")["content"]
        # print(prix)

        categorie = pageA.find("meta",property="product:category")["content"]
        # print(categorie)

        attributs = pageA.find("ul", class_="list-attributs").text.strip()
        # print(attributs)

        siteinternet = pageA.find("meta",property="twitter:url")["content"]
        # print(siteinternet)

        fichier = "touteSaq.csv"

        infos = [titre,prix,categorie,attributs,siteinternet]
        # print(infos)

        saq = open(fichier,"a")
        saqdonnees = csv.writer(saq)
        saqdonnees.writerow(infos)




  