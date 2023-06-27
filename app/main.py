# -*- coding: utf-8 -*-
"""
Created on Wed May 31 08:45:50 2023

@author: luist
"""

import utils
import leer_archivos_csv
import charts



def run():
    data=leer_archivos_csv.read_csv('./data.csv')
    data=list(filter(lambda item: item['Continent']=='North America', data))

    country=list(map(lambda x: x['Country/Territory'] , data))
    porcentajes=list(map(lambda x: x['World Population Percentage'] , data))
    charts.generate_pie_chart(country, porcentajes)
    
    pais=input('Ingrese el Nombre del Pais:')

    result=utils.population_by_country(data, pais)
    
    
    if len(result)> 0:
        pais=result[0]
        labels, values=utils.get_population(pais)
        charts.generate_bar_chart(pais['Country/Territory'],labels, values)
    
if __name__ =='__main__':
    run()
    #print(country)