import pandas as pd
from bs4 import BeautifulSoup
import requests

Product_Name = []
Prices = []
Description = []
Reviews = []

url = "https://www.consciousfood.com/collections/dry-fruits"

# for i in range(2, 5):
r = requests.get(url)
soup = BeautifulSoup(r.text, "lxml")
box = soup.find("div",class_ = "collection page-width")

names = box.find_all("a", class_="full-unstyled-link")
for i in names:
    name = i.text
    Product_Name.append(name)


prices = box.find_all("#text")
for i in prices:
    price = i.text
    Prices.append(price)

print(len(Product_Name))
print(Prices)


# cleaned_prices = []
# for price in Prices:
#     cleaned_price = price.replace('\nSale price', '').replace(',', '').strip()
#     cleaned_prices.append(cleaned_price)

# np = soup.find('a', class_="pagination__next link")
# print(np)
# if np is not None:
#     cnp = "https://www.farmley.com" + np.get("href")
#     url = cnp
# else:
#     break

# df = pd.DataFrame({"Product Name": Product_Name, "Prices": cleaned_prices})
# print(df)

# df.to_csv("Farmley.csv")