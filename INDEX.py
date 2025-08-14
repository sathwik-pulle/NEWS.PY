import requests
from bs4 import BeautifulSoup


url = 'https://www.bbc.com/news'


response = requests.get(url)
html = response.text


soup = BeautifulSoup(html, 'html.parser')


headlines = []
for item in soup.find_all('div', attrs={'data-component': 'text-block'}):
    headline = item.find('h3')
    if headline:
        headlines.append(headline.get_text())


top_headlines = headlines[:10]


print("Top BBC News Headlines:")
for i, headline in enumerate(top_headlines, 1):
    print(f"{i}. {headline}")


with open('headlines.txt', 'w', encoding='utf-8') as f:
    for i, headline in enumerate(top_headlines, 1):
        f.write(f"{i}. {headline}\n")

print(f"\nSaved {len(top_headlines)} headlines to headlines.txt")
