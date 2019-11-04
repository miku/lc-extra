import pandas as pd

# Daten laden.
df = pd.read_excel("konkordanz_pica_gnd_pica_export.xls")

df["Pica Sbf-Bezeichnung"] = df["Pica Sbf-Bezeichnung"].str.upper()

# Ausschnitt, speichern.
df[["Pica3", "Pica Sbf-Bezeichnung"]].to_excel("output.xlsx")
