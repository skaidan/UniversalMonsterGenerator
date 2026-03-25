# bases1/lord-soth.py
"""
LordSoth creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=lord-soth
"""
from creature_base import GlobalCreatureBaseClass


class LordSoth(GlobalCreatureBaseClass):
    """
    Medium Undead (Paladin) creature - LordSoth
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 228, 'min_level': 1, 'level': 1, 'STR': 22, 'DEX': 11, 'CON': 20, 'INT': 12, 'WIS': 16, 'CHAR': 20, 'armor_class': 18, 'alignment': 'Lawful Evil Armor Class  18 (plate) Hit Points  228 (24d8 + 120) Speed  30 ft. STR 22 (+6) DEX 11 (+0) CON 20 (+5) INT 12 (+1) WIS 16 (+3) CHA 20 (+5) Saving Throws  Dex +6', 'legendary': False, 'size': 'Medium', 'type': 'Undead (Paladin)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

