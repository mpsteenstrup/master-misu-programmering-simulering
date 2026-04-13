import matplotlib.pyplot as plt
import numpy as np
import min_stil
# Data konverteret fra dine strenge
pre_data = [int(d) for d in "423243324343332553452"]
post_data = [int(d) for d in "1121323213132111211311"]

# Definer intervaller (bins) - vi lægger 0.5 til for at centrere søjlerne over tallene
bins = np.arange(1, 7) - 0.5

plt.figure(figsize=(10, 6))

# Tegn histogrammerne ved siden af hinanden
plt.hist([pre_data, post_data], bins=bins, color=[min_stil.FARVE_PRE, min_stil.FARVE_POST], 
         label=['Pre-spørgeskema', 'Post-spørgeskema'], edgecolor='black', alpha=0.8)

# Formatering
plt.title('Pre- og Post-besvarelser: \n "I projektet kommer I til at arbejde med at ændre i eksisterende programmer. \n Hvor svært tror du at det kommer til at være." \n skala 1:let-5:svært')#, fontsize=14)
plt.xlabel('Værdi (Svar)', fontsize=12)
plt.ylabel('Antal besvarelser', fontsize=12)
plt.xticks(range(0, 7))
plt.legend(loc='upper right')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('holdning_programmering_self_efficacy.png', dpi=300, bbox_inches='tight')
plt.show()