# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 14:58:29 2023

@author: luist
"""

import csv

def read_csv(path):
    with open(path, 'r') as csvfile:
        reader=csv.reader(csvfile, delimiter=',')
        header=next(reader)
        #print(header)
        data=[]
        for row in reader:
            iterable=zip(header, row)
            #print(list(iterable))
            country_dic={key:value for key , value in iterable}
            data.append(country_dic)
            #print(country_dic)
        return data
    

if __name__=='__main__':
    data=read_csv('./data.csv')
    print(data[0])
    
