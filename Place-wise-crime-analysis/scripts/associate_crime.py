# -*- coding: utf-8 -*-
"""
Created on Wed May 11 23:34:09 2016

@author: Shan
"""
import pandas as pd
import pickle



def point_inside_polygon(x,y,poly):

    n = len(poly)
    inside =False

    p1x,p1y = poly[0]
    for i in range(n+1):
        p2x,p2y = poly[i % n]
        if y > min(p1y,p2y):
            if y <= max(p1y,p2y):
                if x <= max(p1x,p2x):
                    if p1y != p2y:
                        xinters = (y-p1y)*(p2x-p1x)/(p2y-p1y)+p1x
                    if p1x == p2x or x <= xinters:
                        inside = not inside
        p1x,p1y = p2x,p2y

    return inside
    
    

parks_formatted = []
with open("E:\\RelevancyNEWT\\Crime\\tag_crimes_in_parks\\formatted_parks.p",'rb') as fp:
    parks_formatted = pickle.load(fp)
    
    
    
df = pd.DataFrame()
park_count = []
with open("E:\\RelevancyNEWT\\Crime\\Data\\reports.p",'rb') as fp:
   df = pickle.load(fp)
   
ass_id = []
ass_title = []
is_associated = []

for i in range(len(df['latLang'])):
    ass_id.append(0)
    ass_title.append('')
    is_associated.append(False)
   
df['is_associated'] = is_associated
df['place_id'] = ass_id
df['place_title'] = ass_title

df =df[df.offence_category != 'othercrimes']
df =df[df.offence_category != 'miscellaneous']



df = df.reset_index()
total = 0


length = len(df['latLang'])
for index  in range(len(parks_formatted)):
    park = []

    park_enc = parks_formatted[index]['polygon']
    x1 = []
    y1 = []
    for j in park_enc:
        temp_x = float(j['x'])
        temp_y = float(j['y'])
        x1.append(temp_x)
        y1.append(temp_y)
        park.append((temp_x,temp_y))
    

    count = 0
    print(index)
    #print(parks_formatted[index]['title'])
    for i in range(length):
        if df.loc[i,'is_associated'] == False:
            lato = df.loc[i,'latLang']
            if ',' in lato:
                x = float(lato.split(',')[1])
                y = float(lato.split(',')[0])
                if len(park) > 0:
                    if point_inside_polygon(x,y,park):
                        df.loc[i,'is_associated'] = True
                        df.loc[i,'place_id'] = parks_formatted[index]['id']
                        df.loc[i,'place_title'] = parks_formatted[index]['title']
                        
                        count += 1
                        total += 1
    
    park_count.append(count)

'''

df.to_csv("E:\\RelevancyNEWT\\Crime\\tag_crimes_in_parks\\parkss.csv", sep=',')






df = pd.DataFrame()

with open("E:\\RelevancyNEWT\\Crime\\tag_crimes_in_parks\\tagged_parks.p",'rb') as fp:
   df = pickle.load(fp)
   


'''

df = df[df.is_associated == True]


df.to_csv("E:\\RelevancyNEWT\\Crime\\tag_crimes_in_parks\\filter_inparks.csv", sep=',')


   