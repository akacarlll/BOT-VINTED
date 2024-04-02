import pandas as pd
from dateparser import parse

df= pd.read_csv("C:\\Users\\carlf\\OneDrive\\Bureau\\Technique de programmation\\BOT VINTED\\final_data.csv")
def get_dernier(df):
    df["Taille"] = df["Taille"].str.replace("Size information", "")
    df["État"] = df["État"].str.replace("Condition information", "")
    df["Localisation"] = df["Localisation"].str.replace("Localisation", "")
    df['Vues'] = df["Vues"].str.extract(r'(\d+)')



    df['Ajouté'] = df["Date d'ajout"].str.extract(r'(\d+) heures')
    df['Ajouté']  = df['Ajouté'].fillna(100).astype(int)
    df_sorted = df.sort_values(by='Ajouté', ascending=True)
    df_sorted.head(50)

    return df_sorted(3)

def lastlast():
    df = pd.read_csv("C:\\Users\\carlf\\OneDrive\\Bureau\\Technique de programmation\\BOT VINTED\\final_data.csv")
    dernier_items = get_dernier(df)
    print(dernier_items)

# Appeler la fonction main si ce script est exécuté en tant que programme principal
if __name__ == "__main__":
    lastlast()


