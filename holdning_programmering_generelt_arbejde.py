import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# HER IMPORTERER VI DIN NYE STIL-FIL
import min_stil 

# Aktiver stilen med det samme
min_stil.aktiver_stil()

# 1. INDLÆS DATA
df_pre = pd.read_csv('Programmering i globale tendenser - pre.csv')
df_post = pd.read_csv('Programmering i globale tendenser - post.csv')

# Hjælpefunktion til at hente data
def get_column_data(df, keyword):
    for col in df.columns:
        if keyword.lower() in col.lower():
            return df[col].value_counts().reindex([1, 2, 3, 4, 5], fill_value=0)
    return None

# Funktion til at lave en figur med 2 diagrammer
def lav_figur(sporgsmal_liste, figur_titel,filnavn):
    # Vi sætter figsize her, da det er specifikt for denne type plot (2 ved siden af hinanden)
    fig, axes = plt.subplots(1, 2, figsize=(14, 6)) 
    fig.suptitle(figur_titel, fontsize=16, fontweight='bold')
    
    bar_width = 0.35
    index = np.arange(1, 6)

    for i, (keyword, title) in enumerate(sporgsmal_liste):
        ax = axes[i]
        
        # Hent data
        post_counts = get_column_data(df_post, keyword)

        rects2 = ax.bar(index, post_counts, bar_width, 
                        color=min_stil.FARVE_PRE, # Den røde farve fra filen
                        edgecolor='black',
                        alpha=0.8)
        
        # Formatering (Resten klares af min_stil.aktiver_stil(), men titler er specifikke)
        ax.set_title(title)
        ax.set_xticks(index)
        ax.set_xlabel('Værdi')
        ax.set_ylabel('Antal')
        ax.set_ylim(0, max(post_counts.max(), post_counts.max()) + 2)
       # ax.legend()
        
        # Sæt tal på søjlerne
        ax.bar_label(rects2, padding=3)

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    min_stil.gem_figur(filnavn)
    plt.show()

# --- GENERER FIGUR 1 ---
par_1 = [
    ("fremtidige arbejde", "fremtidige arbejde med programmering")
]
lav_figur(par_1, "Værdi og Læring","holdning_programmering_generelt_arbejde")


# , ("forbindelse med SRP", " forbindelse med SRP")