import requests
from bs4 import BeautifulSoup

url = "https://proglib.io/?tags%5B%5D=da3eaa9f-1111-4e25-83dd-8780deff020b&page=1"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    articles = soup.find_all("article", class_="block preview-card")
    for article in articles:
        title_tag = article.find("h2", class_="preview-card__title")
        description_tag = article.find('div', class_="preview-card__text")
        link_tag = article.find("a", class_="no-link")
        if title_tag and link_tag:
            title = title_tag.get_text(strip=True)
            description = description_tag.get_text(strip=True)
            link = "https://proglib.io" + link_tag["href"]
            print(f"Название: {title}")
            print(f"Описание: {description}")
            print(f"Ссылка: {link}\n")
else:
    print("Не удалось загрузить страницу")
