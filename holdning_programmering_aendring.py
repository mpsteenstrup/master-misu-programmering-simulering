import matplotlib.pyplot as plt
import numpy as np
import re
# Data konverteret fra dine strenge

s = "-100-1-10200-1-1-1-1-1-2-20-1-1-200"
numbers = [-1,0,0,-1,-1,0,2,0,0,-1,-1,-1,-1,-1,-2,-2,0,-1,-1,-2,0,0]
print(numbers)
# Definer intervaller (bins) - vi lægger 0.5 til for at centrere søjlerne over tallene
bins = np.arange(-3, 5) - 0.5

plt.figure(figsize=(10, 6))

# Tegn histogrammerne ved siden af hinanden
plt.hist([numbers], bins=bins, color=['#e74c3c'], edgecolor='black', alpha=0.8)

# Formatering
plt.title('Ændring i vurdering af sværhedsgrad')#, fontsize=14)
plt.xlabel('Værdi (Svar)', fontsize=12)
plt.ylabel('Antal besvarelser', fontsize=12)
plt.xticks(range(-3, 4))
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('holdning_programmering_aendring.png', dpi=300, bbox_inches='tight')
plt.show()