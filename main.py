# ©Rishabh Tripathi (github.com/ristri)
from bs4 import BeautifulSoup
import urllib.request
from datetime import datetime

def main():
    print("©Rishabh Tripathi (github.com/ristri)")
    soup = html_source()
    img_dl(soup)
def user_input():
    url = input("Enter Website URL (with http://)-\n")
    return url
def html_source():
    req = urllib.request.urlopen(user_input()).read()
    data= BeautifulSoup(req,"html.parser")
    return data
def img_name():
    return datetime.now().strftime("%Y%m%d%H%M%S.%f" + ".jpg")
def img_dl(soup):
    i=0
    for link in soup.findAll("img"):
        img_url = link.get("src")
        if check(img_url):
            i+=1
            image = urllib.request.urlopen(img_url)
            with open(img_name(),'wb') as f:
                f.write(image.read())
                print("Downloaded %d" %i)
def check(img_url):
    return (img_url.endswith(".jpg") or img_url.endswith(".jpeg")) and (img_url.startswith("http") or img_url.startswith("https"))

if __name__ == '__main__':
    main()
