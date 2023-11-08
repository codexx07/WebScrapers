import pandas as pd
from bs4 import BeautifulSoup
import requests

Product_Name = []
Prices = []
Weight = []
Reviews = []

url = "https://shop.bayara.com/nuts-seeds.html"

for i in range(2,18):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "lxml")
    box = soup.find("ol",class_ = "products list items product-items")

    names = box.find_all("a", class_="product-item-link")
    for i in names:
        name=i.text
        Product_Name.append(name)
    
    prices = box.find_all("span", class_="normal-price")
    for i in prices:
        pr=i.text
        Prices.append(pr)
    # print(Prices)
    
    wt = box.find_all("div", class_="prod_default_size")
    for i in wt:
        w=i.text
        Weight.append(w)

    np = soup.find('a', class_="action next")
    cnp = np.get("href")
    if cnp is not None:
        url = cnp
    else:
        break

cleaned_prices=[9.36, 24.19, 21.56, 22.31, 12.25, 17.5, 7.0, 7.0, 7.0, 7.0, 22.0, 21.75, 30.0, 13.25, 17.5, 18.75, 15.5, 10.0, 13.0, 11.5, 17.5, 16.88, 28.99, 14.75, 17.5, 17.5, 24.88, 19.75, 16.25, 21.25, 11.25, 11.25, 7.25, 30.0, 22.25, 15.73, 28.75, 18.0, 19.63, 15.0, 14.98, 27.25, 23.13, 37.91, 8.75, 22.38, 24.5, 11.5, 11.5, 22.06, 17.25, 6.75, 6.13, 51.25, 14.5, 23.75, 4.13, 14.5, 4.38, 5.5, 4.75, 32.25, 29.5, 39.5, 32.5, 19.0, 19.75, 15.95, 35.0, 17.25, 19.5, 13.0, 9.88, 6.25, 4.25, 4.24, 4.88, 9.88, 17.88, 20.75, 18.75, 71.36, 11.0, 43.75, 19.5, 19.5, 15.75, 17.75, 34.75, 14.5, 15.75, 46.75, 37.5, 29.25, 27.5, 4.0, 26.75, 17.75, 32.25, 4.5, 26.75, 9.75, 17.75, 2.75, 11.75, 18.75, 16.75, 16.75, 16.75, 21.75, 35.25, 8.0, 14.5, 13.0, 22.5, 7.5, 12.75, 1.5, 20.75, 38.75, 17.25, 28.5, 4.25, 16.75, 26.5, 44.75, 4.5, 9.5, 9.5, 11.0, 26.5, 15.75]
    

df = pd.DataFrame({"Product Name": Product_Name, "Prices": cleaned_prices, "Weight": Weight})
print(df)

df.to_csv("Bayara4.csv")
