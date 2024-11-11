import requests
from bs4 import BeautifulSoup
def parsing():
    url = "https://proglib.io/?tags%5B%5D=da3eaa9f-1111-4e25-83dd-8780deff020b&page=1"
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers)
    result = BeautifulSoup(response.text, "html.parser")
    article = result.find("article", class_="block preview-card")
    title = result.find('h2', class_="preview-card__title").text
    description = result.find('div', class_="preview-card__text").text
    link = article.find("a", class_="no-link")
    href = "https://proglib.io" + link["href"]
    return(f'{title}\n\n{description}\n\n{href}')
'''
    url_article = requests.get(href, headers=headers)
    soup_article = BeautifulSoup(url_article.text, "html.parser")

    #author = soup_article.find('div', class_="flex align-between").get_text(strip=True)
    #author = author.find('span', class_="author-info mr-4")
    authors = soup_article.find_all("span", class_="author-info")
    for author in authors:
        name_tag = author.find("a", class_="link-reverse")
        profile_url_tag = author.find("a", class_="no-link")
        name_author = name_tag.get_text(strip=True)
        profile_url = "https://proglib.io" + profile_url_tag["href"]
    print(name_author)
    print(profile_url)
    text = soup_article.find('div', class_="block__content ugc entity__content")
    #for item in text:
        #print(item)
        #if item:
    text_article = text.get_text(strip=False)
    print(text_article)
    return(name_author + '\n' + profile_url + '\n' + text_article)
'''
