import requests
from bs4 import BeautifulSoup
import pandas as pd
products = []
prices_list =[]

# url = "https://www.ebay.com/sch/i.html?_from=R40&_nkw=smart+watch&_sacat=0&_pgn=0" 
# r = requests.get(url)
# # print(r)
# soup = BeautifulSoup(r.text,"lxml")
# # box = soup.find("div", class_="srp-river-main")

for i in range(1,10):
    url = "https://www.ebay.com/sch/i.html?_from=R40&_nkw=smart+watch&_sacat=0&_pgn="+ str(i) 
    r = requests.get(url)
    # print(r)
    # print(url)
    soup = BeautifulSoup(r.text,"lxml")
    box = soup.find("div", class_="srp-river-main")

    # np = soup.find("a",class_ = "pagination__item").get("href")
    # print(np)
    # print(np)
    # url = np
    # r = requests.get(url)
    # soup = BeautifulSoup(r.text,"lxml")

    # ------------------Name

    names = box.find_all("div",class_ = "s-item__title")[1:61]
    # print(names)
    for i in names:
        name = i.text
        products.append(name)
    # print(products)

    # ------------------Prices
    prices = box.find_all("span",class_ = "s-item__price")[1:61]
    # print(prices)

    for i in prices:
        price = i.text
        prices_list.append(price)
    # print(prices_list)

df = pd.DataFrame({"Product Discription":products,"Prices":prices_list})
print(df)
df.to_csv("Smart watches.csv")