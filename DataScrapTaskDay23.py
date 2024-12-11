import requests
from bs4 import BeautifulSoup
import pandas as pd


bData1 = []
pN = 1
for j in range(1,51):
    BURL = f'https://books.toscrape.com/catalogue/page-{pN}.html'
    data = requests.get(url='https://books.toscrape.com/catalogue/page-2.html',headers={'user-agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Mobile Safari/537.36'})
    Bsoup = BeautifulSoup(data.content)
    for i in Bsoup.find_all('article',{'class':'product_pod'}):
        img = i.find('div',attrs={'class':'image_container'}).a.img
        imgdata = { 'src':img.attrs['src'],
                    'alt':img.attrs['alt']}
        rating1 = i.find(['p'],{'class':['star-rating']})
        price1 = i.find(['p'],{'class':['price_color']})
        ti = i.find('h3').a.attrs['title']
        bData={'Imgdata':imgdata,
            'Price':(price1.text.split('£')[1]),
            'Rating':rating1.attrs['class'][1],
            'Title':ti}
        bData1.append(bData)
    pN+=1
dtdf = pd.DataFrame(bData1)
dtdf.to_csv('BooksScrapeData.csv')