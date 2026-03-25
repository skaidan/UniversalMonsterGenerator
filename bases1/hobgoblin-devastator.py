# bases1/hobgoblin-devastator.py
"""
HobgoblinDevastator creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=hobgoblin-devastator
"""
from creature_base import GlobalCreatureBaseClass


class HobgoblinDevastator(GlobalCreatureBaseClass):
    """
    Medium Fey (Goblinoid) creature - HobgoblinDevastator
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 45, 'min_level': 1, 'level': 1, 'STR': 13, 'DEX': 12, 'CON': 14, 'INT': 16, 'WIS': 13, 'CHAR': 11, 'armor_class': 13, 'alignment': 'typically Lawful Neutral Armor Class  13 (studded leather) Hit Points  45 (7d8 + 14) Speed  30 ft. STR 13 (+1) DEX 12 (+1) CON 14 (+2) INT 16 (+3) WIS 13 (+1) CHA 11 (+0) Skills  Arcana +5 Senses  darkvision 60 ft.', 'legendary': False, 'size': 'Medium', 'type': 'Fey (Goblinoid)', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

