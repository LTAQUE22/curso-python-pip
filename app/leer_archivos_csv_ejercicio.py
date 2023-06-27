# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 14:58:29 2023

@author: paola
"""
import csv

def read_csv(path):

   with open(path, 'r') as csvfile:
      reader=csv.reader(csvfile, delimiter=',')
      my_dict={}
      for i in reader:
         my_dict[i[0]]=int(i[1]) 
      total=sum(my_dict.values())
   return total

response = read_csv('./data.csv')
print(response)