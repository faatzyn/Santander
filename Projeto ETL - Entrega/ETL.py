# EXTRACT
import pandas as pd
df = pd.read_csv('santander_etl.csv')

# TRANSFORM
# Calculando Total sem Tributos
df['Valor Sem Tributos'] = df['Total Com Tributos'] - (
    df['Total Com Tributos'] * df["Aliquota Icms"] / 100
    + df['Total Com Tributos'] * df["Aliquota Pis"] / 100
    + df['Total Com Tributos'] * df["Aliquota Cofins"] / 100
)

# Calculando valor de ICMS
df['Valor de ICMS'] = df['Total Com Tributos'] * df["Aliquota Icms"] / 100

# Calculando valor de PIS
df['Valor de PIS'] = df['Total Com Tributos'] * df["Aliquota Pis"] / 100

# Calculando valor de COFINS
df['Valor de COFINS'] = df['Total Com Tributos'] * df["Aliquota Cofins"] / 100


# LOAD
# Salvei numa nova saida para não sobrescrever o CSV
df.to_csv('santander_etl_processado.csv')