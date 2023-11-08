import pandas as pd
from bs4 import BeautifulSoup
import requests

Product_Name = []
Prices = []
Description = []
Reviews = []

url = "https://www.farmley.com/collections/all"      #Change URL according to the website 

for i in range(2, 5):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "lxml")

    names = soup.find_all("a", class_="product-item__title text--strong link")
    for i in names:
        name = i.text
        Product_Name.append(name)

    prices = soup.find_all("span", class_="price price--highlight")
    for i in prices:
        price = i.text
        Prices.append(price)

    cleaned_prices = []
    for price in Prices:
        cleaned_price = price.replace('\nSale price', '').replace(',', '').strip()
        cleaned_prices.append(cleaned_price)

    np = soup.find('a', class_="pagination__next link")
    # print(np)
    if np is not None:
        cnp = "https://www.farmley.com" + np.get("href")
        url = cnp
    else:
        break
print(Product_Name)
df = pd.DataFrame({"Product Name": Product_Name, "Prices": Prices})
print(df)

df.to_csv("Outputs/Farmley.csv")     #Change File name according to use