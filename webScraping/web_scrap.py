from bs4 import BeautifulSoup

"""

import requests

url = "https://www.newegg.ca/gigabyte-geforce-rtx-3080-ti-gv-n308tgaming-oc-12gd/p/N82E16814932436?Description=3080&cm_re=3080-_-14-932-436-_-Product"

result = requests.get(url)

print(result.text)

doc = BeautifulSoup(result.text,"html.parser")

print(doc.pretify())

prices = doc.find_all(text="$")

print(prices)

parent = prices[0].parent

strong = prices.find_all("strong")

print(strong.string)

"""




"""

 with open("index.html","r") as f:
	doc = BeautifulSoup(f,"html.parser")

print(doc.pretify())


tag = doc.title
tag.string = "hello"

tags = doc.find_all("p")


print(tag.string)

"""





