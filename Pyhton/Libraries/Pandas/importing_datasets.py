import pandas as pd
import json

# IMPORTING CSV FILES

# if the file is in the same directory
df0 = pd.read_csv("pokemon.csv")

# can use the full path instead
df1 = pd.read_csv("C:/Users/bruny/Desktop/Bruno - Learning notes/pokemon.csv")

url = "https://raw.githubusercontent.com/codedex-io/datasets/refs/heads/main/pokemon/pokemon.csv"
df2 = pd.read_csv(url) # Pandas can read directly from a URL

# if the data was separated by something different than a comma
df3 = pd.read_csv("pokemon.tsv", sep="\t")

# to consider row 1 the header, rather than row 0
df4 = pd.read_csv("pokemon.csv", header=1)

# if a file has no header at all
df5 = pd.read_csv('pokemon.csv', header=None)
df5.columns = ['pokedex_number', 'name', 'type1', 'type2', 'attack', 'defense', 'speed']

# IMPORTING EXCEL FILES

# this will import the first sheet in the Excel file
df6 = pd.read_excel('sales.xlsx')

# or one sheet in particular
df7 = pd.read_excel('sales.xlsx', sheet_name='Q1 2026') 

# or all sheets at once
df8 = pd.read_excel("sales.xlsx", sheet_name=None)

# IMPORTING JSON FILES

# The basic form; just two column: "data" and "error"
df9 = pd.read_json('tiktok.json')

# Load JSON file
with open('tiktok.json', 'r') as f:
    raw_json = json.load(f)

# Convert the list of videos to a DataFrame
df = pd.DataFrame(raw_json['data']['videos'])