import requests
from bs4 import BeautifulSoup

url = "https://www.naturesbasket.co.in/BrandProduct/Healthy-Alternatives/631"
r = requests.get(url)
soup = BeautifulSoup(r.content, "lxml")

# Save the soup object to an HTML file
with open('output.html', 'w', encoding='utf-8') as file:
    file.write(str(soup))

# Print the first 500 characters of the soup object to the console
print(str(soup)[:])


# names = soup.find_all("a", class_="search_Ptitle")
# for i in names:
#     Product_Name.append(i.text.strip())

# prices = soup.find_all("span", class_="search_PSellingP")
# for i in prices:
#     price = i.text.strip()
#     Prices.append(price.replace('\u20b9', 'Rs'))  # Replace the Rupee symbol with 'Rs'

# df = pd.DataFrame({"Product Name": Product_Name, "Prices": Prices})

# # Convert DataFrame to string and replace problematic characters for printing
# print(df.to_string(index=False).encode('ascii', 'replace').decode())

# df.to_csv("HealthyAlternatives.csv", index=False, encoding='utf-8-sig')
