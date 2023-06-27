# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 10:11:14 2023

@author: luist
"""

import matplotlib.pyplot as plt



def generate_bar_chart(name,labels, values):

    fig , ax =plt.subplots()
    ax.bar(labels, values)
    plt.savefig(f'./imgs/bar_{name}.png')
    plt.close()

def generate_pie_chart(labels, values):
    fig , ax =plt.subplots()
    ax.pie(values,labels=labels)
    ax.axis('equal')
    plt.savefig(f'pie.png')
    plt.close()

if __name__=='__main__':
    labels=['a','b','c','d']
    values=[100,200,800,15]
    generate_bar_chart(labels, values)
    generate_pie_chart(labels, values)


