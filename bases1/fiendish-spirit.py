# bases1/fiendish-spirit.py
"""
FiendishSpirit creature class scraped from https://www.aidedd.org/dnd/monstres.php?vo=fiendish-spirit
"""
from creature_base import GlobalCreatureBaseClass


class FiendishSpirit(GlobalCreatureBaseClass):
    """
    Large fiend creature - FiendishSpirit
    Source: AiDeDd Monster Database (D&D 5e SRD)
    """
    
    # Valores por defecto extraídos del scraping
    DEFAULT_STATS = {'hit_points': 50, 'min_level': 1, 'level': 1, 'STR': 13, 'DEX': 16, 'CON': 15, 'INT': 10, 'WIS': 10, 'CHAR': 16, 'armor_class': 12, 'alignment': '- Armor Class  12 + the level of the spell (natural armor) Hit Points  50 (Demon only) or 40 (Devil only) or 60 (Yugoloth only) + 15 for each spell level above 6th Speed  40 ft.; climb 40 ft. (Demon only); fly 60 ft. (Devil only) STR 13 (+1) DEX 16 (+3) CON 15 (+2) INT 10 (+0) WIS 10 (+0) CHA 16 (+3) Damage Resistances  fire Damage Immunities  poison Condition Immunities  poisoned Senses  darkvision 60 ft.', 'legendary': False, 'size': 'Large', 'type': 'fiend', 'hit_points_up': [1, 1, 1], 'STR_up': [1, 1, 0], 'DEX_up': [0, 1, 0], 'CON_up': [0, 0, 1], 'INT_up': [1, 0, 0], 'WIS_up': [0, 0, 1], 'CHAR_up': [0, 0, 0], 'abilities': []}

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

