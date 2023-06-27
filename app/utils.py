# -*- coding: utf-8 -*-
"""
Created on Wed May 31 08:43:06 2023

@author: paola
"""
def  get_population(pais_dict):
    population_dict={
        "2022":pais_dict["2022 Population"],
        "2020":pais_dict["2020 Population"],
        "2015":pais_dict["2015 Population"],
        "2010":pais_dict["2010 Population"],
        "2000":pais_dict["2000 Population"],
        "1990":pais_dict["1990 Population"],
        "1980":pais_dict["1980 Population"],
        "1970":pais_dict["1970 Population"]
        
        }
    labels=population_dict.keys()
    values=population_dict.values()
    return labels, values

def population_by_country(data, country):
    result=list(filter(lambda item :item['Country/Territory']==country, data))
    return result
