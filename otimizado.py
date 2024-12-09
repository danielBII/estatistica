import pandas as pd
from scipy.stats import ranksums

# Dados Homens
nomes_homens = [
    "Max Park", "Luke Garrett", "Aaron Huynh", "Matty Hiroto Inaba", "Caleb Chen", "Ryan Pilat",
    # Adicionar mais nomes conforme necessário...
]
resultados_homens = [
    186, 232, 34, 59, 40, 121,
    # Adicionar mais resultados conforme necessário...
]
paises_homens = [
    "Estados Unidos", "Estados Unidos", "Estados Unidos", "Estados Unidos", "Estados Unidos", "Estados Unidos",
    # Adicionar mais países conforme necessário...
]
anos_homens = [
    2023, 2023, 2024, 2024, 2024, 2024,
    # Adicionar mais anos conforme necessário...
]
num_competicoes_homens = [
    186, 232, 34, 59, 40, 121,
    # Adicionar mais números conforme necessário...
]

# Dados Mulheres
nomes_mulheres = [
    "Nancy Liu", "Dana Yi", "Heidi Chan", "Kymberlyn Calderon", "Eva Kato", "Teri McAcy",
    # Adicionar mais nomes conforme necessário...
]
resultados_mulheres = [
    4.32, 4.98, 5, 5.2, 5.46, 5.71,
    # Adicionar mais resultados conforme necessário...
]
paises_mulheres = [
    "Estados Unidos", "Estados Unidos", "Estados Unidos", "Estados Unidos", "Estados Unidos", "Estados Unidos",
    # Adicionar mais países conforme necessário...
]
anos_mulheres = [
    2024, 2023, 2024, 2019, 2019, 2024,
    # Adicionar mais anos conforme necessário...
]
num_competicoes_mulheres = [
    31, 117, 44, 79, 97, 29,
    # Adicionar mais números conforme necessário...
]

# Criando DataFrames
df_homens = pd.DataFrame({
    "Nome": nomes_homens,
    "Resultado": resultados_homens,
    "País": paises_homens,
    "Ano": anos_homens,
    "Num_Comp": num_competicoes_homens
})

df_mulheres = pd.DataFrame({
    "Nome": nomes_mulheres,
    "Resultado": resultados_mulheres,
    "País": paises_mulheres,
    "Ano": anos_mulheres,
    "Num_Comp": num_competicoes_mulheres
})

# Realizando o teste de ranksums (equivalente ao teste U de Mann-Whitney)
u_statistic, p_value = ranksums(df_homens["Resultado"], df_mulheres["Resultado"])

# Calculando as médias
media_homens = df_homens["Resultado"].mean()
media_mulheres = df_mulheres["Resultado"].mean()

# Combinando os DataFrames para análise conjunta
df_combined = pd.concat([df_homens, df_mulheres], ignore_index=True)
percentual_paises_comb = df_combined["País"].value_counts(normalize=True) * 100

# Exibindo os resultados
print("Teste de Ranksums:")
print(f"U-Statistic: {u_statistic}")
print(f"P-Value: {p_value}\n")

print("Médias:")
print(f"Homens: {media_homens}")
print(f"Mulheres: {media_mulheres}\n")

print("Percentual de Representantes por País:")
print(percentual_paises_comb)
