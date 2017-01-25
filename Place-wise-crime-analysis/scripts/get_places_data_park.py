import requests
import pickle
from bs4 import BeautifulSoup
import re
import time


def get_places_ids(place_ids,place_links,base_url,no_of_pages):
    
    for i in range(no_of_pages):
        url = base_url.format(str(i+1))
      
        r  = requests.get(url)
        soup = BeautifulSoup(r.text)
        
        #filtering data to get only relevant data having a links to places
        ul_data = soup.find_all('ul', {'class':"two-columns clearfix"})
        a_data = ul_data[0].find_all('a', href=True)
        
      
        for a in a_data:
            #getting data between <a> tags
            link = a['href']
            idd = ''
            i = 21
            #parsnig id between //id/ in link
            while link[i] != '/':
                idd += link[i]
                i=i+1
            place_ids.append(idd)
            place_links.append(link)
        
 
def get_place_data(place_ids,place_responses,base_url):
    for i,idd in enumerate(place_ids):
        url = base_url.format(idd)
        if i % 90 == 0:
            time.sleep(1000)
        r = requests.get(url)
        if 'debug' in r.json():
            print("faulty")
            time.sleep(1000)
            r = requests.get(url)
            
        if 'debug' in r.json():
            print("faulty")
            time.sleep(1000)
            r = requests.get(url)
        
        if 'debug' in r.json():
            place_responses.append(str(r.json())+"--id=="+idd)
        else:
            place_responses.append(r.json())
        
        
        
        
ids = []
links = []
place_responses = []
#link for parks = http://lahore.wikimapia.org/tag/194/{0}
#no of pages for park = 12       
get_places_ids(ids,links,'http://lahore.wikimapia.org/tag/194/{0}',12)
#api link = http://api.wikimapia.org/?key=D3D76525-8D5E10AC-1F182E91-2B4CB110-91F7E13E-D9EDB3F8-938CC779-9E708858&function=place.getbyid&id={0}&format=json&pack=&language=en&data_blocks=main%2Cgeometry%2Clocation%2C
get_place_data(ids,place_responses,'http://api.wikimapia.org/?key=D3D76525-8D5E10AC-1F182E91-2B4CB110-91F7E13E-D9EDB3F8-938CC779-9E708858&function=place.getbyid&id={0}&format=json&pack=&language=en&data_blocks=main%2Cgeometry%2Clocation%2C')

with open("E:\\RelevancyNEWT\\Crime\\Data\\raw_data_parks.p",'wb') as fp:
    pickle.dump(place_responses,fp)
    
#for f in *.py; do python "$f"; done
   
