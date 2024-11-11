import requests
from bs4 import BeautifulSoup
url = "https://proglib.io/?tags%5B%5D=da3eaa9f-1111-4e25-83dd-8780deff020b&page=1"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)
result = BeautifulSoup(response.text, "html.parser")
article = result.find("article", class_="block preview-card")
title = result.find('h2', class_="preview-card__title").text
description = result.find('div', class_="preview-card__text").text
link = article.find("a", class_="no-link")
href = "https://proglib.io" + link["href"]
print(title)
print(description)
print(href)