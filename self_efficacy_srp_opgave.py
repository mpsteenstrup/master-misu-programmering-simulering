import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import min_stil  # Vi importerer din stilfil

# 1. Aktiver stilen
min_stil.aktiver_stil()

# 2. Indlæs data
df = pd.read_csv('Programmering i globale tendenser - post.csv')

# 3. Vælg kolonne og forbered data
# Vi tæller værdierne (1-5) ligesom i dit andet script for at få ensartet layout
kolonne_navn = "Projektet har omhandlet bevægelse nedad i et tyngdefelt. I i et andet projekt, eksempelvis i forbindelse med SRP, skal modellere en bil der bevæger sig vandret. I hvor høj grad føler I jer i stand til at ændre i koden og lave en analyse af denne situation?"

# Tæl forekomster af 1, 2, 3, 4, 5
counts = df[kolonne_navn].value_counts().reindex([1, 2, 3, 4, 5], fill_value=0)

# 4. Opsætning af figuren
fig, ax = plt.subplots(figsize=(8, 6))

# Lav bar-plottet med farven fra din stil-fil
index = np.arange(1, 6)
rects = ax.bar(index, counts, color=min_stil.FARVE_POST, edgecolor='black', alpha=0.8)

# 5. Formatering (matcher holdning-scriptet)
#ax.set_title('Modificering af kode til SRP kontekst')
ax.set_title('Post besvarelse til spørgsmålet: \n "Projektet har omhandlet bevægelse nedad i et tyngdefelt. \n I et andet projekt, eksempelvis i forbindelse med SRP, skal modellere en bil der bevæger sig vandret. \n I hvor høj grad føler I jer i stand til at ændre i koden og lave en analyse af denne situation?" \n skala 1: slet ikke - 5:jeg mener godt at jeg ville kunne det')
ax.set_xlabel('Værdi (Svar)')
ax.set_ylabel('Antal besvarelser')
ax.set_xticks(index)
ax.set_ylim(0, max(counts) + 1) # Giver lidt luft i toppen

# Tilføj tal ovenpå søjlerne
ax.bar_label(rects, padding=3)

# 6. Gem og vis
plt.tight_layout()
min_stil.gem_figur("self_efficacy_srp_opgave.png")
plt.show()