# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 10:33:27 2022

@author: Luis Torres
"""

import pandas as pd

# Obtener la data

url = 'Casos_positivos_de_COVID-19_en_Colombia.csv'
data = pd.read_csv(url)[:10000]


