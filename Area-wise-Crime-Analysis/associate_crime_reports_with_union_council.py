# -*- coding: utf-8 -*-


import pandas as pd
import re

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
    
    
path = 'pop_den.csv'
df = pd.read_csv(path)

path = 'reports.csv'
reports = pd.read_csv(path)

ass_id = []
ass_title = []
is_associated = []

for i in range(len(reports['latLang'])):
    ass_id.append(0)
    ass_title.append('')
    is_associated.append(False)
   
reports['is_associated'] = is_associated
reports['uc_id'] = ass_id
reports['uc_name'] = ass_title

reports = reports[reports.offence_category != 'othercrimes']
reports =reports[reports.offence_category != 'miscellaneous']
reports =reports[reports.offence_category != 'chequedishonour']

reports = reports.reset_index()
total = 0

length = len(reports['latLang'])
for index in range(len(df)):
    uc = []

    uc_enc = df.loc[index,'poly']
    x1 = []
    y1 = []
    for j in uc_enc:
        temp_x = float(j['x'])
        temp_y = float(j['y'])
        x1.append(temp_x)
        y1.append(temp_y)
        uc.append((temp_x,temp_y))
        
    count = 0
    print(index)
    #print(parks_formatted[index]['title'])
    for i in range(length):
        if reports.loc[i,'is_associated'] == False:
            lato = reports.loc[i,'latLang']
            if ',' in lato:
                x = float(lato.split(',')[1])
                y = float(lato.split(',')[0])
                if len(uc) > 0:
                    if point_inside_polygon(x,y,uc):
                        reports.loc[i,'is_associated'] = True
                        reports.loc[i,'uc_id'] = df.loc[index,'uc_no']
                        reports.loc[i,'uc_name'] = df.loc[index,'uc_name']
                        
                        count += 1
                        total += 1


reports = reports[reports.is_associated == True]


