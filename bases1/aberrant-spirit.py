# bases1/aberrant-spirit.py
"""
AberrantSpirit creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=aberrant-spirit
"""
from creature_base import GlobalCreatureBaseClass


class AberrantSpirit(GlobalCreatureBaseClass):
    """
    Medium aberration creature - AberrantSpirit
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 10, 'min_level': 1, 'level': 1, 'STR': 16, 'DEX': 10, 'CON': 15, 'INT': 16, 'WIS': 10, 'CHAR': 6, 'armor_class': 11, 'alignment': '- Armor Class  11 + the level of the spell (natural armor) Hit Points  40 + 10 for each spell level above 4th Speed  30 ft.; fly 30 ft. (hover) (Beholderkin only) STR 16 (+3) DEX 10 (+0) CON 15 (+2) INT 16 (+3) WIS 10 (+0) CHA 6 (-2) Damage Immunities  psychic Senses  darkvision 60 ft.', 'legendary': False, 'size': 'Medium', 'type': 'aberration', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

