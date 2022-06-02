# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 10:33:27 2022

@author: Luis Torres
"""

import pandas as pd
import matplotlib.pyplot as plt


# Obtener la data

url = 'Casos_positivos_de_COVID-19_en_Colombia.csv'
data = pd.read_csv(url)[:10000]

# Tratamiento de la data (Eliminar columnas del dataset)

data.drop('Código ISO del país', axis = 1, inplace=True)
data.drop('Fecha de muerte', axis = 1, inplace=True)
data.drop('Nombre del país', axis = 1, inplace=True)
data.drop('Pertenencia étnica', axis = 1, inplace=True)
data.drop('Nombre del grupo étnico', axis = 1, inplace=True)
data.drop('Fecha de inicio de síntomas', axis = 1, inplace=True)
data.drop('Unidad de medida de edad', axis = 1, inplace=True)
data.drop('Código DIVIPOLA departamento', axis = 1, inplace=True)
data.drop('Código DIVIPOLA municipio', axis = 1, inplace=True)
data.drop('ID de caso', axis = 1, inplace=True)


# 1.Número de casos de Contagiados en el País

numero_casos = data.shape[0]
print(f'El número de casos de contagiados en el pais es de: {numero_casos}')


# 2.Número de Municipios Afectados

numero_municipios = data['Nombre municipio'].value_counts().count()
print(f'El número de municipios afectados es: {numero_municipios}')


# 3.Liste los municipios afectados (sin repetirlos)

municipios_afectados = data['Nombre municipio'].value_counts()
print(f'Municipios afectados: {municipios_afectados}')


# 4.Número de personas que se encuentran en atención en casa

data.loc[data['Ubicación del caso'] == 'casa'] = 'Leve'
data.loc[data['Ubicación del caso'] == 'CASA'] = 'Leve'
numero_atencion_casa = data[data['Ubicación del caso'] == 'Casa'].shape[0]
print(f'El numero de personas con atención en casa es de: {numero_atencion_casa}')


# 5.Número de personas que se encuentran recuperados

numero_recuperados = data[data['Recuperado'] == 'Recuperado'].shape[0]
print(f'El numero de personas recuperadas es de: {numero_recuperados}')


# 6. Número de personas que ha fallecido

numero_fallecidos = data[data['Estado'] == 'Fallecido'].shape[0]
print(f'El numero de personas que ha fallecidos es de: {numero_fallecidos}')


# 7.Ordenar de Mayor a menor por tipo de caso (Importado, en estudio, Relacionado)

tipo_caso = data['Tipo de contagio' ].value_counts().head()
print(f'Tipo de caso:\n{tipo_caso}')


# 8.Número de departamentos afectados

numero_departamentos = data['Nombre departamento'].value_counts().count()
print(f'El número de departamentos afectados es: {numero_departamentos}')


# 9.Liste los departamentos afectados(sin repetirlos)

departamentos_afectados = data['Nombre departamento'].value_counts()
print(f'Departamentos afectados: {municipios_afectados}')


# 10.Ordene de mayor a menor por tipo de atención

tipo_atencion = data['Tipo de recuperación'].value_counts().head()
print('*'*50)
print(f'Tipo de atencion:\n{tipo_atencion}')


# 11.Liste de mayor a menor los 10 departamentos con mas casos de contagiados

departamentos_mas_casos = data['Nombre departamento' ].value_counts().head(10)
print(f'Los 10 departamentos con mas caso de contagiados son:\n{departamentos_mas_casos}')


# 12.Liste de mayor a menor los 10 departamentos con mas casos de fallecidos

aux = data[data['Estado'] == 'Fallecido'].groupby('Nombre departamento')
departamentos_fallecidos = aux.size().sort_values(ascending=False).head(10)
print(f'Los 10 departamentos con más casos casos de fallecidos son:\n{departamentos_fallecidos}')


# 13.Liste de mayor a menor los 10 departamentos con mas casos de recuperados

aux = data[data['Recuperado'] == 'Recuperado'].groupby('Nombre departamento')
departamentos_recuperados = aux.size().sort_values(ascending=False).head(10)
print(f'Los 10 departamentos con más casos casos de recuperados son:\n{departamentos_recuperados}')


# 14.Liste de mayor a menor los 10 municipios con mas casos de contagiados

municipios_mas_casos = data['Nombre municipio' ].value_counts().head(10)
print(f'Los 10 municipios con mas caso de contagiados son:\n{municipios_mas_casos}')


# 15.Liste de mayor a menor los 10 municipios con mas casos de fallecidos

aux = data[data['Estado'] == 'Fallecido'].groupby('Nombre municipio')
municipios_fallecidos = aux.size().sort_values(ascending=False).head(10)
print(f'Los 10 municipios con más casos casos de fallecidos son:\n{municipios_fallecidos}')


# 16.Liste de mayor a menor los 10 municipios con mas casos de recuperados

aux = data[data['Recuperado'] == 'Recuperado'].groupby('Nombre municipio')
municipios_recuperados = aux.size().sort_values(ascending=False).head(10)
print(f'Los 10 municipios con más casos casos de recuperados son:\n{municipios_recuperados}')


# 17.Liste agrupado por departamento y en orden de Mayor a menor las ciudades con mas casos de contagiados

dep_ciud_contagios = data.groupby(['Nombre departamento', 'Nombre municipio']).size().sort_values(ascending=False)
print(f'Departamentos y sus ciudades con mas casos de contagios:\n{dep_ciud_contagios}')

# 18.Número de Mujeres y hombres contagiados por ciudad por departamento

numero_h_m_contagiados = data.groupby(['Sexo', 'Nombre municipio', 'Nombre departamento']).size().sort_values(ascending=False)
print(f'Número de Mujeres y hombres contagiados por ciudad por departamento:\n{numero_h_m_contagiados}')


# 19.Liste el promedio de edad de contagiados por hombre y mujeres por ciudad por departamento

promedio_edad = data.groupby( ['Sexo', 'Nombre municipio', 'Nombre departamento']).Edad.mean()
print(f'Promedio de edad de contagiados por hombre y mujeres por ciudad por departamento: \n{promedio_edad}')


# 20.Liste de mayor a menor el número de contagiados por departamento de procedencia

departamento_procedencia = data['Nombre departamento'].value_counts()
print(f'Número de contagiados por departamento de procedencia: \n{departamento_procedencia}')


# 21.Liste de mayor a menor las fechas donde se presentaron mas contagios

fechas_mas_contagios = data['Fecha de diagnóstico' ].value_counts().sort_values(ascending=False)
print(f'Fechas donde se presentaron mas contagios:\n{fechas_mas_contagios}')


# 22.Diga cual es la tasa de mortalidad y recuperación que tiene toda Colombia

cantidad_muertes = data[data['Estado'] == 'Fallecido'].shape[0]
cantidad_recuperados = data[data['Recuperado'] == 'Recuperado'].shape[0]

tasa_mortalidad = cantidad_muertes / numero_casos * 100
tasa_recuperacion = cantidad_recuperados / numero_casos * 100

print(f'Tasa de mortalidad en Colombia: {tasa_mortalidad}')
print(f'Tasa de recuperacion en Colombia: {tasa_recuperacion}')


# 23. Liste la tasa de mortalidad y recuperación que tiene cada departamento

muertes_departamento = data[data['Estado'] == 'Fallecido'].groupby('Nombre departamento').size()
tasa_mortalidad_dpto = muertes_departamento /  numero_casos * 100
print(f'Tasa de mortalidad de cada departamento:\n{tasa_mortalidad_dpto}')

recuperacion_departamento = data[data['Recuperado'] == 'Recuperado'].groupby('Nombre departamento').size()
tasa_recuperacion_dpto = recuperacion_departamento /  numero_casos * 100
print(f'Tasa de recuperacion de cada departamento:\n{tasa_recuperacion_dpto}')


# 24.Liste la tasa de mortalidad y recuperación que tiene cada ciudad

muertes_municipio = data[data['Estado'] == 'Fallecido'].groupby('Nombre municipio').size()
tasa_mortalidad_munic = muertes_municipio /  numero_casos * 100
print(f'Tasa de mortalidad de cada municipio:\n{tasa_mortalidad_munic}')

recuperacion_municipio = data[data['Recuperado'] == 'Recuperado'].groupby('Nombre municipio').size()
tasa_recuperacion_munic = recuperacion_municipio /  numero_casos * 100
print(f'Tasa de recuperacion de cada municipio:\n{tasa_recuperacion_munic}')


# 25.Liste por cada ciudad la cantidad de personas por atención

cantidad_atencion = data.groupby(['Nombre municipio', 'Ubicación del caso']).size()
print(f'Cantidad de personas por atención:\n{cantidad_atencion}')


