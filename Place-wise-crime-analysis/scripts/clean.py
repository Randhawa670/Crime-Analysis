# -*- coding: utf-8 -*-


import pickle

with open("E:\\Research\\Crime\\Crime\\tag_crimes_in_parks\\raw_data_parks.p",'rb') as fp:
    parks_raw = pickle.load(fp)
   
parks_formatted = []

for park_info in parks_raw:
    park = {
    'title' : park_info['title'],
    'polygon' : park_info['polygon']
    }
    
    parks_formatted.append(park)


with open("E:\\Research\\Crime\\Crime\\tag_crimes_in_parks\\formatted_parks.p",'wb') as fp:
    pickle.dump(parks_formatted,fp)