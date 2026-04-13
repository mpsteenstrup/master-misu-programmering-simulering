# Filnavn: min_stil.py
import matplotlib.pyplot as plt

# --- 1. FARVEPALET ---
# Vi definerer farverne som variabler her, så vi kun skal ændre dem ét sted
FARVE_PRE = "#1f77b4"   # Standard blå
FARVE_POST = "#c51b1b"  # Din valgte røde farve
FARVE_G = "#32c51b"
FARVE_NEUTRAL = "lightgray"

# --- 2. GENERELLE INDSTILLINGER (Globalt layout) ---
def aktiver_stil():
    """Kører en række indstillinger der standardiserer alle grafer"""
    
    # Skrifttyper og størrelser
    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['font.size'] = 12
    plt.rcParams['axes.titlesize'] = 14
#    plt.rcParams['axes.titleweight'] = 'bold'
    plt.rcParams['axes.labelsize'] = 12
    
    # Figur layout
    plt.rcParams['figure.figsize'] = (10, 6) # Standard størrelse
    plt.rcParams['figure.dpi'] = 100         # Opløsning
    
    # Gitter og akser
    plt.rcParams['axes.grid'] = True         # Slå gitter til som standard
    plt.rcParams['grid.alpha'] = 0.3         # Gør gitteret svagt
    plt.rcParams['grid.linestyle'] = '--'    # Stiplet gitter
    plt.rcParams['axes.axisbelow'] = True    # Læg gitter bag ved søjlerne
    
    # Farver på akser
    plt.rcParams['axes.edgecolor'] = '#333333'
    plt.rcParams['xtick.color'] = '#333333'
    plt.rcParams['ytick.color'] = '#333333'

# --- 3. HJÆLPEFUNKTIONER (Valgfrit) ---
def gem_figur(filnavn):
    """Gemmer figuren med ensartede indstillinger"""
    plt.savefig(filnavn, bbox_inches='tight', dpi=300)
    print(f"Figuren er gemt som: {filnavn}")