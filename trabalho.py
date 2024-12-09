import pandas as pd

# Dados Homens
nomes_homens = [
    "Max Park", "Luke Garrett", "Aaron Huynh", "Matty Hiroto Inaba", "Caleb Chen", "Ryan Pilat",
    "Asher Kim-Magierek", "Jerry Yao", "Max Siauw", "Carson Widjaja", "Sebastian Stone",
    "Brennen Lin", "Brendyn Dunagan", "Siddharth Reddy", "Patrick Ponce", "Dylan Miller",
    "Kyle Santucci", "Luke Griesser", "Dominic Redisi", "Morgan Yeh", "Nicolás Sánchez",
    "Varun Mohanraj", "Angel Armando Jaime Sánchez", "Sameer Aggarwal", "Zeke Mackay",
    "Tommy Cherry", "Dylan Baumbach", "Brian Johnson", "Cristian Samuel Carasco Peña",
    "Bill Wang", "Henry Lichner", "Jeremy Bulambot", "Tanzer Balimtas", "Christopher Sun",
    "Rami Sbahi", "Shaun Mack", "Luke Tycksen", "Zayn Khanani", "Matias Marcantoni-Nunez",
    "Christopher Yen", "Oliver Michael Sitja Sichel", "Phillip Lewicki", "Drew Brads",
    "Ben Zhao", "Ryan Wu", "Paul Mahvi", "Joaquin Ruenes Hernández", "Kenji Gipson-Nahman",
    "Blake Thompson", "Evan Liu", "Carter Thomas", "Zerui Cheng", "Jeriel James Thomas",
    "Lucas Etter", "Caleb Yao (姚英華)", "Simon Kellum", "Jacob Bennett", "Arhaan Sareen",
    "Christopher Chi", "Derek White", "Michael Nielsen", "Ayden Dincher", "Jackson Bodkin",
    "Brayden Adams", "Michael Lee", "Daniel Gutierrez", "Ethan Jan", "Luigi Soriano",
    "Aaron Jake Wong", "Andrew Moy", "Andrew Y, Feng", "Danny Sungin Park (박성인)",
    "William Greninger", "Ari Randers-Pehrson", "Keaton Ellis", "Krish Shah-Nathwani",
    "Peter Weyers", "Antoine Cantin", "Kerry Creech", "Zavian Valedon", "Matthew Lee",
    "Noah Kim", "Timothy Castle", "Tyler Howlett", "Tyler Robinson", "Zachary Ochs",
    "Daniel Karnaukh", "Ray Bai", "Dan Tran", "Jacob Nokes", "Jack Pfeifer", "Jeremy Anderson",
    "Collin Burns", "Jack Bellomy", "Nolan Wood", "Parker Trager", "Silas Breault",
    "Derek Hsieh", "Dylan Wang", "Jacob Schwartz"
]

# Resultados
resultados_homens = [
    186, 232, 34, 59, 40, 121, 67, 42, 152, 77, 55, 73, 32, 31, 133, 117, 62, 74, 41,
    39, 129, 112, 60, 128, 127, 102, 55, 180, 3, 61, 41, 30, 54, 46, 62, 83, 60, 146,
    32, 67, 41, 117, 48, 25, 85, 212, 55, 54, 198, 236, 55, 30, 34, 58, 51, 217, 56,
    52, 189, 111, 75, 53, 21, 52, 25, 73, 36, 70, 58, 29, 12, 80, 25, 81, 140, 112,
    45, 90, 56, 59, 51, 32, 105, 89, 84, 75, 132, 102, 80, 60, 86, 24, 55, 36, 65,
    69, 12, 70, 43, 64
]

# Países Homens e Anos Homens
paises_homens = [
    "Estados Unidos", "Estados Unidos", "Estados Unidos", "Estados Unidos", "Estados Unidos",
    "Estados Unidos", "Estados Unidos", "Estados Unidos", "Estados Unidos", "Canadá",
    "Estados Unidos", "Estados Unidos", "Estados Unidos", "Estados Unidos", "Canadá",
    "Estados Unidos", "Estados Unidos", "Canadá", "Estados Unidos", "Estados Unidos",
    "México", "Estados Unidos", "Estados Unidos", "República Dominicana", "Canadá",
    "Estados Unidos", "Estados Unidos", "Estados Unidos", "Estados Unidos", "Estados Unidos"
]

anos_homens = [
    2023, 2023, 2024, 2024, 2024, 2024, 2022, 2024, 2022, 2024, 2024, 2023, 2023, 2024,
    2024, 2024, 2022, 2024, 2019, 2022, 2024, 2023, 2022, 2024, 2024, 2023, 2024,
    2022, 2024, 2024, 2018, 2024, 2023, 2024, 2023, 2022, 2024, 2022, 2023, 2023,
    2017, 2022, 2022, 2024, 2024, 2024, 2017, 2024, 2024, 2023, 2022, 2015, 2024,
    2024, 2023, 2023, 2022, 2023, 2023, 2024, 2024, 2024, 2024, 2023, 2024, 2019,
    2024, 2024, 2024, 2022, 2024, 2024, 2017, 2023, 2024, 2018, 2022, 2023, 2024,
    2024, 2023, 2023, 2023, 2023, 2022, 2024, 2024, 2023, 2022, 2024, 2015, 2023,
    2024, 2024, 2024, 2022, 2019, 2023
]
num_competicoes_homens = [
    186, 232, 34, 59, 40, 121, 67, 42, 152, 77, 55, 73, 32, 31, 133, 117, 62, 74,
    41, 39, 129, 112, 60, 128, 127, 102, 55, 180, 3, 61, 41, 30, 54, 46, 62, 83,
    60, 146, 32, 67, 41, 117, 48, 25, 85, 212, 55, 54, 198, 236, 55, 30, 34, 58,
    51, 217, 56, 52, 189, 111, 75, 53, 21, 52, 25, 73, 36, 70, 58, 29, 12, 80, 25,
    81, 140, 112, 45, 90, 56, 59, 51, 32, 105, 89, 84, 75, 132, 102, 80, 60, 86,
    24, 55, 36, 65, 69, 12, 70, 43, 64
]


# Criando DataFrame
df_homens = pd.DataFrame({
    "Nome": nomes_homens,
    "Resultado": resultados_homens,
    "País": paises_homens,
    "Ano": anos_homens,
    "Num_Comp": num_competicoes_homens[:len(num_competicoes_homens)]

})

# Exibindo os dados
print(df_homens)

import pandas as pd

# Dados mulheres
nomes_mulheres = [
    "Nancy Liu", "Dana Yi", "Heidi Chan", "Kymberlyn Calderon", "Eva Kato", "Teri McAcy",
    "Katie Hull", "Salma Sydykov Méndez", "Catherine Connolly", "Chloe Gu", "Kate Grahame",
    "Caitlin Hutnyk", "Livia Kleiner", "Margot Audero", "Fiona Bao", "Amity Trace",
    "Katie Wymbs", "Melissa Su", "Ruby Lu (卢红)", "Isabella Corona", "Alyssa Bernardo",
    "Eden Soref", "Peri Le Dain", "Lauren Phung", "Anna Zhou", "Sylvia Crouch",
    "McKinley Carr", "Emily Wang", "Sophie Chan", "Alina Zhu", "Olivia Schroeder",
    "Aurora Moritz", "Megan Kuo", "Lucy Grace Bryson", "Sydney Weaver", "Kyra Joiner",
    "Maggie Jordan", "Jenna Hassan", "Mia Sponseller", "Sumi Lee", "Jack Krieg",
    "Samantha Raskind", "CJ Dresdner", "Skye Bateman", "Steph Prze", "Luz Joanna Vargas Echavarría",
    "Taj Bressert", "Yeana Kim", "Tiffany Chien", "Addison Dean", "Anna Leidner",
    "Suzanne Tyler", "Torah Hoover", "Nina Ozsvath", "Elizabeth Cutting", "Yuxuan Chen",
    "Lily McClelland", "Sadie Sullivan", "Maggie Jakopac", "Alana Chan", "Cailyn Hoover",
    "Emma Kemp", "Alison Meador", "Jenna Gain", "Jaiden Shum", "Kaitlyn Wong (王紀程)",
    "Hailey Schoelkopf", "Tatiauna Brown", "Jasmin Baltazar", "NJ Kim", "Gabrielle Enyenihi",
    "Julianna Bennett", "Lucinda Zhou", "Natalia Sosa", "Katie Hinkley", "Paola Claudio Fonseca",
    "Leia Jiang", "Jingyi Zhu", "Madalen Tanner", "Allison Li", "Syndey Zhou",
    "Mariana K, Lee", "Naomi Solnick", "Anshu Chennuru", "Aileen Vo", "Gabby Tijerina",
    "Emily Nguyen", "Flora Chan", "Jessica Ying", "Dagne Poveda", "Lucero Esmeralda Alvarado Ruíz",
    "Kailani Luu", "Kristin M, Dan", "Melanie Barber", "Patricia Li", "Maggie Clark",
    "Roxy Behrle", "Sophie Desgagne", "Clara Litman", "Tamar Ozsvath"
]

resultados_mulheres = [
    4.32, 4.98, 5, 5.2, 5.46, 5.71, 5.84, 5.95, 5.97, 6.02, 6.02, 6.04, 6.13, 6.15,
    6.38, 6.39, 6.43, 6.52, 6.6, 6.66, 6.76, 6.79, 6.82, 6.92, 7, 7.11, 7.12, 7.14,
    7.14, 7.15, 7.18, 7.2, 7.21, 7.22, 7.22, 7.23, 7.25, 7.31, 7.35, 7.35, 7.38,
    7.4, 7.41, 7.41, 7.45, 7.48, 7.51, 7.57, 7.61, 7.62, 7.62, 7.7, 7.73, 7.76,
    7.79, 7.87, 7.89, 7.89, 7.91, 7.95, 7.95, 8.02, 8.03, 8.04, 8.07, 8.12, 8.14,
    8.14, 8.19, 8.19, 8.2, 8.25, 8.26, 8.27, 8.31, 8.31, 8.35, 8.38, 8.39, 8.4,
    8.4, 8.42, 8.44, 8.45, 8.46, 8.48, 8.51, 8.51, 8.52, 8.55, 8.57, 8.58, 8.59,
    8.64, 8.66, 8.68, 8.7, 8.72, 8.74, 8.78
]

paises_mulheres = [
    "Estados Unidos", "Estados Unidos", "Estados Unidos", "Estados Unidos", "Estados Unidos",
    "Estados Unidos", "Estados Unidos", "México", "Canadá", "Estados Unidos", "Estados Unidos",
    "Canadá", "Estados Unidos", "Estados Unidos", "Estados Unidos", "Estados Unidos", "Estados Unidos",
    "Canadá", "Estados Unidos", "Canadá", "México", "República Dominicana", "Estados Unidos",
    "Canadá", "Canadá", "Estados Unidos", "Canadá", "Costa Rica", "México", "Canadá"
]

anos_mulheres = [
    2024, 2023, 2024, 2019, 2019, 2024, 2024, 2024, 2019, 2024, 2021, 2018, 2024, 2024,
    2024, 2023, 2023, 2019, 2023, 2020, 2023, 2024, 2019, 2019, 2023, 2024, 2023,
    2018, 2017, 2023, 2024, 2018, 2024, 2024, 2017, 2024, 2019, 2023, 2019, 2016,
    2026, 2017, 2024, 2024, 2024, 2023, 2024, 2023, 2016, 2024, 2018, 2019, 2024,
    2024, 2024, 2024, 2023, 2024, 2018, 2024, 2023, 2024, 2023, 2021, 2023, 2023,
    2023, 2024, 2024, 2024, 2024, 2017, 2024, 2024, 2024, 2020, 2024, 2022, 2024
]

num_competicoes_mulheres = [
    31, 117, 44, 79, 97, 29, 224, 27, 54, 6, 86, 21, 165, 81, 23, 76, 18, 19, 82, 17,
    27, 15, 69, 101, 26, 19, 33, 24, 26, 3, 24, 11, 18, 40, 23, 55, 34, 6, 38, 20,
    30, 45, 11, 30, 26, 6, 54, 9, 43, 16, 15, 7, 8, 67, 70, 93, 5, 7, 16, 7, 103,
    13, 43, 13, 9, 19, 15, 8, 5, 23, 2, 33, 23, 15, 30, 7, 41, 12, 10, 22, 10, 33,
    1, 61, 36, 4, 1, 24, 12, 20, 21, 7, 7, 6, 29, 53, 37, 15, 17, 66
]


# Criando DataFrame
df = pd.DataFrame({
    "Nome": nomes_mulheres[:len(num_competicoes_mulheres)],
    "Resultado": resultados_mulheres,
    "País": paises_mulheres[:len(num_competicoes_mulheres)],
    "Ano": anos_mulheres[:len(num_competicoes_mulheres)],
    "Num_Comp": num_competicoes_mulheres[:len(num_competicoes_mulheres)]
})

# Exibindo dados
print(df.head())
import pandas as pd
from scipy.stats import ranksums

# Criando DataFrames
df_homens = pd.DataFrame({
    "Nome": nomes_homens,
    "Resultado": resultados_homens,
    "País": paises_homens,
    "Ano": anos_homens,
    "Num": num_competicoes_homens[:len(num_competicoes_homens)]
})

df_mulheres = pd.DataFrame({
    "Nome": nomes_mulheres,
    "Resultado": resultados_mulheres,
    "País": paises_mulheres,
    "Ano": anos_mulheres,
    "/Num": num_competicoes_mulheres[:len(num_competicoes_mulheres)]
})

# Realizando o teste de Whitney U
u_statistic, p_value = ranksums(df_homens["Resultado"], df_mulheres["Resultado"])

# Calculando as médias
media_homens = df_homens["Resultado"].mean()
media_mulheres = df_mulheres["Resultado"].mean()

# Calculando o país com maior percentual de representantes (homens e mulheres juntos)
df_combined = pd.concat([df_homens, df_mulheres], ignore_index=True)
percentual_paises_comb = df_combined["País"].value_counts(normalize=True) * 100

# País com maior percentual de representantes entre homens
percentual_paises_homens = df_homens["País"].value_counts(normalize=True) * 100

# Exibindo os resultados
print("Teste de Whitney U:")
print("U-Statistic:", u_statistic)
print("P-Value:", p_value)

print("\nMédias:")
print("Média Homens:", media_homens)
print("Média Mulheres:", media_mulheres)

print("\nPaís com maior percentual de representantes (homens e mulheres):")
print(percentual_paises_comb.head(1))

print("\nPaís com maior percentual de representantes entre homens:")
print(percentual_paises_homens.head(1))