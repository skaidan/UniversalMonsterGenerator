# bases1/autumn-eladrin.py
"""
AutumnEladrin creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=autumn-eladrin
"""
from creature_base import GlobalCreatureBaseClass


class AutumnEladrin(GlobalCreatureBaseClass):
    """
    Medium Fey (Elf) creature - AutumnEladrin
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 165, 'min_level': 1, 'level': 1, 'STR': 12, 'DEX': 16, 'CON': 16, 'INT': 14, 'WIS': 17, 'CHAR': 18, 'armor_class': 19, 'alignment': 'typically Chaotic Neutral Armor Class  19 (natural armor) Hit Points  165 (22d8 + 66) Speed  30 ft. STR 12 (+1) DEX 16 (+3) CON 16 (+3) INT 14 (+2) WIS 17 (+3) CHA 18 (+4) Skills  Insight +7', 'legendary': False, 'size': 'Medium', 'type': 'Fey (Elf)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

