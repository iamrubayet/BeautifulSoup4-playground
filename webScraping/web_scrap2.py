from bs4 import BeautifulSoup
import re

with open("index2.html","r") as f:
	doc = BeautifulSoup(f,"html.parser")

tag = doc.find_all("[option]",text="undergraduate",value="some")

tag = doc.find_all(class_="btn-item")

tag = doc.find_all(text=re.compile("\$.*"),limit=5)


tag['selected']="false"
print(tag.attrs)

print(tag)

tags = doc.find_all(["p","a"])


for tag in tags:
	print(tag.strip())



for tag in tags:
	tag['placeholder']="i changed you!!!"

with open("changed.html","w") as file :
	file.write(str(doc))
