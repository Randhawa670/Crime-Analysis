import numpy as np
from matplotlib import pyplot as p  #contains both numpy and pyplot
import math
import pandas as pd
import pickle

R = 6378137


def distance(lat1,lon1,lat2,lon2):
    p = 0.017453292519943295
    a = 0.5 - math.cos((lat2 - lat1) * p)/2 + math.cos(lat1 * p) * math.cos(lat2 * p) * (1 - math.cos((lon2 - lon1) * p)) / 2
    return 12742 * math.asin(math.sqrt(a))*1000




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
    
    
    
    
    
    
    
def get_boundary(poly,x1,y1):

    for i in range(len(y1)):
        poly.append((x1[i],y1[i]))
        

    x2 = [];y2=[]
    shapes = [[x1,y1]]
    for shape in shapes:
        x,y = shape
        for i in range(len(x)):
            
            temp1x = x[i] - ((35/R) * (180/math.pi))
            temp1y = y[i] - ((35/(R*math.cos(math.pi*x[i]/180))) * (180/math.pi))
            temp2x = x[i] + ((35/R) * (180/math.pi))
            temp2y = y[i] + ((35/(R*math.cos(math.pi*x[i]/180))) * (180/math.pi))
            temp3x = x[i] - ((35/R) * (180/math.pi))
            temp3y = y[i] + ((35/(R*math.cos(math.pi*x[i]/180))) * (180/math.pi))
            temp4x = x[i] + ((35/R) * (180/math.pi))
            temp4y = y[i] - ((35/(R*math.cos(math.pi*x[i]/180))) * (180/math.pi))
            temp5x = x[i] + ((35/R) * (180/math.pi))
            temp5y = y[i] + ((35/R) * (180/math.pi))
            temp6x = x[i] - ((35/R) * (180/math.pi))
            temp6y = y[i] - ((35/R) * (180/math.pi))
            temp7x = x[i] + ((35/R) * (180/math.pi))
            temp7y = y[i] - ((35/R) * (180/math.pi))
            temp8x = x[i] - ((35/R) * (180/math.pi))
            temp8y = y[i] + ((35/R) * (180/math.pi))
            temp9x = x[i] + ((35/(R*math.cos(math.pi*x[i]/180))) * (180/math.pi))
            temp9y = y[i] + ((35/(R*math.cos(math.pi*x[i]/180))) * (180/math.pi))
            temp10x = x[i] - ((35/(R*math.cos(math.pi*x[i]/180))) * (180/math.pi))
            temp10y = y[i] - ((35/(R*math.cos(math.pi*x[i]/180))) * (180/math.pi))
            temp11x = x[i] + ((35/(R*math.cos(math.pi*x[i]/180))) * (180/math.pi))
            temp11y = y[i] - ((35/(R*math.cos(math.pi*x[i]/180))) * (180/math.pi))
            temp12x = x[i] - ((35/(R*math.cos(math.pi*x[i]/180))) * (180/math.pi))
            temp12y = y[i] + ((35/(R*math.cos(math.pi*x[i]/180))) * (180/math.pi))
            
            approx = [(temp1x,temp1y),(temp2x,temp2y),(temp3x,temp3y),(temp4x,temp4y),(temp5x,temp5y),(temp6x,temp6y),(temp7x,temp7y),(temp8x,temp8y),(temp9x,temp9y),(temp10x,temp10y),(temp11x,temp11y),(temp12x,temp12y)]
            
            score = [0 for i in range(12)]
            inside = [True for i in range(12)]
            dist = [0 for i in range(12)]
            
            
            
            for j in range(len(y)):
                for k in range(12):
                    pointx,pointy = approx[k]
                    inside[k] = point_inside_polygon(pointx,pointy,poly)
                    dist[k] = distance(x[j],y[j],pointx,pointy)
                
                score[dist.index(max(dist))] += 1
                
            all_inside = False
            l = 0
            while l < 12:
                ind = score.index(max(score))
                if inside[ind] == False:
                    pointx,pointy  = approx[ind]
                    x2.append(pointx)
                    y2.append(pointy)
                    all_inside = False
                    break
                else:
                    all_inside = True
                    score[ind] = 0
                    
            if all_inside == True:
                pointx,pointy  = approx[0]
                x2.append(pointx)
                y2.append(pointy)
                
    '''
    p.plot(x2*10000,y2*10000)
    p.show()
    '''
    enc_polygon = []
    for i in range(len(x2)):
        point = {
        'x' : 0.0,
        'y' : 0.0
        }
        point['x'] = y2[i]
        point['y'] = x2[i]
        enc_polygon.append(point)
        
    return enc_polygon
        
    
    




#getting all formated parks
parks_formatted = []


with open("E:\\RelevancyNEWT\\Crime\\tag_crimes_in_parks\\formatted_parks.p",'rb') as fp:
    parks_formatted = pickle.load(fp)


for i in range(len(parks_formatted)):
    if(i!=555) & (i!=558):
        poly_new = []
        x1 = []
        y1 = []
        poly = parks_formatted[i]['polygon']
        for j in poly:
            x1.append(float(j['y']))
            y1.append(float(j['x']))
        print(i)
        #print(x1)
        parks_formatted[i]['enc_polygon'] = get_boundary(poly_new,x1,y1)
    
    


with open("E:\\RelevancyNEWT\\Crime\\tag_crimes_in_parks\\formatted_parks.p",'wb') as fp:
    pickle.dump(parks_formatted,fp)















