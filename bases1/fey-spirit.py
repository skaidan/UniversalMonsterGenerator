# bases1/fey-spirit.py
"""
FeySpirit creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=fey-spirit
"""
from creature_base import GlobalCreatureBaseClass


class FeySpirit(GlobalCreatureBaseClass):
    """
    Small fey creature - FeySpirit
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 10, 'min_level': 1, 'level': 1, 'STR': 13, 'DEX': 16, 'CON': 14, 'INT': 14, 'WIS': 11, 'CHAR': 16, 'armor_class': 12, 'alignment': '- Armor Class  12 + the level of the spell (natural armor) Hit Points  30 + 10 for each spell level above 3rd Speed  40 ft. STR 13 (+1) DEX 16 (+3) CON 14 (+2) INT 14 (+2) WIS 11 (+0) CHA 16 (+3) Condition Immunities  charmed Senses  darkvision 60 ft.', 'legendary': False, 'size': 'Small', 'type': 'fey', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

