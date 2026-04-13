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
print(df_pre.head())
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
        pre_counts = get_column_data(df_pre, keyword)
        post_counts = get_column_data(df_post, keyword)
        
        if pre_counts is not None and post_counts is not None:
            # Tegn søjler - HER BRUGER VI FARVERNE FRA min_stil
            rects1 = ax.bar(index - bar_width/2, pre_counts, bar_width, 
                            label='Pre', 
                            color=min_stil.FARVE_PRE, 
                            edgecolor='black',
                            alpha=0.9)
            
            rects2 = ax.bar(index + bar_width/2, post_counts, bar_width, 
                            label='Post', 
                            color=min_stil.FARVE_POST, # Den røde farve fra filen
                            edgecolor='black',
                            alpha=0.8)
            
            # Formatering (Resten klares af min_stil.aktiver_stil(), men titler er specifikke)
            ax.set_title(title)
            ax.set_xticks(index)
            ax.set_xlabel('Værdi (Svar)')
            ax.set_ylabel('Antal besvarelser')
            ax.set_ylim(0, max(pre_counts.max(), post_counts.max()) + 2)
            ax.legend()
            
            # Sæt tal på søjlerne
            ax.bar_label(rects1, padding=3)
            ax.bar_label(rects2, padding=3)

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    min_stil.gem_figur(filnavn)
    plt.show()

# --- GENERER FIGUR 1 ---
par_1 = [
    ("værd at lærer", 'Pre-post svar på spørgsmålet: \n "I hvor høj grad mener du \n at det er værd at lærer at programmere?" \n skala: 1:ikke særligt meget værd - 5:stor værdi'),
    ("hjælpe med at lærer fysik", 'Pre-post svar på spørgsmålet: \n "I hvor høj grad tror du at programmering \n kan hjælpe med at lærer fysik og matematik?" \n skala: 1:ikke så meget - 5:rigtig meget')
]
lav_figur(par_1, "","holdning_programmering_generelt_2_1")


# --- GENERER FIGUR 2 ---
par_2 = [
    ("inden for naturvidenskab", 'Pre-post svar på spørgsmålet: \n "Hvor anvendeligt vurderer du evnen \n til at programmere  er inden for naturvidenskab?" \n skala: 1:ikke så anvendeligt - 5:meget anvendeligt'),
    ("andre akademiske fag", 'Pre-post svar på spørgsmålet: \n "Hvor anvendeligt vurderer du evnene til at programmere \n er inden for andre akademiske fag" \n skala: 1:ikke så anvendeligt - 5:meget anvendeligt')
]
lav_figur(par_2, "Anvendelse på tværs af fag","holdning_programmering_generelt_2_2")


