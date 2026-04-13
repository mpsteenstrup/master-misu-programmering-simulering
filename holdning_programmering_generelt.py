import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Indlæs data
df_pre = pd.read_csv('Programmering i globale tendenser - pre.csv')
df_post = pd.read_csv('Programmering i globale tendenser - post.csv')

# Funktion til at finde den rigtige kolonne baseret på et nøgleord
def get_column_data(df, keyword):
    for col in df.columns:
        if keyword.lower() in col.lower():
            # Tæl antal svar for 1, 2, 3, 4, 5. 
            # reindex sikrer at alle tal er med, selvom ingen har svaret det (f.eks. 0 svar på "1")
            return df[col].value_counts().reindex([1, 2, 3, 4, 5], fill_value=0)
    return None

# Opsætning af de 4 spørgsmål vi skal sammenligne (Nøgleord + Titel)
questions = [
    {
        "keyword": "værd at lærer", 
        "title": "Hvor værdifuldt er det at lære programmering?"
    },
    {
        "keyword": "hjælpe med at lærer fysik", 
        "title": "Kan programmering hjælpe med at lære fysik/matematik?"
    },
    {
        "keyword": "inden for naturvidenskab", 
        "title": "Anvendelighed inden for naturvidenskab"
    },
    {
        "keyword": "andre akademiske fag", 
        "title": "Anvendelighed inden for andre akademiske fag"
    }
]

# Opret plot (2x2 gitter)
fig, axes = plt.subplots(2, 2, figsize=(15, 10))
axes = axes.flatten() # Gør det nemmere at loope igennem
bar_width = 0.35
index = np.arange(1, 6) # x-akse værdier (1-5)

# Loop gennem spørgsmålene og lav graferne
for i, q in enumerate(questions):
    ax = axes[i]
    
    # Hent data
    pre_counts = get_column_data(df_pre, q["keyword"])
    post_counts = get_column_data(df_post, q["keyword"])
    
    # Tjek om vi fandt data
    if pre_counts is not None and post_counts is not None:
        # Tegn søjler
        rects1 = ax.bar(index - bar_width/2, pre_counts, bar_width, label='Pre', color='#1f77b4', alpha=0.8)
        rects2 = ax.bar(index + bar_width/2, post_counts, bar_width, label='Post', color="#fc0000", alpha=0.8)
        
        # Formatering
        ax.set_title(q["title"], fontsize=12, fontweight='bold')
        ax.set_xticks(index)
        ax.set_xlabel('Score (1-5)')
        ax.set_ylabel('Antal svar')
        ax.set_ylim(0, max(pre_counts.max(), post_counts.max()) + 2) # Lidt luft i toppen
        ax.legend()
        ax.grid(axis='y', linestyle='--', alpha=0.3)
        
        # Tilføj tal ovenpå søjlerne (valgfrit, men godt for overblik)
        ax.bar_label(rects1, padding=3)
        ax.bar_label(rects2, padding=3)

plt.tight_layout()
plt.show()