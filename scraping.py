import requests
import csv
from bs4 import BeautifulSoup

url="http://lawrato.com/lawyers"
r = requests.get(url)


lawyers_list=[]


soup=BeautifulSoup(r.content,"html.parser")


lawyers_data = soup.find_all("div",{"class":"col-lg-7 col-xs-7 pad-lt-rt"})
for item in lawyers_data:
    
    
    lawyer_name= item.find_all("span",{"itemprop":"name"})[0]
    lawyer_name=lawyer_name.get_text(strip=True)
    print lawyer_name
    lawyer_address= item.find_all("span",{"itemprop":"addressLocality"})[0]
    lawyer_address=lawyer_address.get_text(strip=True)
    print lawyer_address
    lawyer_experience= item.find_all("p",{"itemscope":""})[1]
    lawyer_experience=lawyer_experience.get_text(strip=True)
    print lawyer_experience
    lawyers= [lawyer_name,lawyer_address,lawyer_experience]
    lawyers_list.append(lawyers)
    print ""
   
   
with open("lawyers.csv", "w") as toWrite:
    writer = csv.writer(toWrite, delimiter=",")
    writer.writerow(["name", "address", "experience"])
    for lawyer_item in lawyers_list:
    	writer = csv.writer(toWrite, delimiter=",")
        writer.writerow([lawyer_item[0],lawyer_item[1],lawyer_item[2]])
