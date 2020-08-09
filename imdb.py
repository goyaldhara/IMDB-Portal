import requests
from bs4 import BeautifulSoup
def imdb():
    url='https://www.imdb.com/search/title?groups=top_250&sort=user_rating'
    resp=requests.get(url)
    if resp.status_code==200:
        soup=BeautifulSoup(resp.text,'html.parser')
        l=soup.find("div",{"class":"lister-list"})
        for i in l.findAll("div",{"class":"lister-item mode-advanced"}):
            for j in i.findAll("h3"):
                var2=j.text
                print(var2)
                for k in i.findAll("strong"):
                    x=k.text
                    print(x)
    else:
        print("Error,Internet connection is not available")

imdb()
input("Press enter to exit ;)")

