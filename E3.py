'''3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa,
na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

IMPORTANTE:
a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;'''

import json
import pandas as pd
import numpy as np

with open("dados.json", encoding='utf-8') as meu_json:
    dados = json.load(meu_json)

df = pd.json_normalize(dados) 
indexNames = df[ df['valor'] == 0.000 ].index
df.drop(indexNames , inplace=True)

# O menor valor de faturamento ocorrido em um dia do mês;

min = df[['valor']].min().item()
print(f'O menor valor de faturamento foi de {min}')

# O maior valor de faturamento ocorrido em um dia do mês;

max = df[['valor']].max().item()
print(f'O menor valor de faturamento foi de {max}')

# Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.
media = df[['valor']].mean().item()
acmedia = df.loc[df['valor'] >media]['dia'].count()

print(f'A quantidade de dias em que o faturamento diário foi superior à média mensal é de {acmedia}')
