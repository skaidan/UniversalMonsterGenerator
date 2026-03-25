# bases1/shadow-spirit.py
"""
ShadowSpirit creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=shadow-spirit
"""
from creature_base import GlobalCreatureBaseClass


class ShadowSpirit(GlobalCreatureBaseClass):
    """
    Medium monstrosity creature - ShadowSpirit
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 10, 'min_level': 1, 'level': 1, 'STR': 13, 'DEX': 16, 'CON': 15, 'INT': 4, 'WIS': 10, 'CHAR': 16, 'armor_class': 11, 'alignment': '- Armor Class  11 + the level of the spell (natural armor) Hit Points  35 + 15 for each spell level above 3rd Speed  40 ft. STR 13 (+1) DEX 16 (+3) CON 15 (+2) INT 4 (-3) WIS 10 (+0) CHA 16 (+3) Damage Resistances  necrotic Condition Immunities  frightened Senses  darkvision 120 ft.', 'legendary': False, 'size': 'Medium', 'type': 'monstrosity', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

