import pandas as pd


df = pd.read_csv("Gapminder.csv", error_bad_lines=False, sep=';')
print(df.head()) #Visualizando as 5 primeiras linhas

df = df.rename(columns={"country": "Pais",  "continent": "continente", "year": "Ano", "lifeExp": "Expectativa de vida", "pop": "Pop Total", "gdpPercap": "PIB"})# renomeando as colunas

df.head(10)

df.shape#Total de linhas e colunas
print(df.columns)#mostrar os nomes das colunas

print(df.dtypes)# mostra os tipos de cada coluna
print(df.tail())# mostra as ultimas linhas
print(df.describe())# retoina informações estatisticas
print(df['continente'].unique()) #retorna os volores dos continentes
Oceania = df.loc[df["continente"] == 'Oceania'] # serve para fazer filtros no banco de dados
print(Oceania.head())
df.groupby("continente")["Pais"].nunique()#tras uma contaem de qnt tem para cada continente
df.groupby("Ano")["Expectativa de vida"].mean()#
